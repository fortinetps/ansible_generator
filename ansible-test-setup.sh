cd /workspaces/ansible
. venv/bin/activate
. hacking/env-setup
ansible-test units --tox --python 3.5 fortios_user_device
ansible-test units --tox --python 3.5 fortios_system_ha_checksums