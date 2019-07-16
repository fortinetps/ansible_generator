#!/bin/bash


if [ -z $1 ]; then
  me=`basename "$0"`
  echo "Please indicate the root of the Ansible repository where you want to put generated files."
  echo "   e.g.:"
  echo "         ./${me} ~/ansible"
  echo ""
  exit -1
fi

if [ ! -f $1/MANIFEST.in ] || 
   [ ! -d $1/lib/ansible/modules/network/fortios/ ] || 
   [ ! -d $1/test/units/modules/network/fortios/ ]; then
  echo "Directory does not look like an official Ansible Repository."
  exit -1

fi

number=`find . -name "fortios_*.py" | wc -l `

echo "Copying ${number} Ansible modules to $1/lib/ansible/modules/network/fortios/ ..."
find . -name "fortios_*.py" -exec cp {} $1/lib/ansible/modules/network/fortios/ \;
echo "Copied"

number=`find . -name "test_*.py" | wc -l `

echo "Copying ${number} Ansible unit test files to $1/test/units/modules/network/fortios/ ..."
find . -name "test_*.py" -exec cp {} $1/test/units/modules/network/fortios/ \;
echo "Copied"