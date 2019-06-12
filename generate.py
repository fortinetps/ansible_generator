#!/usr/bin/python
from jinja2 import Template, Environment, FileSystemLoader
import json
import autopep8
import os
import sys
import getopt

def replaceSpecialChars(str):
    return str.replace('-', '_').replace('.', '_').replace('+', 'plus')


def getModuleName(path, name):
    return replaceSpecialChars(path) + "_" + replaceSpecialChars(name)


def searchProperBreakableChar(line, startingPosition):
    breakableChars = " :.,;"
    for i in reversed(range(0, startingPosition)):
        if line[i] in breakableChars:
            return i
    return startingPosition


def numberOfInitialSpaces(line):
    return len(line)-len(line.lstrip())+2


def splitLargeLines(output):
    output = output.splitlines()
    for i in range(0, len(output)):
        line = output[i]
        if len(line) > 159:
            position = searchProperBreakableChar(line, 159)
            initialSpaces = " " * numberOfInitialSpaces(output[i])
            output.insert(i+1, initialSpaces + line[position:])
            output[i] = output[i][:position]
    output = '\n'.join(output)
    return output


def calculateFullPath(parent_attrs, attribute_name):
    return attribute_name if not parent_attrs else parent_attrs + ',' + attribute_name


def hyphenToUnderscore(data):
    if isinstance(data, list):
        for elem in data:
            elem = hyphenToUnderscore(elem)
        return data
    elif isinstance(data, dict):
        for k, v in data.items():
            if not (len(data) == 2 and 'name' in data and 'help' in data):
                # Only change hyphens for names and complex types. Simple types (enums) only contain name and help
                data[k] = hyphenToUnderscore(v)
        return data
    elif isinstance(data, str):
        return data.replace('-', '_')
    # elif isinstance(data, unicode):   # python3 all strings are unicode
    #     return data.encode('utf-8').replace('-', '_')
    else:
        return data


def renderModule(schema, version, special_attributes):

    file_loader = FileSystemLoader('ansible_templates')
    env = Environment(loader=file_loader,
                      lstrip_blocks=False, trim_blocks=False)

    schema['schema'] = hyphenToUnderscore(schema['schema'])

    short_description = schema['schema']['help'][:-1] + " in Fortinet's FortiOS and FortiGate."
    description = ""
    original_path = schema['path']
    original_name = schema['name']
    path = replaceSpecialChars(original_path)
    name = replaceSpecialChars(original_name)
    module_name = "fortios_" + path + "_" + name
    special_attributes_flattened = [','.join(x for x in elem) for elem in special_attributes]

    template = env.get_template('doc.jinja')
    output = template.render(**locals())

    template = env.get_template('examples.jinja')
    output += template.render(**locals())

    template = env.get_template('return.jinja')
    output += template.render(**locals())

    template = env.get_template('code.jinja')
    output += template.render(calculateFullPath=calculateFullPath, **locals())

    dir = 'output/' + version + '/' + path
    if not os.path.exists(dir):
        os.makedirs(dir)

    file = open('output/' + version + '/' + path + '/fortios_' + path + '_' + name + '.py', 'w')
    output = splitLargeLines(output)
    output = autopep8.fix_code(output, options={'aggressive': 1, 'max_line_length': 160})
    file.write(output)
    file.close()

    file_example = open('output/' + version + '/' + path + '/fortios_' + path +
                        '_' + name + '_example.yml', 'w')
    template = env.get_template('examples.jinja')
    output = template.render(**locals())
    lines = output.splitlines(True)
    file_example.writelines(lines[2:-1])
    file_example.close()

    print("\033[0mFile generated: " + 'output/' + version + '/\033[37mfortios_' + path + '_' + name + '.py')
    print("\033[0mFile generated: " + 'output/' + version + '/\033[37mfortios_' + path + '_' + name + '_example.yml')


def jinjaExecutor(number=None, schema=None):
    if schema is None:
        schema = 'fgt_schema.json'
    fgt_schema_file = open(schema).read()
    fgt_schema = json.loads(fgt_schema_file)
    fgt_sch_results = fgt_schema['results']

    special_attributes_file = open('special_attributes.lst').read()
    special_attributes = json.loads(special_attributes_file)

    if not number:
        real_counter = 0
        for i, pn in enumerate(fgt_sch_results):
            if 'diagnose' not in pn['path'] and 'execute' not in pn['path']:
                module_name = getModuleName(pn['path'], pn['name'])
                print ('\n\033[0mParsing schema:')
                print ('\033[0mModule name: \033[92m' + module_name)
                print ('\033[0mIteration:\033[93m' + str(real_counter) + "\033[0m, Schema position: \033[93m" + str(i))
                renderModule(fgt_sch_results[i],
                             fgt_schema['version'],
                             special_attributes[module_name] if module_name in special_attributes else [])
                real_counter += 1
    else:
        module_name = getModuleName(fgt_sch_results[number]['path'], fgt_sch_results[number]['name'])
        renderModule(fgt_sch_results[number],
                     fgt_schema['version'],
                     special_attributes[module_name] if module_name in special_attributes else [])


if __name__ == "__main__":
    schema = 'fgt_schema.json'
    opts, args = getopt.getopt(sys.argv[1:],"i:h", ["help"])
    for opt, arg in opts:
        if opt in ('-h', '--help'):
            print ("***********************************************************************************")
            print ("Usage: python generator.py -i <input_api_schema_file>")
            print ("")
            print ("  This script generates Ansible modules based API schema file")
            print ("")
            print ("  -i: input_api_schema_file, if not specified, default to use file fgt_schema.json")
            print ("")
            print ("***********************************************************************************")
            print ("examples:  ")
            print ("   python generator.py (default to use fgt_schema.json)")
            print ("   python generator.py -i fgt_monitor_schema.json")
            print ("***********************************************************************************")
            sys.exit(2)
        elif opt == '-i':
            schema = arg

    jinjaExecutor(schema=schema)
