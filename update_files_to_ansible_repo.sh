#!/bin/bash

original_dir=$(pwd)
ansible_dir=$1

if [ -z $1 ]; then
  me=`basename "$0"`
  echo "Please indicate the root of the Ansible repository where you want to put generated files."
  echo "   e.g.:"
  echo "         ./${me} ~/ansible"
  echo ""
  exit -1
fi

if [ ! -f ${ansible_dir}/MANIFEST.in ] || 
   [ ! -d ${ansible_dir}/lib/ansible/modules/network/fortios/ ] || 
   [ ! -d ${ansible_dir}/test/units/modules/network/fortios/ ]; then
  echo "Directory does not look like an official Ansible Repository."
  exit -1

fi

cd ${ansible_dir}
git checkout devel

pull_request_name="fortios_update_first_group"

git checkout -b ${pull_request_name}
git checkout ${pull_request_name}

module_list="fortios_antivirus_heuristic
fortios_antivirus_profile
fortios_antivirus_quarantine
fortios_antivirus_settings
fortios_application_custom
fortios_application_group
fortios_application_list
fortios_application_name
fortios_application_rule_settings
fortios_authentication_rule
fortios_authentication_scheme
fortios_authentication_setting
fortios_dlp_filepattern
fortios_dlp_fp_doc_source
fortios_dlp_fp_sensitivity
fortios_dlp_sensor
fortios_dlp_settings
fortios_dnsfilter_domain_filter
fortios_dnsfilter_profile
fortios_endpoint_control_client"


for module in ${module_list}; do
  module_located=""
  test_module_located=""

  echo -e "\n\033[0mIteration: \033[93m" ${module}
  
  module_located=$(find ${original_dir} -name "${module}.py")
  echo -e "\033[0mLocated in: \033[92m"${module_located}

  cp ${module_located} ${ansible_dir}/lib/ansible/modules/network/fortios/
  git add ${ansible_dir}/lib/ansible/modules/network/fortios/${module}.py

  test_module_located=$(find ${original_dir} -name "test_${module}.py")
  echo -e "\033[0mTest file:  \033[92m"${test_module_located}

  if [ ! -z ${test_module_located} ]; then 
    cp ${test_module_located} ${ansible_dir}/test/units/modules/network/fortios/
    git add ${ansible_dir}/test/units/modules/network/fortios/test_${module}.py
  fi


done

exit 0