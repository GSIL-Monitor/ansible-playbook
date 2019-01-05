#!/usr/bin/env python
# 
# args: 
#	- tag_ori: str, 镜像原来名字
#	- tag_ori_ver: str, 镜像原来版本, 默认 latest
#	- tag_dest: str, 镜像目标名字
#	- tag_dest_ver: str, 镜像目标版本, 默认 latest
#	- keep_ori: bool, 是够保存 原有镜像.
# 
# if is_exist tag_dest:tag_dest_ver:
# 	return tag_dest:tag_dest_ver
# else:
# 	docker pull tag_ori:tag_ori_ver && \
# 	docker tag tag_ori:tag_dest_ver tag_dest:tag_dest_ver 

# 	if not keep_ori:
# 		docker rmi tag_ori:tag_ori_ver

DOCUMENTATION = """
---
module: dkrPullImgAcrossGfw
short_description: docker pull images and rename to a new name, for docker pull images across GFW
description:
  - docker pull images across GFW
version_added: "0.1"
options:
  name:
    required: false
    default: null
    description:
      - The name associated with resource
  tag_ori:
    required: true
    default: null
    description:
      - origin docker images name
  tag_ori_ver:
    required: false
    default: latest
    description:
      - origin docker images version
  tag_dest:
    required: true
    default: null
    description:
      - dest docker images name
  tag_dest_ver:
    required: false
    default: latest
    description:
      - origin docker images version
  keep_ori:
    required: false
    default: false
    description:
      - keep the origin docker image or not.
requirements:
  - docker
author: "Bob Bi"
"""

EXAMPLES = """
- name: docker pull kube-apiserver:v1.12.2
  dkrPullImgAcrossGfw:
  	tag_ori: kube-apiserver
  	tag_ori_ver: v1.12.2
  	tag_dest: 

- name: test nginx is stopped
  kube: name=nginx resource=rc state=stopped

- name: test nginx is absent
  kube: name=nginx resource=rc state=absent

- name: test nginx is present
  kube: filename=/tmp/nginx.yml

- name: test nginx and postgresql are present
  kube: files=/tmp/nginx.yml,/tmp/postgresql.yml

- name: test nginx and postgresql are present
  kube:
    files:
      - /tmp/nginx.yml
      - /tmp/postgresql.yml
"""
