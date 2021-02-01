from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from .models import User

import hashlib


# Create your views here.
def login_view(request):
    if request.method == 'GET':
        if 'uname' in request.session and 'uid' in request.session:
            return HttpResponseRedirect('/note')
        return render(request, 'user/login.html')
    elif request.method == 'POST':
        # 1.获取数据
        username = request.POST['username']
        password = request.POST['password']
        # 2.数据检查
        if not username or not password:
            return HttpResponse('用户名或密码不能为空！')
        # 3.查看有无名称为username的用户
        try:
            user = User.objects.get(username=username)
        except:
            return HttpResponse('用户名或密码错误！')
        # 4.检查密码是否正确
        md5 = hashlib.md5()
        md5.update(password.encode())
        password_h = md5.hexdigest()
        if password_h != user.password:
            return HttpResponse('用户名或密码错误！')
        # 使用session保存登录状态
        request.session['uname'] = username
        request.session['uid'] = user.id

        return HttpResponseRedirect('/note/')


def reg_view(request):
    if request.method == 'GET':
        return render(request, 'user/register.html')
    elif request.method == 'POST':
        # 1.从表单元素中获取数据
        username = request.POST.get('username')
        password_1 = request.POST.get('password_1')
        password_2 = request.POST.get('password_2')

        # print((username,password_1,password_2))
        # 2.数据检查
        # 2.1为空检查
        if not username or not password_1:
            return HttpResponse('用户名和密码不能为空！')
        # 2.2两次密码要一样
        if password_1 != password_2:
            return HttpResponse('两次密码要一致')
        # 2.3用户名称不能重复
        old_user = User.objects.filter(username=username)
        if old_user:
            return HttpResponse('用户名已存在！')
        # 3.计算空口令(密码)的Hash值
        md5 = hashlib.md5()
        md5.update(password_1.encode())
        password_h = md5.hexdigest()

        # 4.数据入库
        try:
            User.objects.create(username=username, password=password_h)
        except:
            return HttpResponse('用户名被占用！')
        return HttpResponseRedirect('/user/login')


def logout_view(request):
    if 'uname' in request.session:
        del request.session['uname']
    if 'uid' in request.session:
        del request.session['uid']
    else:
        return HttpResponse('没有账户登录！')
    return HttpResponseRedirect('/user/login')
