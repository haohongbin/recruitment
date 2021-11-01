from django.contrib.auth.decorators import permission_required
from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.template import loader
from django.http import Http404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView
from django.http import HttpResponseRedirect
from django.views.generic.detail import DetailView
from django.contrib.auth.models import User, Group
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages

from jobs.models import Job, Resume
from jobs.models import Cities, JobTypes

"""
在views里面指定每个url使用哪个模版来渲染页面
把joblist视图注册到我们的URL路径里面
"""
def joblist(request):
    job_list = Job.objects.order_by('job_type')
    # 用模版的加载器来加载模版
    # template = loader.get_template('joblist.html')
    # 定义上下文
    context = {'job_list':job_list}

    for job in job_list:
        job.city_name = Cities[job.job_city][1]
        job.type_name = JobTypes[job.job_type][1]
    # 用模版对象的render方法把上下文展现给用户
    # return HttpResponse(template.render(context))
    return render(request, 'joblist.html', context)

def detail(request, job_id):
    try:
        job = Job.objects.get(pk=job_id)
        job.city_name = Cities[job.job_city][1]
    except Job.DoesNotExist:
        raise Http404("Job does not exist")

    context = {'job':job}
    return render(request, 'job.html', context)


class ResumeCreateView(LoginRequiredMixin, CreateView):
    """
    简历职位页面
    因为类继承只能继承一个父类，Mixin可以达到让一个类能够继承多个类的目的
    """
    template_name = 'resume_form.html'
    success_url = '/joblist/'
    model = Resume
    fields = ["username", "city", "phone",
        "email", "apply_position", "gender",
        "bachelor_school", "master_school", "major", "degree", "picture", "attachment",
        "candidate_introduction", "work_experience", "project_experience"]

    # 从 URL 请求参数带入默认值
    def get_initial(self):
        initial = {}
        for x in self.request.GET:
            initial[x] = self.request.GET[x]
        return initial

    # 简历与当前用户关联
    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.applicant = self.request.user
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())


class ResumeDetailView(DetailView):
    """   简历详情页    """
    model = Resume
    template_name = 'resume_detail.html'


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


# 这个 URL 仅允许有 创建用户权限的用户访问
# @csrf_exempt # 这个标记表示这个视图不去处理CSRF的攻击
@permission_required('auth.user_add')
def create_hr_user(request):
    if request.method == "GET":
        return render(request, 'create_hr.html', {})
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        hr_group = Group.objects.get(name='hr')
        # 创建用户，不是管理员，设置active为活跃的，is_staff为True是员工可以登录管理后台
        user = User(is_superuser=False, username=username, is_active=True, is_staff=True)
        user.set_password(password)
        user.save()
        user.groups.add(hr_group)

        messages.add_message(request, messages.INFO, 'user created %s' % username)
        return render(request, 'create_hr.html')
    return render(request, 'create_hr.html')