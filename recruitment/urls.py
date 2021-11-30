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

from django.urls import path
from rest_framework import routers, serializers, viewsets
from django.contrib.auth.models import User
from jobs.models import Job

# 定义实体序列化的方式，指定序列化返回哪些字段
# 然后再定义ViewSet视图的集合，展示哪些数据
# 最后把视图的集合注册到api列表里面
# Serializers define the API representation.
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'is_staff']

# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class JobSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Job
        fields = '__all__'


class JobViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Job.objects.all()
    serializer_class = JobSerializer


# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'jobs', JobViewSet)

def trigger_error(request):
    division_by_zero = 1 / 0

urlpatterns = [
    # url(r"^", include("jobs.urls")), # 路径映射，用include指令来引用我们jobs应用里面定义的所有的路径
    path("", include("jobs.urls")),
    path('grappelli/', include('grappelli.urls')), # grappelli URLS
    path('admin/', admin.site.urls),
    path('accounts/', include('registration.backends.simple.urls')),

    path('i18n/', include('django.conf.urls.i18n')), # 增加多语言的url路径支持

    path('sentry-debug/', trigger_error),

    # django rest api & api auth (login/logout)
    path('api/', include(router.urls)), # API访问的根路径
    path('api-auth/', include('rest_framework.urls')), # rest api管理后台里面的登录和退出的url路径前缀

]

from django.conf import settings
from django.conf.urls.static import static
if settings.DEBUG:
        #  document_root文档的路径，同时把它加到静态资源中去
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)


admin.site.site_header = _('**科技招聘管理系统')