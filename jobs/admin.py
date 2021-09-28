from django.contrib import admin
from jobs.models import Job
# Register your models here.

"""
admin中定制我们的管理的属性
管理类
"""
class JobAdmin(admin.ModelAdmin):
    # 将详情属性隐藏
    exclude = ('creator','created_date','modified_date')
    # 列表页展示哪些字段 list_display是ModelAdmin中定义的有特定含义的属性
    list_display = ('job_name','job_type','job_city','creator','created_date','modified_date')

    # save_model会被自动调用
    def save_model(self, request, obj, form, change):
        obj.creator = request.user # 创建人设置为当前登录用户
        super().save_model(request,obj,form,change) # 保存对象

admin.site.register(Job, JobAdmin)