#!/usr/bin/env
#

from ansible.module_utils.basic import *

# 创建一个AnsibleModule的实例,argument_spec初始化参数为空字典,因为我们这个模块不需要传递参数,所以传递空字典进去就好了.
module = AnsibleModule(
        argument_spec = dict(),
)
# 调用本地系统命令获取时区设置
status,output = commands.getstatusoutput('''date''')
if status == 0:
        # 按照ansible 的返回格式定义返回内容,stdout为标准输出,changed代表系统有没有东西被变更,rc=0代表执行成功
        result = dict(module='timezone',stdout=output,changed=False,rc=0)
        # 使用ansible规则的module实例下的exit_json返回正常内容
        module.exit_json(**result)
else:
        result = dict(msg='execute failed',rc=status)
        # 当调用失败返回错误信息的时候,数据字典只要传递msg信息就可了,然后调用module实例的fail_json方法给返回
        module.fail_json(**result)