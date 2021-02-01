from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from .models import Note


# Create your views here.

# 登录认证的装饰器
def login_check(fn):
    def wrap(request, *args, **kwargs):
        # 在session没有登录信息
        if 'uname' not in request.session or 'uid' not in request.session:
            # 重定向到登录url
            return HttpResponseRedirect('/user/login')
        return fn(request, *args, **kwargs)

    return wrap


@login_check
def list_view(request):
    username = request.session['uname']
    uid = request.session['uid']
    notes = Note.objects.filter(user_id = uid)
    return render(request,'note/list_note.html',locals())


@login_check
def add_view(request):
    if request.method == 'GET':
        return render(request, 'note/add_note.html')
    elif request.method == 'POST':
        # 1.获取数据
        title = request.POST['title']
        content = request.POST['content']
        uid = request.session['uid']
        # 2.数据入库
        Note.objects.create(title=title,content=content,user_id=uid)

        return HttpResponseRedirect('/note')


@login_check
def mod_view(request,uid):
    try:
        note = Note.objects.get(id=uid)
    except:
        return HttpResponse("没有这份笔记!")
    if request.method == 'GET':
        return render(request,'note/mod_note.html',locals())
    elif request.method == 'POST':
        note.title = request.POST['title']
        note.content = request.POST['content']
        note.save()
        return HttpResponseRedirect('/note')


@login_check
def del_view(request):
    uid = request.GET.get('uid')
    try:
        note = Note.objects.get(id=uid)
    except:
        return HttpResponse('笔记编号错误!')
    note.delete()
    return HttpResponseRedirect('/note')
