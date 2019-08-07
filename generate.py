#!/usr/bin/python
from jinja2 import Template, Environment, FileSystemLoader
import json
import autopep8
import os
import sys
import getopt

def replaceSpecialChars(str):
    return str.replace('-', '_').replace('.', '_').replace('+', 'plus')


def getModuleName(path, name, monitor=None):
    return replaceSpecialChars(path) + "_" + replaceSpecialChars(name) + replaceSpecialChars('' if monitor is None else '_' + monitor)  # Monitor API uri ends with extra monitor action


def searchProperBreakableChar(line, startingPosition):
    breakableChars = " :.,;"
    for i in reversed(range(0, startingPosition)):
        if line[i] in breakableChars:
            return i
    return startingPosition


def numberOfInitialSpaces(line):
    return len(line) - len(line.lstrip()) + 2


def splitLargeLines(output):
    output = output.splitlines()
    for i in range(0, len(output)):
        line = output[i]
        if len(line) > 159:
            position = searchProperBreakableChar(line, 159)
            initialSpaces = " " * numberOfInitialSpaces(output[i])
            output.insert(i + 1, initialSpaces + line[position:])
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
            if not (len(data) == 2 and 'name' in data and 'help' in data) and \
                k != 'help':
                # Only change hyphens for names and complex types.
                # Simple types (enums) only contain name and help
                # Also, avoid changing hyphens in 'help' attributes
                data[k] = hyphenToUnderscore(v)
        return data
    elif isinstance(data, str):
        return data.replace('-', '_')
    # elif isinstance(data, unicode):   # python3 all strings are unicode
    #     return data.encode('utf-8').replace('-', '_')
    else:
        return data


def renderModule(schema, version, special_attributes):

    # Generate module
    file_loader = FileSystemLoader('ansible_templates')
    env = Environment(loader=file_loader,
                      lstrip_blocks=False, trim_blocks=False)

    schema['schema'] = hyphenToUnderscore(schema['schema'])

    short_description = schema['schema']['help'][:-1] + " in Fortinet's FortiOS and FortiGate."
    description = ""
    original_path = schema['path']
    original_name = schema['name']
    original_monitor = schema.get('monitor')
    original_fortiosapi = schema.get('fortiosapi')
    
    path = replaceSpecialChars(original_path)
    name = replaceSpecialChars(original_name)
    monitor = None if original_monitor is None else replaceSpecialChars(original_monitor)
    module_name = "fortios_" + path + "_" + name + ("" if monitor is None else "_" + monitor)
    fortiosapi = None if original_fortiosapi is None else replaceSpecialChars(original_fortiosapi)
    special_attributes_flattened = [','.join(x for x in elem) for elem in special_attributes]

    template = env.get_template('doc.j2')
    output = template.render(calculateFullPath=calculateFullPath, **locals())

    template = env.get_template('examples.j2')
    output += template.render(**locals())

    template = env.get_template('return.j2')
    output += template.render(**locals())

    template = env.get_template('code.j2')
    output += template.render(calculateFullPath=calculateFullPath, **locals())

    dir = 'output/' + version + '/' + path
    if not os.path.exists(dir):
        os.makedirs(dir)

    file = open('output/' + version + '/' + path + '/fortios_' + path + '_' + name + ("" if monitor is None else "_" + monitor) + '.py', 'w')
    output = splitLargeLines(output)
    file.write(output)
    file.close()

    # Generate example
    file_example = open('output/' + version + '/' + path + '/fortios_' + path +
                        '_' + name + ("" if monitor is None else "_" + monitor) + '_example.yml', 'w')
    template = env.get_template('examples.j2')
    output = template.render(**locals())
    lines = output.splitlines(True)
    file_example.writelines(lines[2:-1])
    file_example.close()

    # Generate test
    file_example = open('output/' + version + '/' + path + '/test_fortios_' + path +
                        '_' + name + ("" if monitor is None else "_" + monitor) + '.py', 'w')
    template = env.get_template('tests.j2')
    output = template.render(**locals())
    lines = output.splitlines(True)
    file_example.writelines(lines)
    file_example.close()

    print("\033[0mFile generated: " + 'output/' + version + '/\033[37mfortios_' + path + '_' + name + '.py')
    print("\033[0mFile generated: " + 'output/' + version + '/\033[37mfortios_' + path + '_' + name + '_example.yml')
    print("\033[0mFile generated: " + 'output/' + version + '/\033[37mtest_fortios_' + path + '_' + name + '.py')



