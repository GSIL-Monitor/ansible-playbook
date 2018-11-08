ansible-playbook
==================
个人常用 ansible-playbook 说明.

## 一. 目录说明
- `tools` : 可能会用到的工具
- `filter_plugins` : 自定义过滤器
- `roles` : ansible-playbook roles
- `roles/ROLE_NAME/{pb.yml, hosts, README.md}` : 当前 role 使用的示例文件.
	- `pb.yml` : playbook 引导文件
	- `hosts` : inventory 文件, **可能包含所需的变量**.
	- `README.md` : 当前 role 的使用说明与帮助文件.

注意:
1. ansible-playbook 目录下的所有 `hosts_*`, `tmp/`, 'tmp_*' 文件都**不会**上传到 git

## 二. Base Rule
1. role 所使用的**局部变量**, 默认 放在 `roles/ROLE/defaule/main.yaml`
2. 全局变量位于 `hosts_var`, `group_var` 目录.

