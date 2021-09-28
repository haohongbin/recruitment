from django.conf.urls import url
from django.urls import path
from jobs import views

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

]