def jinjaExecutor(number=None, schema=None):
    if schema is None:
        schema = 'fgt_schema.json'
    fgt_schema_file = open(schema).read()
    fgt_schema = json.loads(fgt_schema_file)
    fgt_sch_results = fgt_schema['results']

    special_attributes_file = open('special_attributes.lst').read()
    special_attributes = json.loads(special_attributes_file)

    autopep_files = './output/' + fgt_schema['version']

    if not number:
        real_counter = 0
        for i, pn in enumerate(fgt_sch_results):
            if 'diagnose' not in pn['path'] and 'execute' not in pn['path']:
                module_name = getModuleName(pn['path'], pn['name'])
                print('\n\033[0mParsing schema:')
                print('\033[0mModule name: \033[92m' + module_name)
                print('\033[0mIteration:\033[93m' + str(real_counter) + "\033[0m, Schema position: \033[93m" + str(i))
                renderModule(fgt_sch_results[i],
                             fgt_schema['version'],
                             special_attributes[module_name] if module_name in special_attributes else [])
                real_counter += 1
    else:
        module_name = getModuleName(fgt_sch_results[number]['path'], fgt_sch_results[number]['name'])
        renderModule(fgt_sch_results[number],
                     fgt_schema['version'],
                     special_attributes[module_name] if module_name in special_attributes else [])

        autopep_files = './output/' + \
                fgt_schema['version'] + '/' + \
                replaceSpecialChars(fgt_sch_results[number]['path']) + \
                '/fortios_' + replaceSpecialChars(fgt_sch_results[number]['path']) + '_' + replaceSpecialChars(fgt_sch_results[number]['name']) + '.py'

        autopep_files += ' ./output/' + \
                fgt_schema['version'] + '/' + \
                replaceSpecialChars(fgt_sch_results[number]['path']) + \
                '/test_fortios_' + replaceSpecialChars(fgt_sch_results[number]['path']) + '_' + replaceSpecialChars(fgt_sch_results[number]['name']) + '.py'


    print("\n\n\033[0mExecuting autopep8 ....")
    # Note this is done with popen and not with autopep8.fix_code in order to get the multiprocessig optimization, only available from CLI
    os.popen('autopep8 --aggressive --max-line-length 160 --jobs 8 --ignore E402 --in-place --recursive ' + autopep_files)
    # Avoid this check since it conflicts with Ansible guidelines:
    # E402 - Fix module level import not at top of file

    # Fix exceptional issues due to bugs in autopep
    # Using os.popen for quick edit and modification. Should be replaced by proper Python calls
    print("\n\n\033[0mFinal fixes ....")
    if os.path.isfile("/wireless_controller_hotspot20/fortios_wireless_controller_hotspot20_anqp_ip_address_type.py"):
        os.popen("sed -i 's/filtered_data =/filtered_data = \\\/' ./output/" + fgt_schema['version'] + "/wireless_controller_hotspot20/fortios_wireless_controller_hotspot20_anqp_ip_address_type.py")
    if os.path.isfile("/wireless_controller_hotspot20/fortios_wireless_controller_hotspot20_anqp_network_auth_type.py"):
        os.popen("sed -i 's/filtered_data =/filtered_data = \\\/' ./output/" + fgt_schema['version'] + "/wireless_controller_hotspot20/fortios_wireless_controller_hotspot20_anqp_network_auth_type.py")
    if os.path.isfile("/wireless_controller_hotspot20/fortios_wireless_controller_hotspot20_anqp_roaming_consortium.py"):
        os.popen("sed -i 's/filtered_data =/filtered_data = \\\/' ./output/" + fgt_schema['version'] + "/wireless_controller_hotspot20/fortios_wireless_controller_hotspot20_anqp_roaming_consortium.py")
    if os.path.isfile("/wireless_controller_hotspot20/fortios_wireless_controller_hotspot20_h2qp_conn_capability.py"):
        os.popen("sed -i 's/filtered_data =/filtered_data = \\\/' ./output/" + fgt_schema['version'] + "/wireless_controller_hotspot20/fortios_wireless_controller_hotspot20_h2qp_conn_capability.py")
    os.popen("find . -name 'test_fortios_router_bfd*.py' -exec rm {} \\;")
    os.popen("cp ./output/v6.0.2/system/test_fortios_system_*.py /workspaces/ansible/test/units/modules/network/fortios/ && cp ./output/v6.0.2/system/fortios_system_*.py /workspaces/ansible/lib/ansible/modules/network/fortios/")

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
