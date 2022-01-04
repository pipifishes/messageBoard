from django.shortcuts import render
'''
index文件夹的urls。py定义了几条路由信息，因此需要再index/views.py中定义相应的视图函数
'''

def page_not_found(request,exception):
    return render(request,'404.html',status=404)

def page_error(request):
    return render(request,'500.html',status=500)

from django.shortcuts import render,redirect
from .models import Message
from .form import MessageModeForm
def newview(request):
    message = Message.objects.all().order_by('-id')
    if request.method == 'POST':
        form = MessageModeForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')
    return render(request,'index.html',locals())








