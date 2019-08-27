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

# pull_request_name and module_list are repeated over the code.
# The intention is to run this script with a single pull_request_name
# and module_list. Choose the one you need and delete the rest

pull_request_name="fortios_update_first_group"

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


pull_request_name="fortios_update_second_group"

module_list="fortios_endpoint_control_forticlient_ems
fortios_endpoint_control_forticlient_registration_sync
fortios_endpoint_control_profile
fortios_endpoint_control_settings
fortios_extender_controller_extender
fortios_firewall_address6
fortios_firewall_address6_template
fortios_firewall_address
fortios_firewall_addrgrp6
fortios_firewall_addrgrp
fortios_firewall_auth_portal
fortios_firewall_central_snat_map
fortios_firewall_dnstranslation
fortios_firewall_DoS_policy6
fortios_firewall_DoS_policy
fortios_firewall_identity_based_route
fortios_firewall_interface_policy6
fortios_firewall_interface_policy
fortios_firewall_internet_service_custom
fortios_firewall_internet_service"

pull_request_name="fortios_update_third_group"

module_list="fortios_firewall_internet_service_group
fortios_firewall_ipmacbinding_setting
fortios_firewall_ipmacbinding_table
fortios_firewall_ippool6
fortios_firewall_ippool
fortios_firewall_ip_translation
fortios_firewall_ipv6_eh_filter
fortios_firewall_ldb_monitor
fortios_firewall_local_in_policy6
fortios_firewall_local_in_policy
fortios_firewall_multicast_address6
fortios_firewall_multicast_address
fortios_firewall_multicast_policy6
fortios_firewall_multicast_policy
fortios_firewall_policy46
fortios_firewall_policy64
fortios_firewall_policy6
fortios_firewall_policy
fortios_firewall_profile_group
fortios_firewall_profile_protocol_options"

pull_request_name="fortios_update_fourth_group"

module_list="fortios_firewall_proxy_address
fortios_firewall_proxy_addrgrp
fortios_firewall_proxy_policy
fortios_firewall_schedule_group
fortios_firewall_schedule_onetime
fortios_firewall_schedule_recurring
fortios_firewall_service_category
fortios_firewall_service_custom
fortios_firewall_service_group
fortios_firewall_shaper_per_ip_shaper
fortios_firewall_shaper_traffic_shaper
fortios_firewall_shaping_policy
fortios_firewall_shaping_profile
fortios_firewall_sniffer
fortios_firewall_ssh_host_key
fortios_firewall_ssh_local_ca
fortios_firewall_ssh_local_key
fortios_firewall_ssh_setting
fortios_firewall_ssl_server
fortios_firewall_ssl_setting"


pull_request_name="fortios_update_fifth_group"

module_list="fortios_firewall_ssl_ssh_profile
fortios_firewall_ttl_policy
fortios_firewall_vip46
fortios_firewall_vip64
fortios_firewall_vip6
fortios_firewall_vip
fortios_firewall_vipgrp46
fortios_firewall_vipgrp64
fortios_firewall_vipgrp6
fortios_firewall_vipgrp
fortios_firewall_wildcard_fqdn_custom
fortios_firewall_wildcard_fqdn_group
fortios_ftp_proxy_explicit
fortios_icap_profile
fortios_icap_server
fortios_ips_custom
fortios_ips_decoder
fortios_ips_global
fortios_ips_rule
fortios_ips_rule_settings"


pull_request_name="fortios_update_sixth_group"

module_list="fortios_ips_sensor
fortios_ips_settings
fortios_log_custom_field
fortios_log_disk_filter
fortios_log_disk_setting
fortios_log_eventfilter
fortios_log_fortianalyzer2_filter
fortios_log_fortianalyzer2_setting
fortios_log_fortianalyzer3_filter
fortios_log_fortianalyzer3_setting
fortios_log_fortianalyzer_filter
fortios_log_fortianalyzer_override_filter
fortios_log_fortianalyzer_override_setting
fortios_log_fortianalyzer_setting
fortios_log_fortiguard_filter
fortios_log_fortiguard_override_filter
fortios_log_fortiguard_override_setting
fortios_log_fortiguard_setting
fortios_log_gui_display
fortios_log_memory_filter"


pull_request_name="fortios_update_seventh_group"

module_list="fortios_log_memory_global_setting
fortios_log_memory_setting
fortios_log_null_device_filter
fortios_log_null_device_setting
fortios_log_setting
fortios_log_syslogd2_filter
fortios_log_syslogd2_setting
fortios_log_syslogd3_filter
fortios_log_syslogd3_setting
fortios_log_syslogd4_filter
fortios_log_syslogd4_setting
fortios_log_syslogd_filter
fortios_log_syslogd_override_filter
fortios_log_syslogd_override_setting
fortios_log_syslogd_setting
fortios_log_threat_weight
fortios_log_webtrends_filter
fortios_log_webtrends_setting
fortios_report_chart
fortios_report_dataset"

pull_request_name="fortios_update_eighth_group"

module_list="fortios_report_layout
fortios_report_setting
fortios_report_style
fortios_report_theme
fortios_router_access_list
fortios_router_auth_path
fortios_router_bfd6
fortios_router_bfd
fortios_router_bgp
fortios_router_multicast6
fortios_router_multicast
fortios_router_multicast_flow
fortios_router_ospf6
fortios_router_ospf
fortios_router_policy6
fortios_router_policy
fortios_router_prefix_list
fortios_router_rip
fortios_router_setting
fortios_router_static"

pull_request_name="fortios_update_nineth_group"

module_list="
fortios_spamfilter_profile
fortios_ssh_filter_profile
fortios_switch_controller_global
fortios_switch_controller_lldp_profile
fortios_switch_controller_lldp_settings
fortios_switch_controller_mac_sync_settings
fortios_switch_controller_managed_switch
fortios_switch_controller_network_monitor_settings
fortios_system_accprofile
fortios_system_admin
fortios_system_api_user
fortios_system_central_management
fortios_system_dhcp_server
fortios_system_dns
fortios_system_global
fortios_system_interface
fortios_system_sdn_connector
fortios_system_settings
fortios_system_vdom
fortios_system_virtual_wan_link"

cd ${ansible_dir}
git checkout devel

git checkout -b ${pull_request_name}
git checkout ${pull_request_name}

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