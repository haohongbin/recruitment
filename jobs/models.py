from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
from django.utils.translation import gettext_lazy as _ # gettext_lazy 获取多语言资源对应的文本内容


# Create your models here.

# 候选人学历
DEGREE_TYPE = (('本科', '本科'), ('硕士', '硕士'), ('博士', '博士'))

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
    # _("职位类别") 以职位类别key作为函数的入参，去取到这个key对应的多语言的资源
    job_type = models.SmallIntegerField(blank=False, choices=JobTypes, verbose_name=_("职位类别")) # blank=False 字段不能为空
    job_name = models.CharField(max_length=250, blank=False, verbose_name=_("职位名称"))
    job_city = models.SmallIntegerField(choices=Cities, blank=False, verbose_name=_("工作地点"))
    job_responsibility = models.TextField(max_length=1024, verbose_name=_("职位职责"))
    job_requirement = models.TextField(max_length=1024, blank=False, verbose_name=_("职位要求"))
    # creator是User的外键引用,删除数据外键关联处理（on_delete=models.SET_NULL）
    creator = models.ForeignKey(User, verbose_name=_("创建人"), null=True, on_delete=models.SET_NULL)
    # 创建日期，使用 auto_now_add ，可以自动在创建时指定当前时间并使用了默认时区
    created_date = models.DateTimeField(verbose_name=_("创建日期"), auto_now_add=True)
    # 修改日期，使用 auto_now，可以自动在模型保存时更新时间并使用了默认时区
    modified_date = models.DateTimeField(verbose_name=_("修改日期"), auto_now=True)

    class Meta:
        verbose_name = _('职位') # 给你的模型类起一个更可读的名字一般定义为中文
        verbose_name_plural = _('职位列表') #这个选项是指定，模型的复数形式是什么，如果不指定Django会自动在模型名称后加一个’s’

    def __str__(self):
        return self.job_name


class Resume(models.Model):
    # Translators: 简历实体的翻译
    username = models.CharField(max_length=135, verbose_name=_('姓名'))
    applicant = models.ForeignKey(User, verbose_name=_("申请人"), null=True, on_delete=models.SET_NULL)
    city = models.CharField(max_length=135, verbose_name=_('城市'))
    phone = models.CharField(max_length=135, verbose_name=_('手机号码'))
    email = models.EmailField(max_length=135, blank=True, verbose_name=_('邮箱'))
    apply_position = models.CharField(max_length=135, blank=True, verbose_name=_('应聘职位'))
    born_address = models.CharField(max_length=135, blank=True, verbose_name=_('生源地'))
    gender = models.CharField(max_length=135, blank=True, verbose_name=_('性别'))

    # 上传文件和图片
    picture = models.ImageField(upload_to='images/', blank=True, verbose_name=_('个人照片'))
    attachment = models.FileField(upload_to='file/', blank=True, verbose_name=_('简历附件'))

    # 学校与学历信息
    bachelor_school = models.CharField(max_length=135, blank=True, verbose_name=_('本科学校'))
    master_school = models.CharField(max_length=135, blank=True, verbose_name=_('研究生学校'))
    doctor_school = models.CharField(max_length=135, blank=True, verbose_name=_('博士生学校'))
    major = models.CharField(max_length=135, blank=True, verbose_name=_('专业'))
    degree = models.CharField(max_length=135, choices=DEGREE_TYPE, blank=True, verbose_name=_('学历'))
    created_date = models.DateTimeField(verbose_name=_("创建日期"), default=datetime.now)
    modified_date = models.DateTimeField(verbose_name=_("修改日期"), auto_now=True)

    # 候选人自我介绍，工作经历，项目经历
    candidate_introduction = models.TextField(max_length=1024, blank=True, verbose_name=_('自我介绍'))
    work_experience = models.TextField(max_length=1024, blank=True, verbose_name=_('工作经历'))
    project_experience = models.TextField(max_length=1024, blank=True, verbose_name=_('项目经历'))

    class Meta:
        verbose_name = _('简历')
        verbose_name_plural = _('简历列表')

    def __str__(self):
        return self.username
