Role Name: kubeadm-init
=========

该 role 用于 kubeadm 建立 kubernetes 集群**之前**初始化系统所用. 


Role 所用变量
-------------
参见 `kubeadm-init/default/main.yml`


Playbook 依赖
-------------

A list of other roles hosted on Galaxy should go here, plus any details in regards to parameters that may need to be set for other roles, or variables that are used from other roles.

Playbook 使用示例
----------------

Playbook 参考:
```
roles/kubeadm-init/pb.yml
```
hosts 参考:
```
roles/kubeadm-init/hosts
```
运行 Playbook: 使用时, 请把 `pb.yml`, `hosts` 文件拷贝到 `roles` 同级目录, 并根据需要修改之后使用如下命令.
```
$ ansible-playbook -i hosts pb.yml
```


License
-------

BSD

Author Information
------------------

An optional section for the role authors to include contact information, or a website (HTML is not allowed).
