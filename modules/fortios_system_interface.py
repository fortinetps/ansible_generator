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
module: fortios_system_interface
short_description: Configure interfaces in Fortinet's FortiOS and FortiGate.
description:
    - This module is able to configure a FortiGate or FortiOS by allowing the
      user to set and modify system feature and interface category.
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
    system_interface:
        description:
            - Configure interfaces.
        default: null
        suboptions:
            ac_name:
                description:
                    - PPPoE server name.
            aggregate:
                description:
                    - Aggregate interface.
            algorithm:
                description:
                    - Frame distribution algorithm.
                choices:
                    - L2
                    - L3
                    - L4
            alias:
                description:
                    - Alias will be displayed with the interface name to make it easier to distinguish.
            allowaccess:
                description:
                    - Permitted types of management access to this interface.
                choices:
                    - ping
                    - https
                    - ssh
                    - snmp
                    - http
                    - telnet
                    - fgfm
                    - radius-acct
                    - probe-response
                    - capwap
                    - ftm
            ap_discover:
                description:
                    - Enable/disable automatic registration of unknown FortiAP devices.
                choices:
                    - enable
                    - disable
            arpforward:
                description:
                    - Enable/disable ARP forwarding.
                choices:
                    - enable
                    - disable
            auth_type:
                description:
                    - PPP authentication type to use.
                choices:
                    - auto
                    - pap
                    - chap
                    - mschapv1
                    - mschapv2
            auto_auth_extension_device:
                description:
                    - Enable/disable automatic authorization of dedicated Fortinet extension device on this interface.
                choices:
                    - enable
                    - disable
            bfd:
                description:
                    - Bidirectional Forwarding Detection (BFD) settings.
                choices:
                    - global
                    - enable
                    - disable
            bfd_desired_min_tx:
                description:
                    - BFD desired minimal transmit interval.
            bfd_detect_mult:
                description:
                    - BFD detection multiplier.
            bfd_required_min_rx:
                description:
                    - BFD required minimal receive interval.
            broadcast_forticlient_discovery:
                description:
                    - Enable/disable broadcasting FortiClient discovery messages.
                choices:
                    - enable
                    - disable
            broadcast_forward:
                description:
                    - Enable/disable broadcast forwarding.
                choices:
                    - enable
                    - disable
            captive_portal:
                description:
                    - Enable/disable captive portal.
            cli_conn_status:
                description:
                    - CLI connection status.
            color:
                description:
                    - Color of icon on the GUI.
            dedicated_to:
                description:
                    - Configure interface for single purpose.
                choices:
                    - none
                    - management
            defaultgw:
                description:
                    - Enable to get the gateway IP from the DHCP or PPPoE server.
                choices:
                    - enable
                    - disable
            description:
                description:
                    - Description.
            detected_peer_mtu:
                description:
                    - MTU of detected peer (0 _ 4294967295).
            detectprotocol:
                description:
                    - Protocols used to detect the server.
                choices:
                    - ping
                    - tcp-echo
                    - udp-echo
            detectserver:
                description:
                    - Gateway's ping server for this IP.
            device_access_list:
                description:
                    - Device access list.
            device_identification:
                description:
                    - Enable/disable passively gathering of device identity information about the devices on the network connected to this interface.
                choices:
                    - enable
                    - disable
            device_identification_active_scan:
                description:
                    - Enable/disable active gathering of device identity information about the devices on the network connected to this interface.
                choices:
                    - enable
                    - disable
            device_netscan:
                description:
                    - Enable/disable inclusion of devices detected on this interface in network vulnerability scans.
                choices:
                    - disable
                    - enable
            device_user_identification:
                description:
                    - Enable/disable passive gathering of user identity information about users on this interface.
                choices:
                    - enable
                    - disable
            devindex:
                description:
                    - Device Index.
            dhcp_client_identifier:
                description:
                    - DHCP client identifier.
            dhcp_relay_agent_option:
                description:
                    - Enable/disable DHCP relay agent option.
                choices:
                    - enable
                    - disable
            dhcp_relay_ip:
                description:
                    - DHCP relay IP address.
            dhcp_relay_service:
                description:
                    - Enable/disable allowing this interface to act as a DHCP relay.
                choices:
                    - disable
                    - enable
            dhcp_relay_type:
                description:
                    - DHCP relay type (regular or IPsec).
                choices:
                    - regular
                    - ipsec
            dhcp_renew_time:
                description:
                    - DHCP renew time in seconds (300_604800), 0 means use the renew time provided by the server.
            disc_retry_timeout:
                description:
                    - Time in seconds to wait before retrying to start a PPPoE discovery, 0 means no timeout.
            disconnect_threshold:
                description:
                    - Time in milliseconds to wait before sending a notification that this interface is down or disconnected.
            distance:
                description:
                    - Distance for routes learned through PPPoE or DHCP, lower distance indicates preferred route.
            dns_server_override:
                description:
                    - Enable/disable use DNS acquired by DHCP or PPPoE.
                choices:
                    - enable
                    - disable
            drop_fragment:
                description:
                    - Enable/disable drop fragment packets.
                choices:
                    - enable
                    - disable
            drop_overlapped_fragment:
                description:
                    - Enable/disable drop overlapped fragment packets.
                choices:
                    - enable
                    - disable
            egress_shaping_profile:
                description:
                    - Outgoing traffic shaping profile.
            endpoint_compliance:
                description:
                    - Enable/disable endpoint compliance enforcement.
                choices:
                    - enable
                    - disable
            estimated_downstream_bandwidth:
                description:
                    - Estimated maximum downstream bandwidth (kbps). Used to estimate link utilization.
            estimated_upstream_bandwidth:
                description:
                    - Estimated maximum upstream bandwidth (kbps). Used to estimate link utilization.
            explicit_ftp_proxy:
                description:
                    - Enable/disable the explicit FTP proxy on this interface.
                choices:
                    - enable
                    - disable
            explicit_web_proxy:
                description:
                    - Enable/disable the explicit web proxy on this interface.
                choices:
                    - enable
                    - disable
            external:
                description:
                    - Enable/disable identifying the interface as an external interface (which usually means it's connected to the Internet).
                choices:
                    - enable
                    - disable
            fail_action_on_extender:
                description:
                    - Action on extender when interface fail .
                choices:
                    - soft-restart
                    - hard-restart
                    - reboot
            fail_alert_interfaces:
                description:
                    - Names of the FortiGate interfaces from which the link failure alert is sent for this interface.
                suboptions:
                    name:
                        description:
                            - Names of the physical interfaces belonging to the aggregate or redundant interface. Source system.interface.name.
                        required: true
            fail_alert_method:
                description:
                    - Select link_failed_signal or link_down method to alert about a failed link.
                choices:
                    - link-failed-signal
                    - link-down
            fail_detect:
                description:
                    - Enable/disable fail detection features for this interface.
                choices:
                    - enable
                    - disable
            fail_detect_option:
                description:
                    - Options for detecting that this interface has failed.
                choices:
                    - detectserver
                    - link-down
            fortiheartbeat:
                description:
                    - Enable/disable FortiHeartBeat (FortiTelemetry on GUI).
                choices:
                    - enable
                    - disable
            fortilink:
                description:
                    - Enable FortiLink to dedicate this interface to manage other Fortinet devices.
                choices:
                    - enable
                    - disable
            fortilink_backup_link:
                description:
                    - fortilink split interface backup link.
            fortilink_split_interface:
                description:
                    - Enable/disable FortiLink split interface to connect member link to different FortiSwitch in stack for uplink redundancy (maximum 2
                       interfaces in the "members" command).
                choices:
                    - enable
                    - disable
            fortilink_stacking:
                description:
                    - Enable/disable FortiLink switch_stacking on this interface.
                choices:
                    - enable
                    - disable
            forward_domain:
                description:
                    - Transparent mode forward domain.
            gwdetect:
                description:
                    - Enable/disable detect gateway alive for first.
                choices:
                    - enable
                    - disable
            ha_priority:
                description:
                    - HA election priority for the PING server.
            icmp_accept_redirect:
                description:
                    - Enable/disable ICMP accept redirect.
                choices:
                    - enable
                    - disable
            icmp_send_redirect:
                description:
                    - Enable/disable ICMP send redirect.
                choices:
                    - enable
                    - disable
            ident_accept:
                description:
                    - Enable/disable authentication for this interface.
                choices:
                    - enable
                    - disable
            idle_timeout:
                description:
                    - PPPoE auto disconnect after idle timeout seconds, 0 means no timeout.
            inbandwidth:
                description:
                    - Bandwidth limit for incoming traffic (0 _ 16776000 kbps), 0 means unlimited.
            ingress_spillover_threshold:
                description:
                    - Ingress Spillover threshold (0 _ 16776000 kbps).
            interface:
                description:
                    - Interface name. Source system.interface.name.
            internal:
                description:
                    - Implicitly created.
            ip:
                description:
                    - "Interface IPv4 address and subnet mask, syntax: X.X.X.X/24."
            ipmac:
                description:
                    - Enable/disable IP/MAC binding.
                choices:
                    - enable
                    - disable
            ips_sniffer_mode:
                description:
                    - Enable/disable the use of this interface as a one_armed sniffer.
                choices:
                    - enable
                    - disable
            ipunnumbered:
                description:
                    - Unnumbered IP used for PPPoE interfaces for which no unique local address is provided.
            ipv6:
                description:
                    - IPv6 of interface.
                suboptions:
                    autoconf:
                        description:
                            - Enable/disable address auto config.
                        choices:
                            - enable
                            - disable
                    dhcp6_client_options:
                        description:
                            - DHCPv6 client options.
                        choices:
                            - rapid
                            - iapd
                            - iana
                    dhcp6_information_request:
                        description:
                            - Enable/disable DHCPv6 information request.
                        choices:
                            - enable
                            - disable
                    dhcp6_prefix_delegation:
                        description:
                            - Enable/disable DHCPv6 prefix delegation.
                        choices:
                            - enable
                            - disable
                    dhcp6_prefix_hint:
                        description:
                            - DHCPv6 prefix that will be used as a hint to the upstream DHCPv6 server.
                    dhcp6_prefix_hint_plt:
                        description:
                            - DHCPv6 prefix hint preferred life time (sec), 0 means unlimited lease time.
                    dhcp6_prefix_hint_vlt:
                        description:
                            - DHCPv6 prefix hint valid life time (sec).
                    dhcp6_relay_ip:
                        description:
                            - DHCPv6 relay IP address.
                    dhcp6_relay_service:
                        description:
                            - Enable/disable DHCPv6 relay.
                        choices:
                            - disable
                            - enable
                    dhcp6_relay_type:
                        description:
                            - DHCPv6 relay type.
                        choices:
                            - regular
                    ip6_address:
                        description:
                            - "Primary IPv6 address prefix, syntax: xxxx:xxxx:xxxx:xxxx:xxxx:xxxx:xxxx:xxxx/xxx"
                    ip6_allowaccess:
                        description:
                            - Allow management access to the interface.
                        choices:
                            - ping
                            - https
                            - ssh
                            - snmp
                            - http
                            - telnet
                            - fgfm
                            - capwap
                    ip6_default_life:
                        description:
                            - Default life (sec).
                    ip6_delegated_prefix_list:
                        description:
                            - Advertised IPv6 delegated prefix list.
                        suboptions:
                            autonomous_flag:
                                description:
                                    - Enable/disable the autonomous flag.
                                choices:
                                    - enable
                                    - disable
                            onlink_flag:
                                description:
                                    - Enable/disable the onlink flag.
                                choices:
                                    - enable
                                    - disable
                            prefix_id:
                                description:
                                    - Prefix ID.
                            rdnss:
                                description:
                                    - Recursive DNS server option.
                            rdnss_service:
                                description:
                                    - Recursive DNS service option.
                                choices:
                                    - delegated
                                    - default
                                    - specify
                            subnet:
                                description:
                                    -  Add subnet ID to routing prefix.
                            upstream_interface:
                                description:
                                    - Name of the interface that provides delegated information. Source system.interface.name.
                    ip6_dns_server_override:
                        description:
                            - Enable/disable using the DNS server acquired by DHCP.
                        choices:
                            - enable
                            - disable
                    ip6_extra_addr:
                        description:
                            - Extra IPv6 address prefixes of interface.
                        suboptions:
                            prefix:
                                description:
                                    - IPv6 address prefix.
                                required: true
                    ip6_hop_limit:
                        description:
                            - Hop limit (0 means unspecified).
                    ip6_link_mtu:
                        description:
                            - IPv6 link MTU.
                    ip6_manage_flag:
                        description:
                            - Enable/disable the managed flag.
                        choices:
                            - enable
                            - disable
                    ip6_max_interval:
                        description:
                            - IPv6 maximum interval (4 to 1800 sec).
                    ip6_min_interval:
                        description:
                            - IPv6 minimum interval (3 to 1350 sec).
                    ip6_mode:
                        description:
                            - Addressing mode (static, DHCP, delegated).
                        choices:
                            - static
                            - dhcp
                            - pppoe
                            - delegated
                    ip6_other_flag:
                        description:
                            - Enable/disable the other IPv6 flag.
                        choices:
                            - enable
                            - disable
                    ip6_prefix_list:
                        description:
                            - Advertised prefix list.
                        suboptions:
                            autonomous_flag:
                                description:
                                    - Enable/disable the autonomous flag.
                                choices:
                                    - enable
                                    - disable
                            dnssl:
                                description:
                                    - DNS search list option.
                                suboptions:
                                    domain:
                                        description:
                                            - Domain name.
                                        required: true
                            onlink_flag:
                                description:
                                    - Enable/disable the onlink flag.
                                choices:
                                    - enable
                                    - disable
                            preferred_life_time:
                                description:
                                    - Preferred life time (sec).
                            prefix:
                                description:
                                    - IPv6 prefix.
                                required: true
                            rdnss:
                                description:
                                    - Recursive DNS server option.
                            valid_life_time:
                                description:
                                    - Valid life time (sec).
                    ip6_reachable_time:
                        description:
                            - IPv6 reachable time (milliseconds; 0 means unspecified).
                    ip6_retrans_time:
                        description:
                            - IPv6 retransmit time (milliseconds; 0 means unspecified).
                    ip6_send_adv:
                        description:
                            - Enable/disable sending advertisements about the interface.
                        choices:
                            - enable
                            - disable
                    ip6_subnet:
                        description:
                            - " Subnet to routing prefix, syntax: xxxx:xxxx:xxxx:xxxx:xxxx:xxxx:xxxx:xxxx/xxx"
                    ip6_upstream_interface:
                        description:
                            - Interface name providing delegated information. Source system.interface.name.
                    nd_cert:
                        description:
                            - Neighbor discovery certificate. Source certificate.local.name.
                    nd_cga_modifier:
                        description:
                            - Neighbor discovery CGA modifier.
                    nd_mode:
                        description:
                            - Neighbor discovery mode.
                        choices:
                            - basic
                            - SEND-compatible
                    nd_security_level:
                        description:
                            - Neighbor discovery security level (0 _ 7; 0 = least secure, default = 0).
                    nd_timestamp_delta:
                        description:
                            - Neighbor discovery timestamp delta value (1 _ 3600 sec; default = 300).
                    nd_timestamp_fuzz:
                        description:
                            - Neighbor discovery timestamp fuzz factor (1 _ 60 sec; default = 1).
                    vrip6_link_local:
                        description:
                            - Link_local IPv6 address of virtual router.
                    vrrp_virtual_mac6:
                        description:
                            - Enable/disable virtual MAC for VRRP.
                        choices:
                            - enable
                            - disable
                    vrrp6:
                        description:
                            - IPv6 VRRP configuration.
                        suboptions:
                            accept_mode:
                                description:
                                    - Enable/disable accept mode.
                                choices:
                                    - enable
                                    - disable
                            adv_interval:
                                description:
                                    - Advertisement interval (1 _ 255 seconds).
                            preempt:
                                description:
                                    - Enable/disable preempt mode.
                                choices:
                                    - enable
                                    - disable
                            priority:
                                description:
                                    - Priority of the virtual router (1 _ 255).
                            start_time:
                                description:
                                    - Startup time (1 _ 255 seconds).
                            status:
                                description:
                                    - Enable/disable VRRP.
                                choices:
                                    - enable
                                    - disable
                            vrdst6:
                                description:
                                    - Monitor the route to this destination.
                            vrgrp:
                                description:
                                    - VRRP group ID (1 _ 65535).
                            vrid:
                                description:
                                    - Virtual router identifier (1 _ 255).
                                required: true
                            vrip6:
                                description:
                                    - IPv6 address of the virtual router.
            l2forward:
                description:
                    - Enable/disable l2 forwarding.
                choices:
                    - enable
                    - disable
            lacp_ha_slave:
                description:
                    - LACP HA slave.
                choices:
                    - enable
                    - disable
            lacp_mode:
                description:
                    - LACP mode.
                choices:
                    - static
                    - passive
                    - active
            lacp_speed:
                description:
                    - How often the interface sends LACP messages.
                choices:
                    - slow
                    - fast
            lcp_echo_interval:
                description:
                    - Time in seconds between PPPoE Link Control Protocol (LCP) echo requests.
            lcp_max_echo_fails:
                description:
                    - Maximum missed LCP echo messages before disconnect.
            link_up_delay:
                description:
                    - Number of milliseconds to wait before considering a link is up.
            lldp_transmission:
                description:
                    - Enable/disable Link Layer Discovery Protocol (LLDP) transmission.
                choices:
                    - enable
                    - disable
                    - vdom
            macaddr:
                description:
                    - Change the interface's MAC address.
            managed_device:
                description:
                    - Available when FortiLink is enabled, used for managed devices through FortiLink interface.
                suboptions:
                    name:
                        description:
                            - Managed dev identifier.
                        required: true
            management_ip:
                description:
                    - High Availability in_band management IP address of this interface.
            member:
                description:
                    - Physical interfaces that belong to the aggregate or redundant interface.
                suboptions:
                    interface_name:
                        description:
                            - Physical interface name. Source system.interface.name.
            min_links:
                description:
                    - Minimum number of aggregated ports that must be up.
            min_links_down:
                description:
                    - Action to take when less than the configured minimum number of links are active.
                choices:
                    - operational
                    - administrative
            mode:
                description:
                    - Addressing mode (static, DHCP, PPPoE).
                choices:
                    - static
                    - dhcp
                    - pppoe
            mtu:
                description:
                    - MTU value for this interface.
            mtu_override:
                description:
                    - Enable to set a custom MTU for this interface.
                choices:
                    - enable
                    - disable
            name:
                description:
                    - Name.
                required: true
            ndiscforward:
                description:
                    - Enable/disable NDISC forwarding.
                choices:
                    - enable
                    - disable
            netbios_forward:
                description:
                    - Enable/disable NETBIOS forwarding.
                choices:
                    - disable
                    - enable
            netflow_sampler:
                description:
                    - Enable/disable NetFlow on this interface and set the data that NetFlow collects (rx, tx, or both).
                choices:
                    - disable
                    - tx
                    - rx
                    - both
            outbandwidth:
                description:
                    - Bandwidth limit for outgoing traffic (0 _ 16776000 kbps).
            padt_retry_timeout:
                description:
                    - PPPoE Active Discovery Terminate (PADT) used to terminate sessions after an idle time.
            password:
                description:
                    - PPPoE account's password.
            ping_serv_status:
                description:
                    - PING server status.
            polling_interval:
                description:
                    - sFlow polling interval (1 _ 255 sec).
            pppoe_unnumbered_negotiate:
                description:
                    - Enable/disable PPPoE unnumbered negotiation.
                choices:
                    - enable
                    - disable
            pptp_auth_type:
                description:
                    - PPTP authentication type.
                choices:
                    - auto
                    - pap
                    - chap
                    - mschapv1
                    - mschapv2
            pptp_client:
                description:
                    - Enable/disable PPTP client.
                choices:
                    - enable
                    - disable
            pptp_password:
                description:
                    - PPTP password.
            pptp_server_ip:
                description:
                    - PPTP server IP address.
            pptp_timeout:
                description:
                    - Idle timer in minutes (0 for disabled).
            pptp_user:
                description:
                    - PPTP user name.
            preserve_session_route:
                description:
                    - Enable/disable preservation of session route when dirty.
                choices:
                    - enable
                    - disable
            priority:
                description:
                    - Priority of learned routes.
            priority_override:
                description:
                    - Enable/disable fail back to higher priority port once recovered.
                choices:
                    - enable
                    - disable
            proxy_captive_portal:
                description:
                    - Enable/disable proxy captive portal on this interface.
                choices:
                    - enable
                    - disable
            redundant_interface:
                description:
                    - Redundant interface.
            remote_ip:
                description:
                    - Remote IP address of tunnel.
            replacemsg_override_group:
                description:
                    - Replacement message override group.
            role:
                description:
                    - Interface role.
                choices:
                    - lan
                    - wan
                    - dmz
                    - undefined
            sample_direction:
                description:
                    - Data that NetFlow collects (rx, tx, or both).
                choices:
                    - tx
                    - rx
                    - both
            sample_rate:
                description:
                    - sFlow sample rate (10 _ 99999).
            scan_botnet_connections:
                description:
                    - Enable monitoring or blocking connections to Botnet servers through this interface.
                choices:
                    - disable
                    - block
                    - monitor
            secondary_IP:
                description:
                    - Enable/disable adding a secondary IP to this interface.
                choices:
                    - enable
                    - disable
            secondaryip:
                description:
                    - Second IP address of interface.
                suboptions:
                    allowaccess:
                        description:
                            - Management access settings for the secondary IP address.
                        choices:
                            - ping
                            - https
                            - ssh
                            - snmp
                            - http
                            - telnet
                            - fgfm
                            - radius-acct
                            - probe-response
                            - capwap
                            - ftm
                    detectprotocol:
                        description:
                            - Protocols used to detect the server.
                        choices:
                            - ping
                            - tcp-echo
                            - udp-echo
                    detectserver:
                        description:
                            - Gateway's ping server for this IP.
                    gwdetect:
                        description:
                            - Enable/disable detect gateway alive for first.
                        choices:
                            - enable
                            - disable
                    ha_priority:
                        description:
                            - HA election priority for the PING server.
                    id:
                        description:
                            - ID.
                        required: true
                    ip:
                        description:
                            - Secondary IP address of the interface.
                    ping_serv_status:
                        description:
                            - PING server status.
            security_exempt_list:
                description:
                    - Name of security_exempt_list.
            security_external_logout:
                description:
                    - URL of external authentication logout server.
            security_external_web:
                description:
                    - URL of external authentication web server.
            security_groups:
                description:
                    - User groups that can authenticate with the captive portal.
                suboptions:
                    name:
                        description:
                            - Names of user groups that can authenticate with the captive portal.
                        required: true
            security_mac_auth_bypass:
                description:
                    - Enable/disable MAC authentication bypass.
                choices:
                    - enable
                    - disable
            security_mode:
                description:
                    - Turn on captive portal authentication for this interface.
                choices:
                    - none
                    - captive-portal
                    - 802.1X
            security_redirect_url:
                description:
                    - URL redirection after disclaimer/authentication.
            service_name:
                description:
                    - PPPoE service name.
            sflow_sampler:
                description:
                    - Enable/disable sFlow on this interface.
                choices:
                    - enable
                    - disable
            snmp_index:
                description:
                    - Permanent SNMP Index of the interface.
            speed:
                description:
                    - Interface speed. The default setting and the options available depend on the interface hardware.
                choices:
                    - auto
                    - 10full
                    - 10half
                    - 100full
                    - 100half
                    - 1000full
                    - 1000half
                    - 1000auto
            spillover_threshold:
                description:
                    - Egress Spillover threshold (0 _ 16776000 kbps), 0 means unlimited.
            src_check:
                description:
                    - Enable/disable source IP check.
                choices:
                    - enable
                    - disable
            status:
                description:
                    - Bring the interface up or shut the interface down.
                choices:
                    - up
                    - down
            stpforward:
                description:
                    - Enable/disable STP forwarding.
                choices:
                    - enable
                    - disable
            stpforward_mode:
                description:
                    - Configure STP forwarding mode.
                choices:
                    - rpl-all-ext-id
                    - rpl-bridge-ext-id
                    - rpl-nothing
            subst:
                description:
                    - Enable to always send packets from this interface to a destination MAC address.
                choices:
                    - enable
                    - disable
            substitute_dst_mac:
                description:
                    - Destination MAC address that all packets are sent to from this interface.
            switch:
                description:
                    - Contained in switch.
            switch_controller_access_vlan:
                description:
                    - Block FortiSwitch port_to_port traffic.
                choices:
                    - enable
                    - disable
            switch_controller_arp_inspection:
                description:
                    - Enable/disable FortiSwitch ARP inspection.
                choices:
                    - enable
                    - disable
            switch_controller_dhcp_snooping:
                description:
                    - Switch controller DHCP snooping.
                choices:
                    - enable
                    - disable
            switch_controller_dhcp_snooping_option82:
                description:
                    - Switch controller DHCP snooping option82.
                choices:
                    - enable
                    - disable
            switch_controller_dhcp_snooping_verify_mac:
                description:
                    - Switch controller DHCP snooping verify MAC.
                choices:
                    - enable
                    - disable
            switch_controller_igmp_snooping:
                description:
                    - Switch controller IGMP snooping.
                choices:
                    - enable
                    - disable
            switch_controller_learning_limit:
                description:
                    - Limit the number of dynamic MAC addresses on this VLAN (1 _ 128, 0 = no limit, default).
            tagging:
                description:
                    - Config object tagging.
                suboptions:
                    category:
                        description:
                            - Tag category. Source system.object-tagging.category.
                    name:
                        description:
                            - Tagging entry name.
                        required: true
                    tags:
                        description:
                            - Tags.
                        suboptions:
                            name:
                                description:
                                    - Tag name. Source system.object-tagging.tags.name.
                                required: true
            tcp_mss:
                description:
                    - TCP maximum segment size. 0 means do not change segment size.
            trust_ip_1:
                description:
                    - Trusted host for dedicated management traffic (0.0.0.0/24 for all hosts).
            trust_ip_2:
                description:
                    - Trusted host for dedicated management traffic (0.0.0.0/24 for all hosts).
            trust_ip_3:
                description:
                    - Trusted host for dedicated management traffic (0.0.0.0/24 for all hosts).
            trust_ip6_1:
                description:
                    - "Trusted IPv6 host for dedicated management traffic (::/0 for all hosts)."
            trust_ip6_2:
                description:
                    - "Trusted IPv6 host for dedicated management traffic (::/0 for all hosts)."
            trust_ip6_3:
                description:
                    - "Trusted IPv6 host for dedicated management traffic (::/0 for all hosts)."
            type:
                description:
                    - Interface type.
                choices:
                    - physical
                    - vlan
                    - aggregate
                    - redundant
                    - tunnel
                    - vdom-link
                    - loopback
                    - switch
                    - hard-switch
                    - vap-switch
                    - wl-mesh
                    - fext-wan
                    - vxlan
                    - hdlc
                    - switch-vlan
            username:
                description:
                    - Username of the PPPoE account, provided by your ISP.
            vdom:
                description:
                    - Interface is in this virtual domain (VDOM). Source system.vdom.name.
            vindex:
                description:
                    - Switch control interface VLAN ID.
            vlanforward:
                description:
                    - Enable/disable traffic forwarding between VLANs on this interface.
                choices:
                    - enable
                    - disable
            vlanid:
                description:
                    - VLAN ID (1 _ 4094).
            vrf:
                description:
                    - Virtual Routing Forwarding ID.
            vrrp:
                description:
                    - VRRP configuration.
                suboptions:
                    accept_mode:
                        description:
                            - Enable/disable accept mode.
                        choices:
                            - enable
                            - disable
                    adv_interval:
                        description:
                            - Advertisement interval (1 _ 255 seconds).
                    preempt:
                        description:
                            - Enable/disable preempt mode.
                        choices:
                            - enable
                            - disable
                    priority:
                        description:
                            - Priority of the virtual router (1 _ 255).
                    proxy_arp:
                        description:
                            - VRRP Proxy ARP configuration.
                        suboptions:
                            id:
                                description:
                                    - ID.
                                required: true
                            ip:
                                description:
                                    - Set IP addresses of proxy ARP.
                    start_time:
                        description:
                            - Startup time (1 _ 255 seconds).
                    status:
                        description:
                            - Enable/disable this VRRP configuration.
                        choices:
                            - enable
                            - disable
                    version:
                        description:
                            - VRRP version.
                        choices:
                            - 2
                            - 3
                    vrdst:
                        description:
                            - Monitor the route to this destination.
                    vrdst_priority:
                        description:
                            - Priority of the virtual router when the virtual router destination becomes unreachable (0 _ 254).
                    vrgrp:
                        description:
                            - VRRP group ID (1 _ 65535).
                    vrid:
                        description:
                            - Virtual router identifier (1 _ 255).
                        required: true
                    vrip:
                        description:
                            - IP address of the virtual router.
            vrrp_virtual_mac:
                description:
                    - Enable/disable use of virtual MAC for VRRP.
                choices:
                    - enable
                    - disable
            wccp:
                description:
                    - Enable/disable WCCP on this interface. Used for encapsulated WCCP communication between WCCP clients and servers.
                choices:
                    - enable
                    - disable
            weight:
                description:
                    - Default weight for static routes (if route has no weight configured).
            wins_ip:
                description:
                    - WINS server IP.
'''

EXAMPLES = '''
- hosts: localhost
  vars:
   host: "192.168.122.40"
   username: "admin"
   password: ""
   vdom: "root"
  tasks:
  - name: Configure interfaces.
    fortios_system_interface:
      host:  "{{ host }}"
      username: "{{ username }}"
      password: "{{ password }}"
      vdom:  "{{ vdom }}"
      https: "False"
      state: "present"
      system_interface:
        ac_name: "<your_own_value>"
        aggregate: "<your_own_value>"
        algorithm: "L2"
        alias: "<your_own_value>"
        allowaccess: "ping"
        ap_discover: "enable"
        arpforward: "enable"
        auth_type: "auto"
        auto_auth_extension_device: "enable"
        bfd: "global"
        bfd_desired_min_tx: "13"
        bfd_detect_mult: "14"
        bfd_required_min_rx: "15"
        broadcast_forticlient_discovery: "enable"
        broadcast_forward: "enable"
        captive_portal: "18"
        cli_conn_status: "19"
        color: "20"
        dedicated_to: "none"
        defaultgw: "enable"
        description: "<your_own_value>"
        detected_peer_mtu: "24"
        detectprotocol: "ping"
        detectserver: "<your_own_value>"
        device_access_list: "<your_own_value>"
        device_identification: "enable"
        device_identification_active_scan: "enable"
        device_netscan: "disable"
        device_user_identification: "enable"
        devindex: "32"
        dhcp_client_identifier:  "myId_33"
        dhcp_relay_agent_option: "enable"
        dhcp_relay_ip: "<your_own_value>"
        dhcp_relay_service: "disable"
        dhcp_relay_type: "regular"
        dhcp_renew_time: "38"
        disc_retry_timeout: "39"
        disconnect_threshold: "40"
        distance: "41"
        dns_server_override: "enable"
        drop_fragment: "enable"
        drop_overlapped_fragment: "enable"
        egress_shaping_profile: "<your_own_value>"
        endpoint_compliance: "enable"
        estimated_downstream_bandwidth: "47"
        estimated_upstream_bandwidth: "48"
        explicit_ftp_proxy: "enable"
        explicit_web_proxy: "enable"
        external: "enable"
        fail_action_on_extender: "soft-restart"
        fail_alert_interfaces:
         -
            name: "default_name_54 (source system.interface.name)"
        fail_alert_method: "link-failed-signal"
        fail_detect: "enable"
        fail_detect_option: "detectserver"
        fortiheartbeat: "enable"
        fortilink: "enable"
        fortilink_backup_link: "60"
        fortilink_split_interface: "enable"
        fortilink_stacking: "enable"
        forward_domain: "63"
        gwdetect: "enable"
        ha_priority: "65"
        icmp_accept_redirect: "enable"
        icmp_send_redirect: "enable"
        ident_accept: "enable"
        idle_timeout: "69"
        inbandwidth: "70"
        ingress_spillover_threshold: "71"
        interface: "<your_own_value> (source system.interface.name)"
        internal: "73"
        ip: "<your_own_value>"
        ipmac: "enable"
        ips_sniffer_mode: "enable"
        ipunnumbered: "<your_own_value>"
        ipv6:
            autoconf: "enable"
            dhcp6_client_options: "rapid"
            dhcp6_information_request: "enable"
            dhcp6_prefix_delegation: "enable"
            dhcp6_prefix_hint: "<your_own_value>"
            dhcp6_prefix_hint_plt: "84"
            dhcp6_prefix_hint_vlt: "85"
            dhcp6_relay_ip: "<your_own_value>"
            dhcp6_relay_service: "disable"
            dhcp6_relay_type: "regular"
            ip6_address: "<your_own_value>"
            ip6_allowaccess: "ping"
            ip6_default_life: "91"
            ip6_delegated_prefix_list:
             -
                autonomous_flag: "enable"
                onlink_flag: "enable"
                prefix_id: "95"
                rdnss: "<your_own_value>"
                rdnss_service: "delegated"
                subnet: "<your_own_value>"
                upstream_interface: "<your_own_value> (source system.interface.name)"
            ip6_dns_server_override: "enable"
            ip6_extra_addr:
             -
                prefix: "<your_own_value>"
            ip6_hop_limit: "103"
            ip6_link_mtu: "104"
            ip6_manage_flag: "enable"
            ip6_max_interval: "106"
            ip6_min_interval: "107"
            ip6_mode: "static"
            ip6_other_flag: "enable"
            ip6_prefix_list:
             -
                autonomous_flag: "enable"
                dnssl:
                 -
                    domain: "<your_own_value>"
                onlink_flag: "enable"
                preferred_life_time: "115"
                prefix: "<your_own_value>"
                rdnss: "<your_own_value>"
                valid_life_time: "118"
            ip6_reachable_time: "119"
            ip6_retrans_time: "120"
            ip6_send_adv: "enable"
            ip6_subnet: "<your_own_value>"
            ip6_upstream_interface: "<your_own_value> (source system.interface.name)"
            nd_cert: "<your_own_value> (source certificate.local.name)"
            nd_cga_modifier: "<your_own_value>"
            nd_mode: "basic"
            nd_security_level: "127"
            nd_timestamp_delta: "128"
            nd_timestamp_fuzz: "129"
            vrip6_link_local: "<your_own_value>"
            vrrp_virtual_mac6: "enable"
            vrrp6:
             -
                accept_mode: "enable"
                adv_interval: "134"
                preempt: "enable"
                priority: "136"
                start_time: "137"
                status: "enable"
                vrdst6: "<your_own_value>"
                vrgrp: "140"
                vrid: "141"
                vrip6: "<your_own_value>"
        l2forward: "enable"
        lacp_ha_slave: "enable"
        lacp_mode: "static"
        lacp_speed: "slow"
        lcp_echo_interval: "147"
        lcp_max_echo_fails: "148"
        link_up_delay: "149"
        lldp_transmission: "enable"
        macaddr: "<your_own_value>"
        managed_device:
         -
            name: "default_name_153"
        management_ip: "<your_own_value>"
        member:
         -
            interface_name: "<your_own_value> (source system.interface.name)"
        min_links: "157"
        min_links_down: "operational"
        mode: "static"
        mtu: "160"
        mtu_override: "enable"
        name: "default_name_162"
        ndiscforward: "enable"
        netbios_forward: "disable"
        netflow_sampler: "disable"
        outbandwidth: "166"
        padt_retry_timeout: "167"
        password: "<your_own_value>"
        ping_serv_status: "169"
        polling_interval: "170"
        pppoe_unnumbered_negotiate: "enable"
        pptp_auth_type: "auto"
        pptp_client: "enable"
        pptp_password: "<your_own_value>"
        pptp_server_ip: "<your_own_value>"
        pptp_timeout: "176"
        pptp_user: "<your_own_value>"
        preserve_session_route: "enable"
        priority: "179"
        priority_override: "enable"
        proxy_captive_portal: "enable"
        redundant_interface: "<your_own_value>"
        remote_ip: "<your_own_value>"
        replacemsg_override_group: "<your_own_value>"
        role: "lan"
        sample_direction: "tx"
        sample_rate: "187"
        scan_botnet_connections: "disable"
        secondary_IP: "enable"
        secondaryip:
         -
            allowaccess: "ping"
            detectprotocol: "ping"
            detectserver: "<your_own_value>"
            gwdetect: "enable"
            ha_priority: "195"
            id:  "196"
            ip: "<your_own_value>"
            ping_serv_status: "198"
        security_exempt_list: "<your_own_value>"
        security_external_logout: "<your_own_value>"
        security_external_web: "<your_own_value>"
        security_groups:
         -
            name: "default_name_203"
        security_mac_auth_bypass: "enable"
        security_mode: "none"
        security_redirect_url: "<your_own_value>"
        service_name: "<your_own_value>"
        sflow_sampler: "enable"
        snmp_index: "209"
        speed: "auto"
        spillover_threshold: "211"
        src_check: "enable"
        status: "up"
        stpforward: "enable"
        stpforward_mode: "rpl-all-ext-id"
        subst: "enable"
        substitute_dst_mac: "<your_own_value>"
        switch: "<your_own_value>"
        switch_controller_access_vlan: "enable"
        switch_controller_arp_inspection: "enable"
        switch_controller_dhcp_snooping: "enable"
        switch_controller_dhcp_snooping_option82: "enable"
        switch_controller_dhcp_snooping_verify_mac: "enable"
        switch_controller_igmp_snooping: "enable"
        switch_controller_learning_limit: "225"
        tagging:
         -
            category: "<your_own_value> (source system.object-tagging.category)"
            name: "default_name_228"
            tags:
             -
                name: "default_name_230 (source system.object-tagging.tags.name)"
        tcp_mss: "231"
        trust_ip_1: "<your_own_value>"
        trust_ip_2: "<your_own_value>"
        trust_ip_3: "<your_own_value>"
        trust_ip6_1: "<your_own_value>"
        trust_ip6_2: "<your_own_value>"
        trust_ip6_3: "<your_own_value>"
        type: "physical"
        username: "<your_own_value>"
        vdom: "<your_own_value> (source system.vdom.name)"
        vindex: "241"
        vlanforward: "enable"
        vlanid: "243"
        vrf: "244"
        vrrp:
         -
            accept_mode: "enable"
            adv_interval: "247"
            preempt: "enable"
            priority: "249"
            proxy_arp:
             -
                id:  "251"
                ip: "<your_own_value>"
            start_time: "253"
            status: "enable"
            version: "2"
            vrdst: "<your_own_value>"
            vrdst_priority: "257"
            vrgrp: "258"
            vrid: "259"
            vrip: "<your_own_value>"
        vrrp_virtual_mac: "enable"
        wccp: "enable"
        weight: "263"
        wins_ip: "<your_own_value>"
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


def filter_system_interface_data(json):
    option_list = ['ac_name', 'aggregate', 'algorithm',
                   'alias', 'allowaccess', 'ap_discover',
                   'arpforward', 'auth_type', 'auto_auth_extension_device',
                   'bfd', 'bfd_desired_min_tx', 'bfd_detect_mult',
                   'bfd_required_min_rx', 'broadcast_forticlient_discovery', 'broadcast_forward',
                   'captive_portal', 'cli_conn_status', 'color',
                   'dedicated_to', 'defaultgw', 'description',
                   'detected_peer_mtu', 'detectprotocol', 'detectserver',
                   'device_access_list', 'device_identification', 'device_identification_active_scan',
                   'device_netscan', 'device_user_identification', 'devindex',
                   'dhcp_client_identifier', 'dhcp_relay_agent_option', 'dhcp_relay_ip',
                   'dhcp_relay_service', 'dhcp_relay_type', 'dhcp_renew_time',
                   'disc_retry_timeout', 'disconnect_threshold', 'distance',
                   'dns_server_override', 'drop_fragment', 'drop_overlapped_fragment',
                   'egress_shaping_profile', 'endpoint_compliance', 'estimated_downstream_bandwidth',
                   'estimated_upstream_bandwidth', 'explicit_ftp_proxy', 'explicit_web_proxy',
                   'external', 'fail_action_on_extender', 'fail_alert_interfaces',
                   'fail_alert_method', 'fail_detect', 'fail_detect_option',
                   'fortiheartbeat', 'fortilink', 'fortilink_backup_link',
                   'fortilink_split_interface', 'fortilink_stacking', 'forward_domain',
                   'gwdetect', 'ha_priority', 'icmp_accept_redirect',
                   'icmp_send_redirect', 'ident_accept', 'idle_timeout',
                   'inbandwidth', 'ingress_spillover_threshold', 'interface',
                   'internal', 'ip', 'ipmac',
                   'ips_sniffer_mode', 'ipunnumbered', 'ipv6',
                   'l2forward', 'lacp_ha_slave', 'lacp_mode',
                   'lacp_speed', 'lcp_echo_interval', 'lcp_max_echo_fails',
                   'link_up_delay', 'lldp_transmission', 'macaddr',
                   'managed_device', 'management_ip', 'member',
                   'min_links', 'min_links_down', 'mode',
                   'mtu', 'mtu_override', 'name',
                   'ndiscforward', 'netbios_forward', 'netflow_sampler',
                   'outbandwidth', 'padt_retry_timeout', 'password',
                   'ping_serv_status', 'polling_interval', 'pppoe_unnumbered_negotiate',
                   'pptp_auth_type', 'pptp_client', 'pptp_password',
                   'pptp_server_ip', 'pptp_timeout', 'pptp_user',
                   'preserve_session_route', 'priority', 'priority_override',
                   'proxy_captive_portal', 'redundant_interface', 'remote_ip',
                   'replacemsg_override_group', 'role', 'sample_direction',
                   'sample_rate', 'scan_botnet_connections', 'secondary_IP',
                   'secondaryip', 'security_exempt_list', 'security_external_logout',
                   'security_external_web', 'security_groups', 'security_mac_auth_bypass',
                   'security_mode', 'security_redirect_url', 'service_name',
                   'sflow_sampler', 'snmp_index', 'speed',
                   'spillover_threshold', 'src_check', 'status',
                   'stpforward', 'stpforward_mode', 'subst',
                   'substitute_dst_mac', 'switch', 'switch_controller_access_vlan',
                   'switch_controller_arp_inspection', 'switch_controller_dhcp_snooping', 'switch_controller_dhcp_snooping_option82',
                   'switch_controller_dhcp_snooping_verify_mac', 'switch_controller_igmp_snooping', 'switch_controller_learning_limit',
                   'tagging', 'tcp_mss', 'trust_ip_1',
                   'trust_ip_2', 'trust_ip_3', 'trust_ip6_1',
                   'trust_ip6_2', 'trust_ip6_3', 'type',
                   'username', 'vdom', 'vindex',
                   'vlanforward', 'vlanid', 'vrf',
                   'vrrp', 'vrrp_virtual_mac', 'wccp',
                   'weight', 'wins_ip']
    dictionary = {}

    for attribute in option_list:
        if attribute in json and json[attribute] is not None:
            dictionary[attribute] = json[attribute]

    return dictionary


def flatten_multilists_attributes(data):
    multilist_attrs = [['allowaccess'], ['ipv6', 'ip6_allowaccess']]

    for attr in multilist_attrs:
        try:
            path = "data['" + "']['".join(elem for elem in attr) + "']"
            current_val = eval(path)
            flattened_val = ' '.join(elem for elem in current_val)
            exec(path + '= flattened_val')
        except BaseException:
            pass

    return data


def underscore_to_hyphen(data):
    if isinstance(data, list):
        for elem in data:
            elem = underscore_to_hyphen(elem)
    elif isinstance(data, dict):
        new_data = {}
        for k, v in data.items():
            new_data[k.replace('_', '-')] = underscore_to_hyphen(v)
        data = new_data

    return data


def system_interface(data, fos, check_mode=False):
    vdom = data['vdom']
    state = data['state']

    if not check_mode:
        system_interface_data = data['system_interface']
        system_interface_data = flatten_multilists_attributes(system_interface_data)
        filtered_data = underscore_to_hyphen(filter_system_interface_data(system_interface_data))

    if check_mode:
        return fos.get('system',
                       'interface',
                       vdom=vdom)

    if state == "present":
        return fos.set('system',
                       'interface',
                       data=filtered_data,
                       vdom=vdom)

    elif state == "absent":
        return fos.delete('system',
                          'interface',
                          mkey=filtered_data['name'],
                          vdom=vdom)


def is_successful_status(status):
    return status['status'] == "success" or \
        status['http_method'] == "DELETE" and status['http_status'] == 404


def fortios_system(data, fos, check_mode=False):
    login(data, fos)

    if check_mode or (not check_mode and data['system_interface']):
        resp = system_interface(data, fos, check_mode)

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
        "state": {"required": True, "type": "str", "choices": ["present", "absent"]},
        "system_interface": {
            "required": True, "type": "dict",
            "options": {
                "ac_name": {"required": False, "type": "str"},
                "aggregate": {"required": False, "type": "str"},
                "algorithm": {"required": False, "type": "str",
                              "choices": ["L2", "L3", "L4"]},
                "alias": {"required": False, "type": "str"},
                "allowaccess": {"required": False, "type": "list",
                                "choices": ["ping", "https", "ssh",
                                            "snmp", "http", "telnet",
                                            "fgfm", "radius-acct", "probe-response",
                                            "capwap", "ftm"]},
                "ap_discover": {"required": False, "type": "str",
                                "choices": ["enable", "disable"]},
                "arpforward": {"required": False, "type": "str",
                               "choices": ["enable", "disable"]},
                "auth_type": {"required": False, "type": "str",
                              "choices": ["auto", "pap", "chap",
                                          "mschapv1", "mschapv2"]},
                "auto_auth_extension_device": {"required": False, "type": "str",
                                               "choices": ["enable", "disable"]},
                "bfd": {"required": False, "type": "str",
                        "choices": ["global", "enable", "disable"]},
                "bfd_desired_min_tx": {"required": False, "type": "int"},
                "bfd_detect_mult": {"required": False, "type": "int"},
                "bfd_required_min_rx": {"required": False, "type": "int"},
                "broadcast_forticlient_discovery": {"required": False, "type": "str",
                                                    "choices": ["enable", "disable"]},
                "broadcast_forward": {"required": False, "type": "str",
                                      "choices": ["enable", "disable"]},
                "captive_portal": {"required": False, "type": "int"},
                "cli_conn_status": {"required": False, "type": "int"},
                "color": {"required": False, "type": "int"},
                "dedicated_to": {"required": False, "type": "str",
                                 "choices": ["none", "management"]},
                "defaultgw": {"required": False, "type": "str",
                              "choices": ["enable", "disable"]},
                "description": {"required": False, "type": "str"},
                "detected_peer_mtu": {"required": False, "type": "int"},
                "detectprotocol": {"required": False, "type": "str",
                                   "choices": ["ping", "tcp-echo", "udp-echo"]},
                "detectserver": {"required": False, "type": "str"},
                "device_access_list": {"required": False, "type": "str"},
                "device_identification": {"required": False, "type": "str",
                                          "choices": ["enable", "disable"]},
                "device_identification_active_scan": {"required": False, "type": "str",
                                                      "choices": ["enable", "disable"]},
                "device_netscan": {"required": False, "type": "str",
                                   "choices": ["disable", "enable"]},
                "device_user_identification": {"required": False, "type": "str",
                                               "choices": ["enable", "disable"]},
                "devindex": {"required": False, "type": "int"},
                "dhcp_client_identifier": {"required": False, "type": "str"},
                "dhcp_relay_agent_option": {"required": False, "type": "str",
                                            "choices": ["enable", "disable"]},
                "dhcp_relay_ip": {"required": False, "type": "str"},
                "dhcp_relay_service": {"required": False, "type": "str",
                                       "choices": ["disable", "enable"]},
                "dhcp_relay_type": {"required": False, "type": "str",
                                    "choices": ["regular", "ipsec"]},
                "dhcp_renew_time": {"required": False, "type": "int"},
                "disc_retry_timeout": {"required": False, "type": "int"},
                "disconnect_threshold": {"required": False, "type": "int"},
                "distance": {"required": False, "type": "int"},
                "dns_server_override": {"required": False, "type": "str",
                                        "choices": ["enable", "disable"]},
                "drop_fragment": {"required": False, "type": "str",
                                  "choices": ["enable", "disable"]},
                "drop_overlapped_fragment": {"required": False, "type": "str",
                                             "choices": ["enable", "disable"]},
                "egress_shaping_profile": {"required": False, "type": "str"},
                "endpoint_compliance": {"required": False, "type": "str",
                                        "choices": ["enable", "disable"]},
                "estimated_downstream_bandwidth": {"required": False, "type": "int"},
                "estimated_upstream_bandwidth": {"required": False, "type": "int"},
                "explicit_ftp_proxy": {"required": False, "type": "str",
                                       "choices": ["enable", "disable"]},
                "explicit_web_proxy": {"required": False, "type": "str",
                                       "choices": ["enable", "disable"]},
                "external": {"required": False, "type": "str",
                             "choices": ["enable", "disable"]},
                "fail_action_on_extender": {"required": False, "type": "str",
                                            "choices": ["soft-restart", "hard-restart", "reboot"]},
                "fail_alert_interfaces": {"required": False, "type": "list",
                                          "options": {
                                              "name": {"required": True, "type": "str"}
                                          }},
                "fail_alert_method": {"required": False, "type": "str",
                                      "choices": ["link-failed-signal", "link-down"]},
                "fail_detect": {"required": False, "type": "str",
                                "choices": ["enable", "disable"]},
                "fail_detect_option": {"required": False, "type": "str",
                                       "choices": ["detectserver", "link-down"]},
                "fortiheartbeat": {"required": False, "type": "str",
                                   "choices": ["enable", "disable"]},
                "fortilink": {"required": False, "type": "str",
                              "choices": ["enable", "disable"]},
                "fortilink_backup_link": {"required": False, "type": "int"},
                "fortilink_split_interface": {"required": False, "type": "str",
                                              "choices": ["enable", "disable"]},
                "fortilink_stacking": {"required": False, "type": "str",
                                       "choices": ["enable", "disable"]},
                "forward_domain": {"required": False, "type": "int"},
                "gwdetect": {"required": False, "type": "str",
                             "choices": ["enable", "disable"]},
                "ha_priority": {"required": False, "type": "int"},
                "icmp_accept_redirect": {"required": False, "type": "str",
                                         "choices": ["enable", "disable"]},
                "icmp_send_redirect": {"required": False, "type": "str",
                                       "choices": ["enable", "disable"]},
                "ident_accept": {"required": False, "type": "str",
                                 "choices": ["enable", "disable"]},
                "idle_timeout": {"required": False, "type": "int"},
                "inbandwidth": {"required": False, "type": "int"},
                "ingress_spillover_threshold": {"required": False, "type": "int"},
                "interface": {"required": False, "type": "str"},
                "internal": {"required": False, "type": "int"},
                "ip": {"required": False, "type": "str"},
                "ipmac": {"required": False, "type": "str",
                          "choices": ["enable", "disable"]},
                "ips_sniffer_mode": {"required": False, "type": "str",
                                     "choices": ["enable", "disable"]},
                "ipunnumbered": {"required": False, "type": "str"},
                "ipv6": {"required": False, "type": "dict",
                         "options": {
                             "autoconf": {"required": False, "type": "str",
                                          "choices": ["enable", "disable"]},
                             "dhcp6_client_options": {"required": False, "type": "str",
                                                      "choices": ["rapid", "iapd", "iana"]},
                             "dhcp6_information_request": {"required": False, "type": "str",
                                                           "choices": ["enable", "disable"]},
                             "dhcp6_prefix_delegation": {"required": False, "type": "str",
                                                         "choices": ["enable", "disable"]},
                             "dhcp6_prefix_hint": {"required": False, "type": "str"},
                             "dhcp6_prefix_hint_plt": {"required": False, "type": "int"},
                             "dhcp6_prefix_hint_vlt": {"required": False, "type": "int"},
                             "dhcp6_relay_ip": {"required": False, "type": "str"},
                             "dhcp6_relay_service": {"required": False, "type": "str",
                                                     "choices": ["disable", "enable"]},
                             "dhcp6_relay_type": {"required": False, "type": "str",
                                                  "choices": ["regular"]},
                             "ip6_address": {"required": False, "type": "str"},
                             "ip6_allowaccess": {"required": False, "type": "list",
                                                 "choices": ["ping", "https", "ssh",
                                                             "snmp", "http", "telnet",
                                                             "fgfm", "capwap"]},
                             "ip6_default_life": {"required": False, "type": "int"},
                             "ip6_delegated_prefix_list": {"required": False, "type": "list",
                                                           "options": {
                                                               "autonomous_flag": {"required": False, "type": "str",
                                                                                   "choices": ["enable", "disable"]},
                                                               "onlink_flag": {"required": False, "type": "str",
                                                                               "choices": ["enable", "disable"]},
                                                               "prefix_id": {"required": False, "type": "int"},
                                                               "rdnss": {"required": False, "type": "str"},
                                                               "rdnss_service": {"required": False, "type": "str",
                                                                                 "choices": ["delegated", "default", "specify"]},
                                                               "subnet": {"required": False, "type": "str"},
                                                               "upstream_interface": {"required": False, "type": "str"}
                                                           }},
                             "ip6_dns_server_override": {"required": False, "type": "str",
                                                         "choices": ["enable", "disable"]},
                             "ip6_extra_addr": {"required": False, "type": "list",
                                                "options": {
                                                    "prefix": {"required": True, "type": "str"}
                                                }},
                             "ip6_hop_limit": {"required": False, "type": "int"},
                             "ip6_link_mtu": {"required": False, "type": "int"},
                             "ip6_manage_flag": {"required": False, "type": "str",
                                                 "choices": ["enable", "disable"]},
                             "ip6_max_interval": {"required": False, "type": "int"},
                             "ip6_min_interval": {"required": False, "type": "int"},
                             "ip6_mode": {"required": False, "type": "str",
                                          "choices": ["static", "dhcp", "pppoe",
                                                      "delegated"]},
                             "ip6_other_flag": {"required": False, "type": "str",
                                                "choices": ["enable", "disable"]},
                             "ip6_prefix_list": {"required": False, "type": "list",
                                                 "options": {
                                                     "autonomous_flag": {"required": False, "type": "str",
                                                                         "choices": ["enable", "disable"]},
                                                     "dnssl": {"required": False, "type": "list",
                                                               "options": {
                                                                   "domain": {"required": True, "type": "str"}
                                                               }},
                                                     "onlink_flag": {"required": False, "type": "str",
                                                                     "choices": ["enable", "disable"]},
                                                     "preferred_life_time": {"required": False, "type": "int"},
                                                     "prefix": {"required": True, "type": "str"},
                                                     "rdnss": {"required": False, "type": "str"},
                                                     "valid_life_time": {"required": False, "type": "int"}
                                                 }},
                             "ip6_reachable_time": {"required": False, "type": "int"},
                             "ip6_retrans_time": {"required": False, "type": "int"},
                             "ip6_send_adv": {"required": False, "type": "str",
                                              "choices": ["enable", "disable"]},
                             "ip6_subnet": {"required": False, "type": "str"},
                             "ip6_upstream_interface": {"required": False, "type": "str"},
                             "nd_cert": {"required": False, "type": "str"},
                             "nd_cga_modifier": {"required": False, "type": "str"},
                             "nd_mode": {"required": False, "type": "str",
                                         "choices": ["basic", "SEND-compatible"]},
                             "nd_security_level": {"required": False, "type": "int"},
                             "nd_timestamp_delta": {"required": False, "type": "int"},
                             "nd_timestamp_fuzz": {"required": False, "type": "int"},
                             "vrip6_link_local": {"required": False, "type": "str"},
                             "vrrp_virtual_mac6": {"required": False, "type": "str",
                                                   "choices": ["enable", "disable"]},
                             "vrrp6": {"required": False, "type": "list",
                                       "options": {
                                           "accept_mode": {"required": False, "type": "str",
                                                           "choices": ["enable", "disable"]},
                                           "adv_interval": {"required": False, "type": "int"},
                                           "preempt": {"required": False, "type": "str",
                                                       "choices": ["enable", "disable"]},
                                           "priority": {"required": False, "type": "int"},
                                           "start_time": {"required": False, "type": "int"},
                                           "status": {"required": False, "type": "str",
                                                      "choices": ["enable", "disable"]},
                                           "vrdst6": {"required": False, "type": "str"},
                                           "vrgrp": {"required": False, "type": "int"},
                                           "vrid": {"required": True, "type": "int"},
                                           "vrip6": {"required": False, "type": "str"}
                                       }}
                         }},
                "l2forward": {"required": False, "type": "str",
                              "choices": ["enable", "disable"]},
                "lacp_ha_slave": {"required": False, "type": "str",
                                  "choices": ["enable", "disable"]},
                "lacp_mode": {"required": False, "type": "str",
                              "choices": ["static", "passive", "active"]},
                "lacp_speed": {"required": False, "type": "str",
                               "choices": ["slow", "fast"]},
                "lcp_echo_interval": {"required": False, "type": "int"},
                "lcp_max_echo_fails": {"required": False, "type": "int"},
                "link_up_delay": {"required": False, "type": "int"},
                "lldp_transmission": {"required": False, "type": "str",
                                      "choices": ["enable", "disable", "vdom"]},
                "macaddr": {"required": False, "type": "str"},
                "managed_device": {"required": False, "type": "list",
                                   "options": {
                                       "name": {"required": True, "type": "str"}
                                   }},
                "management_ip": {"required": False, "type": "str"},
                "member": {"required": False, "type": "list",
                           "options": {
                               "interface_name": {"required": False, "type": "str"}
                           }},
                "min_links": {"required": False, "type": "int"},
                "min_links_down": {"required": False, "type": "str",
                                   "choices": ["operational", "administrative"]},
                "mode": {"required": False, "type": "str",
                         "choices": ["static", "dhcp", "pppoe"]},
                "mtu": {"required": False, "type": "int"},
                "mtu_override": {"required": False, "type": "str",
                                 "choices": ["enable", "disable"]},
                "name": {"required": True, "type": "str"},
                "ndiscforward": {"required": False, "type": "str",
                                 "choices": ["enable", "disable"]},
                "netbios_forward": {"required": False, "type": "str",
                                    "choices": ["disable", "enable"]},
                "netflow_sampler": {"required": False, "type": "str",
                                    "choices": ["disable", "tx", "rx",
                                                "both"]},
                "outbandwidth": {"required": False, "type": "int"},
                "padt_retry_timeout": {"required": False, "type": "int"},
                "password": {"required": False, "type": "str"},
                "ping_serv_status": {"required": False, "type": "int"},
                "polling_interval": {"required": False, "type": "int"},
                "pppoe_unnumbered_negotiate": {"required": False, "type": "str",
                                               "choices": ["enable", "disable"]},
                "pptp_auth_type": {"required": False, "type": "str",
                                   "choices": ["auto", "pap", "chap",
                                               "mschapv1", "mschapv2"]},
                "pptp_client": {"required": False, "type": "str",
                                "choices": ["enable", "disable"]},
                "pptp_password": {"required": False, "type": "str"},
                "pptp_server_ip": {"required": False, "type": "str"},
                "pptp_timeout": {"required": False, "type": "int"},
                "pptp_user": {"required": False, "type": "str"},
                "preserve_session_route": {"required": False, "type": "str",
                                           "choices": ["enable", "disable"]},
                "priority": {"required": False, "type": "int"},
                "priority_override": {"required": False, "type": "str",
                                      "choices": ["enable", "disable"]},
                "proxy_captive_portal": {"required": False, "type": "str",
                                         "choices": ["enable", "disable"]},
                "redundant_interface": {"required": False, "type": "str"},
                "remote_ip": {"required": False, "type": "str"},
                "replacemsg_override_group": {"required": False, "type": "str"},
                "role": {"required": False, "type": "str",
                         "choices": ["lan", "wan", "dmz",
                                     "undefined"]},
                "sample_direction": {"required": False, "type": "str",
                                     "choices": ["tx", "rx", "both"]},
                "sample_rate": {"required": False, "type": "int"},
                "scan_botnet_connections": {"required": False, "type": "str",
                                            "choices": ["disable", "block", "monitor"]},
                "secondary_IP": {"required": False, "type": "str",
                                 "choices": ["enable", "disable"]},
                "secondaryip": {"required": False, "type": "list",
                                "options": {
                                    "allowaccess": {"required": False, "type": "str",
                                                    "choices": ["ping", "https", "ssh",
                                                                "snmp", "http", "telnet",
                                                                "fgfm", "radius-acct", "probe-response",
                                                                "capwap", "ftm"]},
                                    "detectprotocol": {"required": False, "type": "str",
                                                       "choices": ["ping", "tcp-echo", "udp-echo"]},
                                    "detectserver": {"required": False, "type": "str"},
                                    "gwdetect": {"required": False, "type": "str",
                                                 "choices": ["enable", "disable"]},
                                    "ha_priority": {"required": False, "type": "int"},
                                    "id": {"required": True, "type": "int"},
                                    "ip": {"required": False, "type": "str"},
                                    "ping_serv_status": {"required": False, "type": "int"}
                                }},
                "security_exempt_list": {"required": False, "type": "str"},
                "security_external_logout": {"required": False, "type": "str"},
                "security_external_web": {"required": False, "type": "str"},
                "security_groups": {"required": False, "type": "list",
                                    "options": {
                                        "name": {"required": True, "type": "str"}
                                    }},
                "security_mac_auth_bypass": {"required": False, "type": "str",
                                             "choices": ["enable", "disable"]},
                "security_mode": {"required": False, "type": "str",
                                  "choices": ["none", "captive-portal", "802.1X"]},
                "security_redirect_url": {"required": False, "type": "str"},
                "service_name": {"required": False, "type": "str"},
                "sflow_sampler": {"required": False, "type": "str",
                                  "choices": ["enable", "disable"]},
                "snmp_index": {"required": False, "type": "int"},
                "speed": {"required": False, "type": "str",
                          "choices": ["auto", "10full", "10half",
                                      "100full", "100half", "1000full",
                                      "1000half", "1000auto"]},
                "spillover_threshold": {"required": False, "type": "int"},
                "src_check": {"required": False, "type": "str",
                              "choices": ["enable", "disable"]},
                "status": {"required": False, "type": "str",
                           "choices": ["up", "down"]},
                "stpforward": {"required": False, "type": "str",
                               "choices": ["enable", "disable"]},
                "stpforward_mode": {"required": False, "type": "str",
                                    "choices": ["rpl-all-ext-id", "rpl-bridge-ext-id", "rpl-nothing"]},
                "subst": {"required": False, "type": "str",
                          "choices": ["enable", "disable"]},
                "substitute_dst_mac": {"required": False, "type": "str"},
                "switch": {"required": False, "type": "str"},
                "switch_controller_access_vlan": {"required": False, "type": "str",
                                                  "choices": ["enable", "disable"]},
                "switch_controller_arp_inspection": {"required": False, "type": "str",
                                                     "choices": ["enable", "disable"]},
                "switch_controller_dhcp_snooping": {"required": False, "type": "str",
                                                    "choices": ["enable", "disable"]},
                "switch_controller_dhcp_snooping_option82": {"required": False, "type": "str",
                                                             "choices": ["enable", "disable"]},
                "switch_controller_dhcp_snooping_verify_mac": {"required": False, "type": "str",
                                                               "choices": ["enable", "disable"]},
                "switch_controller_igmp_snooping": {"required": False, "type": "str",
                                                    "choices": ["enable", "disable"]},
                "switch_controller_learning_limit": {"required": False, "type": "int"},
                "tagging": {"required": False, "type": "list",
                            "options": {
                                "category": {"required": False, "type": "str"},
                                "name": {"required": True, "type": "str"},
                                "tags": {"required": False, "type": "list",
                                         "options": {
                                             "name": {"required": True, "type": "str"}
                                         }}
                            }},
                "tcp_mss": {"required": False, "type": "int"},
                "trust_ip_1": {"required": False, "type": "str"},
                "trust_ip_2": {"required": False, "type": "str"},
                "trust_ip_3": {"required": False, "type": "str"},
                "trust_ip6_1": {"required": False, "type": "str"},
                "trust_ip6_2": {"required": False, "type": "str"},
                "trust_ip6_3": {"required": False, "type": "str"},
                "type": {"required": False, "type": "str",
                         "choices": ["physical", "vlan", "aggregate",
                                     "redundant", "tunnel", "vdom-link",
                                     "loopback", "switch", "hard-switch",
                                     "vap-switch", "wl-mesh", "fext-wan",
                                     "vxlan", "hdlc", "switch-vlan"]},
                "username": {"required": False, "type": "str"},
                "vdom": {"required": False, "type": "str"},
                "vindex": {"required": False, "type": "int"},
                "vlanforward": {"required": False, "type": "str",
                                "choices": ["enable", "disable"]},
                "vlanid": {"required": False, "type": "int"},
                "vrf": {"required": False, "type": "int"},
                "vrrp": {"required": False, "type": "list",
                         "options": {
                             "accept_mode": {"required": False, "type": "str",
                                             "choices": ["enable", "disable"]},
                             "adv_interval": {"required": False, "type": "int"},
                             "preempt": {"required": False, "type": "str",
                                         "choices": ["enable", "disable"]},
                             "priority": {"required": False, "type": "int"},
                             "proxy_arp": {"required": False, "type": "list",
                                           "options": {
                                               "id": {"required": True, "type": "int"},
                                               "ip": {"required": False, "type": "str"}
                                           }},
                             "start_time": {"required": False, "type": "int"},
                             "status": {"required": False, "type": "str",
                                        "choices": ["enable", "disable"]},
                             "version": {"required": False, "type": "str",
                                         "choices": ["2", "3"]},
                             "vrdst": {"required": False, "type": "str"},
                             "vrdst_priority": {"required": False, "type": "int"},
                             "vrgrp": {"required": False, "type": "int"},
                             "vrid": {"required": True, "type": "int"},
                             "vrip": {"required": False, "type": "str"}
                         }},
                "vrrp_virtual_mac": {"required": False, "type": "str",
                                     "choices": ["enable", "disable"]},
                "wccp": {"required": False, "type": "str",
                         "choices": ["enable", "disable"]},
                "weight": {"required": False, "type": "int"},
                "wins_ip": {"required": False, "type": "str"}

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