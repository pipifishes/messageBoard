from django import forms
from .models import *
# 定义模型表单
class MessageModeForm(forms.ModelForm):
    class Meta:
        # 绑定模型
        model = Message
        fields = '__all__'
