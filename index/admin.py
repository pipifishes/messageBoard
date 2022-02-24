from django.contrib import admin
from .models import *
# 修改title和header
admin.site.site_title = '来访人员信息后台系统'
admin.site.site_header = '来访人员信息反馈平台'

@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    # 设置显示的字段
    list_display = ['id','name','content','timestamp','three_weeks','two_weeks','a_week']
    search_fields = ['name']
    # 以‘name’为过滤器
    list_filter = ['name']
    ordering = ['id']
    # 再数据列表页上方，设置日期选择器
    date_hierarchy = 'timestamp'