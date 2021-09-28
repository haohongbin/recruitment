from django.conf.urls import url
from jobs import views

"""
这里只是在应用里面定义了url路径的映射，还需要在整个project的urls映射
"""
urlpatterns = [
    # 职位列表 把joblist视图注册到我们的URL路径里面
    url(r"^joblist/", views.joblist, name="joblist"),

]