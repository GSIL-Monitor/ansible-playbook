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
  docker:
    required: false
    default: null
    description:
      - the path to the docker cli
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

  state:
    required: false
    choices: ['present', 'absent', 'latest', 'reloaded']
    default: present
    description:
      - present handles checking existence or creating if definition file provided,
        absent handles deleting resource(s) based on other options,
        latest handles creating or updating based on existence,
        reloaded handles updating resource(s) definition using definition file,
        stopped handles stopping resource(s) based on other options.
requirements:
  - docker
author: "Bob Bi"
"""

EXAMPLES = """
- name: docker pull kube-apiserver:v1.12.2
  dkrPullImgAcrossGfw:
    docker: docker
  	tag_ori: localRepo/kube-apiserver
  	tag_ori_ver: v1.12.2
  	tag_dest: gct.io/kube-apiserver
    tag_dest_ver: v1.12.2
    keep_ori: false
    state: present
"""


class dkrPullImgAcrossGfw(object):
    DEFAULT_VERSION="latest"

    def __init__(self, module):
        self.module = module
        self.docker = module.params.get("docker")

        if self.docker is None:
            self.docker = module.get_bin_path("docker")
        self.base_cmd = [self.docker]

        self.keep_ori = module.params.get("keep_ori"):
        
        self.tag_ori_ver = module.params.get("tag_ori_ver"):
        if self.tag_ori_ver is None:
            self.tag_ori_ver = self.DEFAULT_VERSION
        self.ori_tag_ver = ":".join([module.params.get("tag_ori"), self.tag_ori_ver])

        self.tag_dest_ver = module.params.get("tag_dest_ver")
        if self.tag_dest_ver is None:
            self.tag_dest_ver = self.DEFAULT_VERSION
        self.dest_tag_ver = ":".join([module.params.get("tag_dest"), self.tag_dest_ver])

    def _is_image_exist(self, tag_ver):
        # docker image inspect TAG:VER
        cmd_l = ["image", "inspect", tag_ver]
        rc, _, _ = self._run_cmd(cmd_l)
        if int(rc) == 0:
            return True
        return False

    def _pull(self, tag_ver):
        # docker pull TAG:VER
        cmd_l = ["pull", tag_ver]
        return self._execute(cmd_l)

    def _tag(self, ori_tag_ver, dest_tag_ver):
        # docker tag TAG_ORI:VER_ORI TAG_DEST:VER_DEST
        cmd_l = ["tag", ori_tag_ver, dest_tag_ver]
        return self._execute(cmd_l)

    def _rmi(self, tag_vers):
        # docker rmi TAG:VER
        cmd_l = ["rmi"]
        if isinstance(tag_vers, list):
            cmd_l += tag_vers
        else:
            cmd_l.append(tag_vers)

        return self._execute(cmd_l)

    def pull_tag_rmi(self):
        if self._is_image_exist(self.dest_tag_ver):
            return []

        res = list()
        # pull
        res_pull = self._pull(self.ori_tag_ver)
        res.append(res_pull)

        # tag
        res_tag = self._tag(self.ori_tag_ver, dest_tag_ver)
        res.append(res_tag)

        # rmi
        if not self.keep_ori and self._is_image_exist(self.ori_tag_ver):
            res_rmi = self._rmi(self.ori_tag_ver)
            res.append(res_rmi)

        return res

    def rmi(self):
        imgs = list()
        if self._is_image_exist(self.dest_tag_ver):
            imgs.append(self.dest_tag_ver)
        if self._is_image_exist(self.ori_tag_ver):
            imgs.append(self.ori_tag_ver)
        return self._rmi(imgs)

    def _run_cmd(self, cmd):
        """ run cmd and get cmd return code"""
        args = self.base_cmd + cmd
        rc, out, err = self.module.run_command(args)
        return rc, out, err

    def _execute(self, cmd):
        try:
            rc, out, err = self._run_cmd(cmd)
            if rc != 0:
                self.module.fail_json(
                    msg='error running docker (%s) command (rc=%d), out=\'%s\', err=\'%s\'' % (' '.join(args), rc, out, err))
        except Exception as exc:
            self.module.fail_json(
                msg='error running docker (%s) command: %s' % (' '.join(args), str(exc)))
        return out.splitlines()

    def _execute_nofail(self, cmd):
        rc, out, err = self._run_cmd(cmd)
        if rc != 0:
            return None
        return out.splitlines()


def main():

    module = AnsibleModule(
        argument_spec=dict(
            name=dict(),
            docker=dict(),
            tag_ori=dict(),
            tag_ori_ver=dict(default="latest", type='string'),
            tag_dest=dict(),
            tag_dest_ver=dict(default="latest", type='string'),
            keep_ori=dict(default=False, type='bool'),
            state=dict(default='present', choices=['present', 'absent', 'latest', 'reloaded']),
            ),
            mutually_exclusive=[['filename', 'list']]
        )

    changed = False

    manager = dkrPullImgAcrossGfw(module)
    state = module.params.get('state')
    if state in ['present', 'latest', 'reloaded']:
        result = manager.pull_tag_rmi()

    elif state == 'absent':
        result = manager.rmi()

    else:
        module.fail_json(msg='Unrecognized state %s.' % state)

    module.exit_json(changed=changed,
                     msg='success: %s' % (' '.join(result))
                     )


from ansible.module_utils.basic import *  # noqa
if __name__ == '__main__':
    main()

