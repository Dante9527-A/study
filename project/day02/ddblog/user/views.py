from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

# Create your views here.
from django.views import View
from .models import UserProfile
import json


class UserView(View):
    # 处理 v1/users的 GET 请求
    def get(self, request):
        return HttpResponse('-user get-')

    # 处理 v1/users的 POST 请求
    def post(self, request):
        # 1.获取前端给后端的json串
        json_str = request.body
        # 2.把json串反序列化为对象
        json_obj = json.loads(json_str)
        # 3.从对象【字典】中获取数据
        username = json_obj['username']
        email = json_obj['email']
        phone = json_obj['phone']
        password_1 = json_obj['password_1']
        password_2 = json_obj['password_2']
        # 4 数据检查
        # 4.1 检查注册的用户名是否可以使用
        old_user = UserProfile.objects.filter(username=username)
        if old_user:
            result = {'code': 10100, 'error': '用户名已注册'}
            return JsonResponse(result)
        # 4.2 两次密码是否一致
        if password_1 != password_2:
            result = {'code': 10101, 'error': '两次密码不一致'}
            return JsonResponse(result)
        # 4.3 添加密码的hash值

        # 4.4 插入数据【仍然需要try】

        return JsonResponse({'code': 200})