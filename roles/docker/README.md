Role Name
=========

安装程序:
	docker-ce: latest
	docker-compose: 1.23.1
	docker-machine: v0.14.0

修改 docker-compose, docker-machine 版本, 方法有二:
1. 传入 `DOCKER_COMPOSE_VERSION`, `DOCKER_MACHINE_VERSION` 变量值.
2. 修改 `default/main.yml` 中 `DOCKER_COMPOSE_VERSION`, `DOCKER_MACHINE_VERSION` 的值.

Example Playbook
----------------
```
$ ansible-playbook -i hosts pb.yml
```

License
-------

BSD

Author Information
------------------

An optional section for the role authors to include contact information, or a website (HTML is not allowed).
