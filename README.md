# Sentry集成

使用Docker安装sentry，使用release版本
https://github.com/getsentry/onpremise/releases
***
## docker安装 
***注意***:  
先安装docker服务  docker --version 验证是否安装成功  
docker镜像加速  ![](snapshot/Docker-Engine.png) 
***
## Sentry安装
下载：wget https://github.com/getsentry/onpremise/archive/refs/tags/21.8.0.zip  
解压：unzip 21.8.0.zip  
cd到解压后的文件夹，执行./install.sh

***注意***:  
在 Mac OS 执行 ./install.sh 遇到一些问题：
* 出错提示：realpath: command not found
原因：就是找不到 realpath 这个命令。
解决方法：需要安装coreutils。我用 brew，安装命令是： brew install coreutils
* 出错提示：FAIL: Required minimum RAM available to Docker is 3800 MB, found 1986 MB
原因：限制了 Docker 的内存使用。
解决方法：我用的是 docker.app，直接打开界面，设置里面 resource 的设置发现是 给 2GB内存给 Docker。修改为 大于 2GB即可。我设置了 5GB。

./install.sh 会把Sentry需要用到的各种容器的依赖，包括像Redis、Kafka、ClickHouse等不同的依赖的镜像，docker的Image镜像都下载下来，这样系统环境准备好了

添加账户：  
docker-compose run --rm web createuser --superuser --force-update  
superuser 表示创建管理员。  
force-update 表示覆盖存在的用户。
***
## 启动服务
docker-compose up -d  
启动完成之后，可以查看docker ps | less
***
## 访问
127.0.0.1:9000

1.创建Teams  
>![](snapshot/sentry-teams.png) 
2.创建Projects(propular为Django)
>![](snapshot/sentry-projects.png) 

创建完成之后，会有引导如何在Django中配置  
>![](snapshot/sentry-setting.png) 

***注意***：  
sentry下载的21.8.0的版本，使用的21.10.0版本时，捕获不到异常
***
## 捕获异常
访问url:http://127.0.0.1:8000/sentry-debug/即可在sentry中捕获到异常  
项目中可以使用error级别日志，也可以捕获到异常  
>![](snapshot/sentry-issues.png) 

### 通过类的方式实现性能记录跟异常捕获的中间件
当系统出现异常时，做两个事情：  
1.把这个异常通过capture_exception上报到Sentry  
2.异常发送钉钉群  


***
***
***
# XSS跨站脚本攻击
恶意攻击者将代码通过网站注入到其他用户浏览器中的攻击方式  
* 攻击者把恶意JavaScript代码作为普通数据放入到网站数据库中
* 其他用户在获取和展示数据的过程中，运行JavaScript代码
* JavaScript代码执行恶意代码（调用恶意请求，发送数据到攻击者等等）   

***示例***  
```python
'''
直接返回  HTML 内容的视图 （这段代码返回的页面有 XSS 漏洞，能够被攻击者利用）
'''
def detail_resume(request, resume_id):
    try:
        resume = Resume.objects.get(pk=resume_id)
        content = "name: %s <br>  introduction: %s <br>" % (resume.username, resume.candidate_introduction)
        return HttpResponse(content)
    except Resume.DoesNotExist:
        raise Http404("resume does not exist")
# 添加url
if settings.DEBUG : # 生产环境不让访问
    # 有 XSS 漏洞的视图页面，
    urlpatterns += [url(r'^detail_resume/(?P<resume_id>\d+)/$', views.detail_resume, name='detail_resume'),]
``` 
某用户（恶意攻击者）申请职位时，在自我介绍中，输入JavaScript代码，然后提交  
```javascript
<script>alert('page cookies:\n' + document.cookie);</script>
```

这样其他用户再通过该url访问恶意攻击者的简历详情时，就会执行JavaScript代码。如下图所示  
>![](snapshot/XSS-attack.png)
*** 
***如何防止?***  
这个视图函数与其他视图函数不同的地方，其他函数是通过render函数返回的，实际上这个模版渲染出来的时候，Django会自动把HTML的内容做转译，
所有的脚本都不会仔执行。所以这个函数自己返回html的时候，可以对它做一个转译。用html弱函数做转译，但是不建议。通常建议的做法是，直接使用系统自带的
render方法，用Django自带的模版的机制去渲染页面，这样能完全避免XSS的攻击（也可以使用通用视图，像简历详情一样）。  

简单点,使用html的escape方法进行转义：
```python
import html
def detail_resume(request, resume_id):
    try:
        resume = Resume.objects.get(pk=resume_id)
        content = "name: %s <br>  introduction: %s <br>" % (resume.username, resume.candidate_introduction)
        return HttpResponse(html.escape(content))
    except Resume.DoesNotExist:
        raise Http404("resume does not exist")
```





