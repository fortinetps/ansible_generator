#!/bin/bash

#set -x

cd $( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null && pwd )

trap ctrl_c SIGINT
trap ctrl_c SIGTERM

START_TIME=$SECONDS

function ctrl_c() {
    echo "** Interrupted by user **"
    ELAPSED_TIME=$(($SECONDS - $START_TIME))
    echo -e "\n\n Total time: ${ELAPSED_TIME} s\n\n Results: \n  Success: ${success}  Failed: ${failed}\n\n  Failed test cases: \n ${list_of_failed[@]} \n"
    exit
}

if [ ! -z $1 ] && [ "$1"="--https" ]; then
  https=true
fi

rm -f $(pwd)/examples/*.retry
rm -f $(pwd)/examples/*.https
rm -f $(pwd)/examples/remove/*.retry
rm -f $(pwd)/examples/remove/*.https

version="v6.0.5"

success=0
failed=0
list_of_failed=()

function modify_playbook_for_https() {
    cat $1 |sed 's/{{ vdom }}"/{{ vdom }}"\n      https: true/g' > $1.https
}

function run_example( ) {

    export ANSIBLE_LIBRARY=$(pwd)/output/${version}/$1

    filename=./examples/$2
    filename_removal=./examples/remove/$2

    echo -e "\n \e[36mRunning playbook:\e[0m \e[32m${filename}\e[0m \n"

    if [ "$https" = true ]; then 
        modify_playbook_for_https ${filename}
        ansible-playbook ${filename}.https
        if [ $? == 0 ]; then
          success=$(($success+1))
        else
          failed=$(($failed+1))
          list_of_failed+=($2"\n")
        fi
        rm ${filename}.https
    else
        ansible-playbook ${filename}
        if [ $? == 0 ]; then
          success=$(($success+1))
        else
          failed=$(($failed+1))
          list_of_failed+=($2"\n")
        fi
    fi

    if [ -f examples/remove/$2 ]; then 
    
        echo -e "\n \e[36mRunning playbook:\e[0m \e[32m${filename_removal}\e[0m \n"
    
        if [ "$https" == true ]; then 
            modify_playbook_for_https ${filename_removal}
            ansible-playbook ${filename_removal}.https
            if [ $? == 0 ]; then
            success=$(($success+1))
            else
            failed=$(($failed+1))
            list_of_failed+=("remove/"$2"\n")
            fi
            rm ${filename_removal}.https
        else
            ansible-playbook ${filename_removal}
            if [ $? == 0 ]; then
            success=$(($success+1))
            else
            failed=$(($failed+1))
            list_of_failed+=("remove/"$2"\n")
            fi
        fi
    fi
}

run_example antivirus fortios_antivirus_heuristic_example.yml
run_example antivirus fortios_antivirus_profile_example.yml
run_example antivirus fortios_antivirus_quarantine_example.yml
run_example antivirus fortios_antivirus_settings_example.yml
run_example application fortios_application_custom_example.yml
run_example application fortios_application_group_example.yml
run_example application fortios_application_list_example.yml
run_example application fortios_application_name_example.yml
run_example application fortios_application_rule_settings_example.yml
run_example authentication fortios_authentication_rule_example.yml
run_example authentication fortios_authentication_scheme_example.yml
run_example authentication fortios_authentication_setting_example.yml
run_example dlp fortios_dlp_filepattern_example.yml
run_example dlp fortios_dlp_fp_doc_source_example.yml
un_example dlp fortios_dlp_fp_sensitivity_example.yml
run_example dlp fortios_dlp_sensor_example.yml
run_example dlp fortios_dlp_settings_example.yml
run_example dnsfilter fortios_dnsfilter_domain_filter_example.yml
run_example dnsfilter fortios_dnsfilter_profile_example.yml
run_example endpoint_control fortios_endpoint_control_client_example.yml
run_example endpoint_control fortios_endpoint_control_forticlient_ems_example.yml
run_example endpoint_control fortios_endpoint_control_forticlient_registration_sync_example.yml
run_example endpoint_control fortios_endpoint_control_profile_example.yml
run_example endpoint_control fortios_endpoint_control_settings_example.yml
run_example extender_controller fortios_extender_controller_extender_example.yml
run_example firewall fortios_firewall_address_example.yml
run_example firewall fortios_firewall_address6_example.yml
run_example firewall fortios_firewall_address6_template_example.yml
run_example firewall fortios_firewall_addrgrp_example.yml
run_example firewall fortios_firewall_addrgrp6_example.yml
run_example firewall fortios_firewall_auth_portal_example.yml
run_example firewall fortios_firewall_central_snat_map_example.yml
run_example firewall fortios_firewall_dnstranslation_example.yml
run_example firewall fortios_firewall_DoS_policy6_example.yml
run_example firewall fortios_firewall_DoS_policy_example.yml
run_example firewall fortios_firewall_identity_based_route_example.yml
run_example firewall fortios_firewall_interface_policy6_example.yml
run_example firewall fortios_firewall_interface_policy_example.yml
run_example firewall fortios_firewall_internet_service_custom_example.yml
run_example firewall fortios_firewall_internet_service_example.yml
run_example firewall fortios_firewall_internet_service_group_example.yml
run_example firewall_ipmacbinding fortios_firewall_ipmacbinding_setting_example.yml
run_example firewall_ipmacbinding fortios_firewall_ipmacbinding_table_example.yml
run_example firewall fortios_firewall_ippool_example.yml
run_example firewall fortios_firewall_ippool6_example.yml
run_example firewall fortios_firewall_ip_translation_example.yml
run_example firewall fortios_firewall_ipv6_eh_filter_example.yml
run_example firewall fortios_firewall_ldb_monitor_example.yml
run_example firewall fortios_firewall_local_in_policy6_example.yml
run_example firewall fortios_firewall_local_in_policy_example.yml
run_example firewall fortios_firewall_multicast_address6_example.yml
run_example firewall fortios_firewall_multicast_address_example.yml
run_example firewall fortios_firewall_multicast_policy6_example.yml
run_example firewall fortios_firewall_multicast_policy_example.yml
run_example firewall fortios_firewall_policy_example.yml
run_example firewall fortios_firewall_policy46_example.yml
run_example firewall fortios_firewall_policy6_example.yml
run_example firewall fortios_firewall_policy64_example.yml
run_example firewall fortios_firewall_profile_group_example.yml
run_example firewall fortios_firewall_profile_protocol_options_example.yml
run_example firewall fortios_firewall_proxy_address_example.yml
run_example firewall fortios_firewall_proxy_addrgrp_example.yml
run_example firewall fortios_firewall_proxy_policy_example.yml
run_example firewall_schedule fortios_firewall_schedule_group_example.yml
run_example firewall_schedule fortios_firewall_schedule_onetime_example.yml
run_example firewall fortios_firewall_vip_example.yml
run_example firewall fortios_firewall_vip46_example.yml
run_example firewall fortios_firewall_vip6_example.yml
run_example firewall fortios_firewall_vip64_example.yml
run_example firewall fortios_firewall_vipgrp_example.yml
run_example firewall fortios_firewall_vipgrp6_example.yml
run_example firewall fortios_firewall_vipgrp46_example.yml
run_example firewall fortios_firewall_vipgrp64_example.yml
run_example icap fortios_icap_profile_example.yml
run_example ips fortios_ips_custom_example.yml
run_example ips fortios_ips_sensor_example.yml
run_example log fortios_log_custom_field_example.yml
run_example log_disk fortios_log_disk_filter_example.yml
run_example log_disk fortios_log_disk_setting_example.yml
run_example log fortios_log_eventfilter_example.yml
run_example log_fortianalyzer2 fortios_log_fortianalyzer2_filter_example.yml
run_example log_fortianalyzer2 fortios_log_fortianalyzer2_setting_example.yml
run_example log_fortiguard fortios_log_fortiguard_filter_example.yml
run_example log fortios_log_gui_display_example.yml
run_example log_memory fortios_log_memory_filter_example.yml
run_example log_memory fortios_log_memory_global_setting_example.yml
run_example ssh_filter fortios_ssh_filter_profile_example.yml
run_example switch_controller fortios_switch_controller_global_example.yml
run_example system fortios_system_accprofile_example.yml
run_example system fortios_system_admin_example.yml
run_example system fortios_system_api_user_example.yml
run_example system fortios_system_central_management_example.yml
run_example system_dhcp fortios_system_dhcp_server_example.yml
run_example system fortios_system_dns_example.yml
run_example system fortios_system_interface_example.yml
run_example system fortios_system_global_example.yml
run_example system fortios_system_sdn_connector_example.yml
run_example report fortios_report_chart_example.yml
run_example report fortios_report_dataset_example.yml
run_example router fortios_router_access_list_example.yml
run_example router fortios_router_ospf_example.yml
run_example user fortios_user_tacacsplus_example.yml
run_example vpn_ipsec fortios_vpn_ipsec_manualkey_example.yml
run_example webfilter fortios_webfilter_content_header_example.yml
run_example webfilter fortios_webfilter_fortiguard_example.yml
run_example webfilter fortios_webfilter_profile_example.yml
run_example webfilter fortios_webfilter_search_engine_example.yml
run_example webfilter fortios_webfilter_urlfilter_example.yml
run_example webfilter fortios_webfilter_ftgd_local_cat_example.yml
run_example webfilter fortios_webfilter_ftgd_local_rating_example.yml
run_example webfilter fortios_webfilter_override_example.yml
run_example webfilter fortios_webfilter_ips_urlfilter_cache_setting_example.yml
run_example webfilter fortios_webfilter_ips_urlfilter_setting_example.yml
run_example webfilter fortios_webfilter_ips_urlfilter_setting6_example.yml
run_example webfilter fortios_webfilter_content_example.yml


# Set proxy inspection mode 
run_example system fortios_system_settings_example.yml

# Run examples that require proxy mode
run_example ftp_proxy fortios_ftp_proxy_explicit_example.yml
run_example spamfilter fortios_spamfilter_profile_example.yml

# Special test cases tested manually
# run_example system fortios_system_vdom_example.yml

ELAPSED_TIME=$(($SECONDS - $START_TIME))
echo -e "\n\n Total time: ${ELAPSED_TIME} s\n\n Results: \n  Success: ${success}  Failed: ${failed}\n\n  Failed test cases: \n ${list_of_failed[@]} \n"
