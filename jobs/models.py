from django.db import models
from django.contrib.auth.models import User

# Create your models here.

# 候选人学历
DEGREE_TYPE = ((u'本科', u'本科'), (u'硕士', u'硕士'), (u'博士', u'博士'))

JobTypes = [
    (0,"技术类"),
    (1,"产品类"),
    (2,"运营类"),
    (3,"设计类"),
    (4,"市场营销类")
]

Cities = [
    (0,"北京"),
    (1,"上海"),
    (2,"深圳"),
    (3,"杭州"),
    (4,"广州")
]

class Job(models.Model):
    job_type = models.SmallIntegerField(blank=False, choices=JobTypes, verbose_name="职位类别") # blank=False 字段不能为空
    job_name = models.CharField(max_length=250, blank=False, verbose_name="职位名称")
    job_city = models.SmallIntegerField(choices=Cities, blank=False, verbose_name="工作地点")
    job_responsibility = models.TextField(max_length=1024, verbose_name="职位职责")
    job_requirement = models.TextField(max_length=1024, blank=False, verbose_name="职位要求")
    # creator是User的外键引用,删除数据外键关联处理（on_delete=models.SET_NULL）
    creator = models.ForeignKey(User, verbose_name="创建人", null=True, on_delete=models.SET_NULL)
    # 创建日期，使用 auto_now_add ，可以自动在创建时指定当前时间并使用了默认时区
    created_date = models.DateTimeField(verbose_name="创建日期", auto_now_add=True)
    # 修改日期，使用 auto_now，可以自动在模型保存时更新时间并使用了默认时区
    modified_date = models.DateTimeField(verbose_name="修改日期", auto_now=True)

    class Meta:
        verbose_name = '职位' # 给你的模型类起一个更可读的名字一般定义为中文
        verbose_name_plural = '职位列表' #这个选项是指定，模型的复数形式是什么，如果不指定Django会自动在模型名称后加一个’s’

    def __str__(self):
        return self.job_name