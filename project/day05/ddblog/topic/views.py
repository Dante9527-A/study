from django.http import JsonResponse
from django.shortcuts import render
from django.utils.decorators import method_decorator

from tools.login_dec import login_check
from django.views import View
import json

# Create your views here.
from .models import Topic
from user.models import UserProfile

class TopicView(View):
    @method_decorator(login_check)
    def post(self,request,author_id):
        # 1 从请求对象的附加数据中获取用户对象
        author = request.myuser
        # 2 从前端获取用户输入的值（内容，不带格式的内容，权限，分类，标题）
        json_str = request.body
        json_obj = json.loads(json_str)
        content = json_obj['content']
        content_text = json_obj['content_text']
        introduce = content_text[:20]
        title = json_obj['title']
        # 3 检查分类的值一定是tec或no-tec
        category = json_obj['category']
        if category not in ['tec','no-tec']:
            result = {'code':10300,'error':'分类错误'}
            return JsonResponse(result)
        limit = json_obj['limit']
        # 4 检查权限的值一定是public或private
        if limit not in ['public','private']:
            result = {'code':10301,'error':'权限错误'}
            return JsonResponse(result)

        # 5 数据入库
        Topic.objects.create(title=title,
                             content=content,
                             limit=limit,
                             category=category,
                             introduce=introduce,
                             user_profile=author)

        # 6 返回
        return JsonResponse({'code':200,'username':author.username})

    def get(self,request,author_id):
        pass
        # 分类的思考
        # v1/topic/aid2010 # 所有的分类
        # v1/topic/aid2010?category=tec/no-etc # 技术或非技术文章

        # 2 权限的思考
        # 登录用户访问自己的文章，可以访问所有的文章（包括public+private）
        # 游客、等登录访问别的文章，只能访问public文章
        # 区分开访问者是不是作者本人

        # 1 获取文章的作者这个对象
        try:
            author = UserProfile.objects.get(username = author_id)
        except:
            result = {'code':10305,'error':'用户名错误！'}
            return JsonResponse(result)

        # 2 获取访问者的身份
        # 获取访问者的身份