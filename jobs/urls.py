from django.conf.urls import url
from django.urls import path
from jobs import views
from django.conf import settings


"""
这里只是在应用里面定义了url路径的映射，还需要在整个project的urls映射
"""
urlpatterns = [
    # 职位列表 把joblist视图注册到我们的URL路径里面 3.x建议用path
    # url(r"^joblist/", views.joblist, name="joblist"),
    path("joblist/", views.joblist, name="joblist"),
    # 职位详情
    # url(r'^job/(?P<job_id>\d+)/$', views.detail, name='detail'),
    path('job/<int:job_id>/', views.detail, name='detail'),
    # 首页自动跳转到职位列表
    path("", views.joblist, name="name"),
    # 提交简历
    path('resume/add/', views.ResumeCreateView.as_view(), name='resume-add'),
    path('resume/<int:pk>/', views.ResumeDetailView.as_view(), name='resume-detail'),

    # 管理员创建 HR 账号的 页面:
    path('create_hr_user/', views.create_hr_user, name='create_hr_user'),

]

if settings.DEBUG : # 生产环境不让访问
    # 有 XSS 漏洞的视图页面，
    urlpatterns += [url(r'^detail_resume/(?P<resume_id>\d+)/$', views.detail_resume, name='detail_resume'),]