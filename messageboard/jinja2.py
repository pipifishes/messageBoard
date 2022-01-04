from django.contrib.staticfiles.storage import staticfiles_storage
from django.urls import reverse
from jinja2 import Environment
'''
需要安装Jinja2模块
'''
# 将jinja2模板定义到Django环境中
def environment(**options):
    env = Environment(**options)
    env.globals.update({
        'static':staticfiles_storage.url,
        'url': reverse,
    })
    return env


