from  django.urls import path
from .views import newview

urlpatterns = [
    path('',newview,name='index'),
]
# newview是.views.py定义的视图函数；name是别名