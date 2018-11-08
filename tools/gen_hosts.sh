#!/bin/bash
#
set -e

HOSTLIST=(
127.0.0.1
192.168.1.15
)

SYS_USER="bob.bi"
SYS_USER_PASS="123456"

# ASB_FILES_PATH='roles/derby-upload-backup/files'
# TMP_FILES_PATH='pkgs'

# echo "Clean roles files dir"
# rm -fr $ASB_FILES_PATH/*

# echo "Copy package to roles files dir"
# for pkg in `ls $TMP_FILES_PATH`; do
#     if [ -f $TMP_FILES_PATH/$pkg ];then
#         for i in  ${HOSTLIST[@]};do
#             mkdir $ASB_FILES_PATH/$i && cp $TMP_FILES_PATH/$pkg $ASB_FILES_PATH/$i
#         done
            
#     else
#         mv $TMP_FILES_PATH/$pkg $ASB_FILES_PATH
#     fi
# done 

# echo "Get PkgName"
# PkgName=`find $ASB_FILES_PATH -type f | tail -1 | xargs basename`

echo "Gen inventory file"
echo >hosts
for i in  ${HOSTLIST[@]};do
    echo "$i ansible_ssh_host=$i ansible_ssh_user=$SYS_USER ansible_ssh_pass=$SYS_USER_PASS pkg_name=$PkgName " >> hosts
done

# echo "Clean tmp package dir ..."
# rm -fr $TMP_FILES_PATH/*

# echo "-----------------------------------------------------------------------------------"
# echo "Ansible Playbook Running ..."
# echo "-----------------------------------------------------------------------------------"
# ansible-playbook -i ./hosts ./derby-upload-backup.yml
