// 外部js文件
$(function () {
    // 当页面元素加载完成之后执行的JS代码
    // alert('外部JS文件加载完成');
    // // 测试外部数据加载
    console.log(blogData);
    console.log(faderData);
    // 使用faderData在页面加载所有的轮播图

    // 声明本地图片路径
    // 图片路径通常随着项目的位置发生变化 对于路径而言尽量不要写死图片路径 通常采用地址+图片名的方式拼接路径 这样项目位置改变只需要改变图片地址 不需要修改代码
    // var BASE_URL = 'http://127.0.0.1:8000/'
    var BASE_URL = '../static/images/';
    var html = '';
    // 遍历faderData 生成三个li标签拼接到字符串html中
    // 打印字符串
    // <li class="slide">
    //     <a href="#">
    //         <img src="../static/images/banner01.jpg" alt="banner1">
    //         <span class="imginfo">
    //             爬虫微课5小时 Python 学习路线!
    //         </span>
    //     </a>
    // </li>
    $.each(faderData, function (i, o) {
        html += '<li class="slide">';
        html += '<a href="#">'
        html += `<img src="${BASE_URL + o.img_url}" alt="">`
        html += '<span class="imginfo">';
        html += o.img_info;
        html += '</span></a></li>'
    })
    console.log(html);
    // 将拼接好的字符串作为兄弟元素添加到fader_controls前
    $('.fader_controls').before(html);

    // jquery-->easyfader-->index.js
    // 调用jQuery.easyfader.min.js提供的函数 实现轮播功能
    $('.fader').easyFader();


    // 加载页面中的博客 
    // 当页面加载时 显示前3条数据  每次滚动时如果滚动条快要到底了再加载5条数据 直到没有数据为止 
    function add_blogs(data) {
        var html = '';
        $.each(data, function (i, o) {
            var blog = `
            <div class="blogs">
                <h3 class="blogtitle">
                    <a href="#">
                        ${o.blogtitle}
                    </a>
                </h3>
                <div class="blogpic">
                    <a href="#">
                        <img src="${BASE_URL+o.blogpic}" alt="">
                    </a>
                </div>
                <p class="blogtext">
                   ${o.blogtext}
                </p>
                <ul>
                    <li class="author">
                        <a href="#">${o.bloginfo.author}</a>
                    </li>
                    <li class="lmname">
                        <a href="#">${o.bloginfo.lmname}</a>
                    </li>
                    <li class="timer">
                        <a href="#">${o.bloginfo.timer}</a>
                    </li>
                    <li class="view">
                        <a href="#">${o.bloginfo.view}</a>
                    </li>
                    <li class="like">
                        <a href="#">${o.bloginfo.like}</a>
                    </li>
                </ul>
            </div>
            `
            html += blog
        })//each结束
        // 将拼接好的字符串追加到页面
        $('.blogsbox').append(html)
    }

    // 当页面加载时 显示blogData前3条数据
    add_blogs(blogData.slice(0,3));

    var canLoad = true;//判读是否可以加载数据
    $(document).scroll(function(){  
        var scrollTop = $(document).scrollTop()
        var windowHeight = $(window).height()
        var documentHeight = $(document).height()
        if(documentHeight-scrollTop-windowHeight<=200){
            // console.log('快突破底线了')
            // 获取后面 5条数据
            // 页面中3条 slice(3,8)  [3:8]
            // 页面中8条 slice(8,13) [8:13]
            // 页面中n条 slice(n,n+5)
            // .blogs表示一条博客 获取.blogs的数量得知当前页面有几条博客 然后再取后5条
            var size = $('.blogs').length;
            if(canLoad){
                var data = blogData.slice(size,size+5);
                if (data.length>0){
                    add_blogs(data)
                }else{
                    alert('没数据了')
                    canLoad = false//没有数据后就禁止加载
                }
            }
        }

    })


})