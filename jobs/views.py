from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.template import loader
from django.http import Http404

from jobs.models import Job
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

