from django.contrib import admin
from interview.models import Candidate
from django.http import HttpResponse
import csv
from datetime import datetime
import logging
# Register your models here.

logger = logging.getLogger(__name__)

exportable_fields = ('username', 'city', 'phone', 'bachelor_school', 'master_school', 'degree', 'first_result', 'first_interviewer_user',
                     'second_result', 'second_interviewer_user', 'hr_result', 'hr_score', 'hr_remark', 'hr_interviewer_user')

def export_model_as_csv(modeladmin, request, queryset):
    """
    导出函数
    :param modeladmin:
    :param request: 用户发起的请求
    :param queryset: 用户列表选择的结果列表里面的数据集合
    :return:
    """
    response = HttpResponse(content_type='text/csv') #返回类型
    field_list = exportable_fields
    response['Content-Disposition'] = 'attachment; filename=%s-list-%s.csv' % (
        'recruitment-candidates',
        datetime.now().strftime('%Y-%m-%d-%H-%M-%S'),
    )
    # 写入表头
    writer = csv.writer(response)
    # 每个字段对应的中文名作为我们导出文件里面的表头
    writer.writerow(
        [queryset.model._meta.get_field(f).verbose_name.title() for f in field_list],
    )
    for obj in queryset:
        ## 单行的记录（各个字段的值），根据字段对象，从当前实例 (obj) 中获取字段值
        csv_line_values = []
        for field in field_list:
            field_object = queryset.model._meta.get_field(field)
            field_value = field_object.value_from_object(obj)
            csv_line_values.append(field_value)
        writer.writerow(csv_line_values)

    logger.info(" %s has exported %s candidate records" % (request.user.username, len(queryset)))
    return response
# 菜单名字定制。设置它的属性
export_model_as_csv.short_description = u'导出为CSV文件'

class CandidateAdmin(admin.ModelAdmin):
    # 导出函数注册到admin的actions里面
    actions = [export_model_as_csv]
    exclude = ('creator', 'created_date', 'modified_date')
    list_display = (
        'username', 'city', 'bachelor_school', 'first_score', 'first_result', 'first_interviewer_user',
        'second_score',
        'second_result', 'second_interviewer_user', 'hr_score', 'hr_result', 'hr_interviewer_user',)

    # 右侧筛选条件
    list_filter = (
    'city', 'first_result', 'second_result', 'hr_result', 'first_interviewer_user', 'second_interviewer_user',
    'hr_interviewer_user')

    # 查询字段
    search_fields = ('username', 'phone', 'email', 'bachelor_school')

    # 列表页排序字段
    ordering = ('hr_result', 'second_result', 'first_result',)

    # 页面字段分组展示 ("username", "city", "phone")会展示为一行
    fieldsets = (
        (None, {'fields': ("userid", ("username", "city", "phone"), ("email", "apply_position", "born_address", "gender"), ("candidate_remark", "bachelor_school", "master_school", "doctor_school"), ("major", "degree", "test_score_of_general_ability", "paper_score", "last_editor"))}),
        ('第一轮面试记录', {'fields': ("first_score", "first_learning_ability", "first_professional_competency", "first_advantage", "first_disadvantage", "first_result", "first_recommend_position", "first_interviewer_user", "first_remark")}),
        ('第二轮面试记录', {'fields': ("second_score", "second_learning_ability", "second_professional_competency", "second_pursue_of_excellence", "second_communication_ability", "second_pressure_score", "second_advantage", "second_disadvantage", "second_result", "second_recommend_position", "second_interviewer_user", "second_remark")}),
        ('HR复试记录', {'fields': ("hr_score", "hr_responsibility", "hr_communication_ability", "hr_logic_ability", "hr_potential", "hr_stability", "hr_advantage", "hr_disadvantage", "hr_result", "hr_interviewer_user", "hr_remark")}),
    )


admin.site.register(Candidate, CandidateAdmin)