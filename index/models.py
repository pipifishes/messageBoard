from django.db import models
'''
1. 如果修改到其他数据库，需要先python3 manage.py migrate
2. 在模型中新增加字段导致报错,在原来已经有的表单中没有值。所以在新添加的值得括号中添加null=True
然后 python3 manage.py makemigrations ；python3 manage.py migrate
'''
# 定义单选框
gender_21days = (
    ('Y', ''), ('N', ''),   # 这里的元组后一位可以写，也可以为空
)
gender_14days = (
    ('Y', '是'), ('N', '否'),
)
gender_7days = (
    ('Y', ''), ('N', ''),
)

class Message(models.Model):
    # 定义‘信息管理表’中的列名
    id = models.AutoField('序号',primary_key=True)
    name = models.CharField('名称',max_length=50)
    content = models.IntegerField('联系方式',max_length=200)
    timestamp = models.DateField('反馈时间',auto_now=True)
    three_weeks = models.CharField(choices=gender_21days,max_length=100,null=True)
    two_weeks = models.CharField(choices=gender_14days,max_length=100,null=True)
    a_week = models.CharField(choices=gender_7days, max_length=100, null=True)

    def __str__(self):
        return self.name
    class Meta:
        # 在admin管理平台“信息管理”定义一张‘信息反馈表’
        verbose_name = '来访人员信息反馈'
        # 将admin后台显示的名称下的模型名称后的’s‘去掉
        verbose_name_plural = '来访人员信息反馈'