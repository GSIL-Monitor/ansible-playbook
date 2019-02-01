Role Name: kubeadm-init
=========

目前, 版本为 1.12.2, 最新版本为 1.13. 

目前尚未支持 1.13 的版本, 因为要翻墙做镜像.

该 role 用于 kubeadm 建立 kubernetes 集群**之前**初始化系统所用. 


Role 所用变量
-------------
参见 `kubeadm-init/default/main.yml`

可能需要修改的变量, 避免与本地网络冲突:
- POD_NETWORK: "10.244.0.0/16"
- SERVICE_NETWORK: "192.168.251.0/24"


Playbook 依赖
-------------

A list of other roles hosted on Galaxy should go here, plus any details in regards to parameters that may need to be set for other roles, or variables that are used from other roles.

Playbook 使用示例
----------------

Playbook 参考:
```
roles/kubeadm-init/pb.yml
```
hosts 参考: 修改下面配置文件中的 ip 地址, 用户, 密码 即可, 注意 kube_role 变量 指代 主机在 kubernets 中的角色. master 只能有一个, node 可以有多个.
```
# roles/kubeadm-init/hosts
[kube]
192.168.1.11 ansible_ssh_host=192.168.1.11 ansible_ssh_user="root" ansible_ssh_pass="123456" ansible_ssh_port=22 kube_role=master
192.168.1.111 ansible_ssh_host=192.168.1.111 ansible_ssh_user="root" ansible_ssh_pass="123456" ansible_ssh_port=22 kube_role=node
```
运行 Playbook: 使用时, 请把 `pb.yml`, `hosts` 文件拷贝到 `roles` 同级目录, 并根据需要修改之后使用如下命令.
```
$ ansible-playbook -i hosts pb.yml
```

Bug
----
目前 kubeadm 升级到了 1.13 的版本, 本playbook 安装为 1.12, 所以在镜像上会有不同, 出现错误, 正在修复中.


License
-------

BSD

Author Information
------------------

An optional section for the role authors to include contact information, or a website (HTML is not allowed).
