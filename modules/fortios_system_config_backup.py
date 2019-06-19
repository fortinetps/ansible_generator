#!/usr/bin/python
from __future__ import (absolute_import, division, print_function)
# Copyright 2019 Fortinet, Inc.
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

__metaclass__ = type

from ansible.module_utils.basic import AnsibleModule
ANSIBLE_METADATA = {'status': ['preview'],
                    'supported_by': 'community',
                    'metadata_version': '1.1'}

DOCUMENTATION = '''
---
module: fortios_system_config_backup
short_description: Backup system config in Fortinet's FortiOS and FortiGate.
description:
    - This module is able to configure a FortiGate or FortiOS by allowing the
      user to set and modify system feature and config category.
      Examples include all parameters and values need to be adjusted to datasources before usage.
      Tested with FOS v6.0.2
version_added: "2.8"
author:
    - Miguel Angel Munoz (@mamunozgonzalez)
    - Nicolas Thomas (@thomnico)
notes:
    - Requires fortiosapi library developed by Fortinet
    - Run as a local_action in your playbook
requirements:
    - fortiosapi>=0.9.8
options:
    host:
       description:
            - FortiOS or FortiGate ip address.
       required: true
    username:
        description:
            - FortiOS or FortiGate username.
        required: true
    password:
        description:
            - FortiOS or FortiGate password.
        default: ""
    vdom:
        description:
            - Virtual domain, among those defined previously. A vdom is a
              virtual instance of the FortiGate that can be configured and
              used as a different unit.
        default: root
    https:
        description:
            - Indicates if the requests towards FortiGate must use HTTPS
              protocol
        type: bool
        default: true
    state:
        description:
            - Indicates whether to create or remove the object
        choices:
            - present
            - absent
    system_config:
        description:
            - Backup system config.
        default: null
        suboptions:
            destination:
                description:
                    - Configuration file destination [file* | usb].
                choices:
                    - file
                    - usb
            filename:
                description:
                    - "When using 'file' destination: the filename to save to on the local file system."
            password:
                description:
                    - Password to encrypt configuration data..
            scope:
                description:
                    - Specify global or VDOM only backup [global | vdom].
                required: true
                choices:
                    - global
                    - vdom
            usb_filename:
                description:
                    - "When using 'usb' destination: the filename to save to on the connected USB device."
            vdom:
                description:
                    - If 'vdom' scope specified, the name of the VDOM to backup configuration.
'''

EXAMPLES = '''
- hosts: localhost
  vars:
   host: "192.168.122.40"
   username: "admin"
   password: ""
   vdom: "root"
  tasks:
  - name: Backup system config.
    fortios_system_config_backup:
      host:  "{{ host }}"
      username: "{{ username }}"
      password: "{{ password }}"
      vdom:  "{{ vdom }}"
      https: "False"
      system_config:
        destination: "file"
        filename: "<your_own_value>"
        password: "<your_own_value>"
        scope: "global"
        usb_filename: "<your_own_value>"
        vdom: "<your_own_value>"
'''

RETURN = '''
build:
  description: Build number of the fortigate image
  returned: always
  type: str
  sample: '1547'
http_method:
  description: Last method used to provision the content into FortiGate
  returned: always
  type: str
  sample: 'PUT'
http_status:
  description: Last result given by FortiGate on last operation applied
  returned: always
  type: str
  sample: "200"
mkey:
  description: Master key (id) used in the last call to FortiGate
  returned: success
  type: str
  sample: "id"
name:
  description: Name of the table used to fulfill the request
  returned: always
  type: str
  sample: "urlfilter"
path:
  description: Path of the table used to fulfill the request
  returned: always
  type: str
  sample: "webfilter"
revision:
  description: Internal revision number
  returned: always
  type: str
  sample: "17.0.2.10658"
serial:
  description: Serial number of the unit
  returned: always
  type: str
  sample: "FGVMEVYYQT3AB5352"
status:
  description: Indication of the operation's result
  returned: always
  type: str
  sample: "success"
vdom:
  description: Virtual domain used
  returned: always
  type: str
  sample: "root"
version:
  description: Version of the FortiGate
  returned: always
  type: str
  sample: "v5.6.3"

'''


def login(data, fos):
    host = data['host']
    username = data['username']
    password = data['password']

    fos.debug('on')
    if 'https' in data and not data['https']:
        fos.https('off')
    else:
        fos.https('on')

    fos.login(host, username, password)


def filter_system_config_data(json):
    option_list = ['destination', 'filename', 'password',
                   'scope', 'usb_filename', 'vdom']
    dictionary = {}

    for attribute in option_list:
        if attribute in json and json[attribute] is not None:
            dictionary[attribute] = json[attribute]

    return dictionary


def underscore_to_hyphen(data):
    return data


def system_config(data, fos, check_mode=False):
    vdom = data['vdom']

    system_config_data = data['system_config']
    filtered_data = underscore_to_hyphen(filter_system_config_data(system_config_data))

    # path-name-code-inject from schema begin
    del filtered_data['filename']

    return fos.monitor('system',
                       'config/backup',
                       parameters=filtered_data,
                       vdom=vdom)
    # path-name-code-inject from schema end

    return fos.monitor('system',
                       'config/backup',
                       data=filtered_data,
                       vdom=vdom)


def is_successful_status(status):
    return status['status'] == "success" or \
        status['http_method'] == "DELETE" and status['http_status'] == 404


def fortios_system(data, fos, check_mode=False):
    login(data, fos)

    if data['system_config']:
        resp = system_config(data, fos, check_mode)

    # fortios-path-code-inject from schema begin
    with open(data['system_config']['filename'], mode='wb') as f:
        f.write(resp.text.encode('utf-8'))
    _resp = {}
    _resp['status'] = 'success'
    resp = _resp
    # fortios-path-code-inject from schema end

    fos.logout()
    return not is_successful_status(resp), \
        resp['status'] == "success", \
        resp


def main():
    fields = {
        "host": {"required": True, "type": "str"},
        "username": {"required": True, "type": "str"},
        "password": {"required": False, "type": "str", "no_log": True},
        "vdom": {"required": False, "type": "str", "default": "root"},
        "https": {"required": False, "type": "bool", "default": True},
        "system_config": {
            "required": True, "type": "dict",
            "options": {
                "destination": {"required": False, "type": "str",
                                "choices": ["file", "usb"]},
                "filename": {"required": False, "type": "str"},
                "password": {"required": False, "type": "str"},
                "scope": {"required": True, "type": "str",
                          "choices": ["global", "vdom"]},
                "usb_filename": {"required": False, "type": "str"},
                "vdom": {"required": False, "type": "str"}

            }
        }
    }

    module = AnsibleModule(argument_spec=fields,
                           supports_check_mode=True)
    try:
        from fortiosapi import FortiOSAPI
    except ImportError:
        module.fail_json(msg="fortiosapi module is required")

    fos = FortiOSAPI()

    is_error, has_changed, result = fortios_system(module.params, fos, module.check_mode)

    if not is_error:
        module.exit_json(changed=has_changed, meta=result)
    else:
        module.fail_json(msg="Error in repo", meta=result)


if __name__ == '__main__':
    main()
