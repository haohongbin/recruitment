"""recruitment URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import include, url
from django.utils.translation import gettext_lazy as _

urlpatterns = [
    # url(r"^", include("jobs.urls")), # 路径映射，用include指令来引用我们jobs应用里面定义的所有的路径
    path("", include("jobs.urls")),
    path('admin/', admin.site.urls),
]

admin.site.site_header = _('**科技招聘管理系统')