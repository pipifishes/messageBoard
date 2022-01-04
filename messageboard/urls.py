# 这是默认导入的包
from django.contrib import admin    # 导入内置admin功能模块
from django.urls import path,include,re_path    # 导入django的路由函数模块
from django.conf.urls import static
from django.conf import settings
'''
urlpatterns：代表整个项目的路由集合
include:是将路由信息分发给index的urls.py处理
'''

urlpatterns = [
    # 指向内置Admin后台系统的路由文件sites.py
    path('admin/', admin.site.urls),
    # 指向index的路由文件urls.py
    path('',include('index.urls'))
]

# 设置404，500错误状态码
from index import views
handler404 = views.page_not_found
handler500 = views.page_error


