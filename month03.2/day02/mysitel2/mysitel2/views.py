from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader

html = '''
<form method='get' action="/test_get?a=100&b=100&a=300">
    <p>
        姓名:<input type="text" name="uname">
    </p>
    <p>
        <input type = 'submit' value = '提交'>
    </p>
</form>
'''

html2 = '''
<form method='post' action="/test_post">
    <p>
        姓名:<input type="text" name="uname">
    </p>
    <p>
        <input type = 'submit' value = '提交'>
    </p>
</form>
'''


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def showData(self):
        return 'name:%s,age:%s' % (self.name, self.age)


def test_get(request):
    # 后端收到客户端提交的查询字符串打印
    # 要求查询字符串中存在名称为uname的数据，如果没有则报错
    # uname = request.GET('uname')

    # 换一种方式获取，试着获取，没有也不报错，值为None
    # uname = request.GET.get('uname')
    # 3.试着获取，有值拿值，没有值，使用默认值
    uname = request.GET.get('uname', '无')

    print(uname)

    # 4.
    print(request.GET.getlist('a'))

    return HttpResponse(html)


def test_post(request):
    if request.method == 'GET':
        return HttpResponse(html2)
    elif request.method == 'POST':
        # 与GET类似，也有
        # request.POST.get('uname',默认值)
        # request.POST.getlist(表单元素名称)
        uname = request.POST['uname']
        return HttpResponse('欢迎您%s' % uname)


def birthday(request):
    year = request.GET.get('year')
    month = request.GET.get('month')
    day = request.GET.get('day')
    return HttpResponse(f'你的生日为{year}年{month}月{day}日')

def Hello():
    return '北京欢迎你'

def test_html(request):
    # 方式一
    # t = loader.get_template('test_html.html')
    # html = t.render()
    # return HttpResponse(html)
    # 方式二
    # dict1 = {}
    # dict1['name'] = 'aid2010'
    # dict1['count'] = 450
    # dict1['citys'] = ['北京', '上海', '杭州']
    # dict1['distr'] = {'北京': 150, '上海': 200, '杭州': 100}
    # dict1['p1'] = Person('佟大为', 40)
    # dict1['function1'] = Hello
    # dict1['script'] = '<script>alert("Hello World")</script>'
    # return render(request, 'test_html.html', dict1)

    #方式三[推荐的方式]
    name = 'aid2010,we are family'
    count = 450
    citys = ['北京', '上海', '杭州']
    distr = {'北京': 150, '上海': 200, '杭州': 100}
    p1 = Person('佟大为', 40)
    function1 = Hello
    script = '<script>alert("Hello World")</script>'
    persons = ['关羽','张飞','赵云','马超','黄忠']
    persons = []
    return render(request, 'test_html.html', locals())

def test_calc(request):
    if request.method == 'GET':
        return render(request,'test_calc.html')
    elif request.method == 'POST':
        x = request.POST['x']
        y = request.POST['y']
        op = request.POST["op"]
        #为空判断
        if not x or not y:
            return HttpResponse("请输入数据")
        try:
            x = int(x)
            y = int(y)
        except:
            return HttpResponse('请输入整数值')
        result = 0
        if op == 'add':
            result = x + y
        elif op == 'sub':
            result = x - y
        elif op == 'mul':
            result = x * y
        elif op == 'div':
            result = x / y
        return render(request,'test_calc.html',locals())