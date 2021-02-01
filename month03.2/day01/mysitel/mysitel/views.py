from django.http import HttpResponse


# 视图函数
# 参数为请求对象
# 返回值为响应对象
def page_2003(request):
    return HttpResponse('这是编号为2003的页面')


def page_2004(request):
    return HttpResponse('这是编号为2004的页面')


def page_index(request):
    return HttpResponse('<h1>Hello World</h1>')


def page_num(request, num):
    return HttpResponse('path转换器：这是编号为%s页面' % num)


def page_data(request, data):
    return HttpResponse('data:%s' % data)


def page_path(request, data):
    return HttpResponse('path:%s' % data)


def add_100(request, num1, num2, op):
    if op not in ['add', 'sub', 'mul']:
        return HttpResponse('运算符有误')
    result = 0
    if op == 'add':
        result = num1 + num2
    elif op == 'sub':
        result = num1 - num2
    elif op == 'mul':
        result = num1 * num2

    # 测试request对象的使用，从request对象中获取信息
    print(request.method)
    print(request.path_info)

    return HttpResponse('计算结果为%s' % result)


def birthday_view(request, y, m, d):
    return HttpResponse(f' 生日为: {y}年{m}月{d}日')
