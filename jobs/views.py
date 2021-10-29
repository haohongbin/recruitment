from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.template import loader
from django.http import Http404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView
from django.http import HttpResponseRedirect
from django.views.generic.detail import DetailView



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