# Generated by Django 3.0.3 on 2021-10-09 08:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Candidate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userid', models.IntegerField(blank=True, null=True, unique=True, verbose_name='应聘者ID')),
                ('username', models.CharField(max_length=135, verbose_name='姓名')),
                ('city', models.CharField(max_length=135, verbose_name='城市')),
                ('phone', models.CharField(max_length=135, verbose_name='手机号码')),
                ('email', models.EmailField(blank=True, max_length=135, verbose_name='邮箱')),
                ('apply_position', models.CharField(blank=True, max_length=135, verbose_name='应聘职位')),
                ('born_address', models.CharField(blank=True, max_length=135, verbose_name='生源地')),
                ('gender', models.CharField(blank=True, max_length=135, verbose_name='性别')),
                ('candidate_remark', models.CharField(blank=True, max_length=135, verbose_name='候选人信息备注')),
                ('bachelor_school', models.CharField(blank=True, max_length=135, verbose_name='本科学校')),
                ('master_school', models.CharField(blank=True, max_length=135, verbose_name='研究生学校')),
                ('doctor_school', models.CharField(blank=True, max_length=135, verbose_name='博士生学校')),
                ('major', models.CharField(blank=True, max_length=135, verbose_name='专业')),
                ('degree', models.CharField(blank=True, choices=[('本科', '本科'), ('硕士', '硕士'), ('博士', '博士')], max_length=135, verbose_name='学历')),
                ('test_score_of_general_ability', models.DecimalField(blank=True, decimal_places=1, max_digits=3, null=True, verbose_name='综合能力测评成绩')),
                ('paper_score', models.DecimalField(blank=True, decimal_places=1, max_digits=3, null=True, verbose_name='笔试成绩')),
                ('first_score', models.DecimalField(blank=True, decimal_places=1, help_text='1-5分，极优秀: >=4.5，优秀: 4-4.4，良好: 3.5-3.9，一般: 3-3.4，较差: <3分', max_digits=2, null=True, verbose_name='初试分')),
                ('first_learning_ability', models.DecimalField(blank=True, decimal_places=1, max_digits=2, null=True, verbose_name='学习能力得分')),
                ('first_professional_competency', models.DecimalField(blank=True, decimal_places=1, max_digits=2, null=True, verbose_name='专业能力得分')),
                ('first_advantage', models.TextField(blank=True, max_length=1024, verbose_name='优势')),
                ('first_disadvantage', models.TextField(blank=True, max_length=1024, verbose_name='顾虑和不足')),
                ('first_result', models.CharField(blank=True, choices=[('建议复试', '建议复试'), ('待定', '待定'), ('放弃', '放弃')], max_length=256, verbose_name='初试结果')),
                ('first_recommend_position', models.CharField(blank=True, max_length=256, verbose_name='推荐部门')),
                ('first_remark', models.CharField(blank=True, max_length=135, verbose_name='初试备注')),
                ('second_score', models.DecimalField(blank=True, decimal_places=1, help_text='1-5分，极优秀: >=4.5，优秀: 4-4.4，良好: 3.5-3.9，一般: 3-3.4，较差: <3分', max_digits=2, null=True, verbose_name='专业复试得分')),
                ('second_learning_ability', models.DecimalField(blank=True, decimal_places=1, max_digits=2, null=True, verbose_name='学习能力得分')),
                ('second_professional_competency', models.DecimalField(blank=True, decimal_places=1, max_digits=2, null=True, verbose_name='专业能力得分')),
                ('second_pursue_of_excellence', models.DecimalField(blank=True, decimal_places=1, max_digits=2, null=True, verbose_name='追求卓越得分')),
                ('second_communication_ability', models.DecimalField(blank=True, decimal_places=1, max_digits=2, null=True, verbose_name='沟通能力得分')),
                ('second_pressure_score', models.DecimalField(blank=True, decimal_places=1, max_digits=2, null=True, verbose_name='抗压能力得分')),
                ('second_advantage', models.TextField(blank=True, max_length=1024, verbose_name='优势')),
                ('second_disadvantage', models.TextField(blank=True, max_length=1024, verbose_name='顾虑和不足')),
                ('second_result', models.CharField(blank=True, choices=[('建议录用', '建议录用'), ('待定', '待定'), ('放弃', '放弃')], max_length=256, verbose_name='专业复试结果')),
                ('second_recommend_position', models.CharField(blank=True, max_length=256, verbose_name='建议方向或推荐部门')),
                ('second_remark', models.CharField(blank=True, max_length=135, verbose_name='专业复试备注')),
                ('hr_score', models.CharField(blank=True, choices=[('S', 'S'), ('A', 'A'), ('B', 'B'), ('C', 'C')], max_length=10, verbose_name='HR复试综合等级')),
                ('hr_responsibility', models.CharField(blank=True, choices=[('S', 'S'), ('A', 'A'), ('B', 'B'), ('C', 'C')], max_length=10, verbose_name='HR责任心')),
                ('hr_communication_ability', models.CharField(blank=True, choices=[('S', 'S'), ('A', 'A'), ('B', 'B'), ('C', 'C')], max_length=10, verbose_name='HR坦诚沟通')),
                ('hr_logic_ability', models.CharField(blank=True, choices=[('S', 'S'), ('A', 'A'), ('B', 'B'), ('C', 'C')], max_length=10, verbose_name='HR逻辑思维')),
                ('hr_potential', models.CharField(blank=True, choices=[('S', 'S'), ('A', 'A'), ('B', 'B'), ('C', 'C')], max_length=10, verbose_name='HR发展潜力')),
                ('hr_stability', models.CharField(blank=True, choices=[('S', 'S'), ('A', 'A'), ('B', 'B'), ('C', 'C')], max_length=10, verbose_name='HR稳定性')),
                ('hr_advantage', models.TextField(blank=True, max_length=1024, verbose_name='优势')),
                ('hr_disadvantage', models.TextField(blank=True, max_length=1024, verbose_name='顾虑和不足')),
                ('hr_result', models.CharField(blank=True, choices=[('建议录用', '建议录用'), ('待定', '待定'), ('放弃', '放弃')], max_length=256, verbose_name='HR复试结果')),
                ('hr_remark', models.CharField(blank=True, max_length=256, verbose_name='HR复试备注')),
                ('creator', models.CharField(blank=True, max_length=256, verbose_name='候选人数据的创建人')),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('modified_date', models.DateTimeField(auto_now=True, null=True, verbose_name='更新时间')),
                ('last_editor', models.CharField(blank=True, max_length=256, verbose_name='最后编辑者')),
                ('first_interviewer_user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='first_interviewer_user', to=settings.AUTH_USER_MODEL, verbose_name='面试官')),
                ('hr_interviewer_user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='hr_interviewer_user', to=settings.AUTH_USER_MODEL, verbose_name='HR面试官')),
                ('second_interviewer_user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='second_interviewer_user', to=settings.AUTH_USER_MODEL, verbose_name='二面面试官')),
            ],
            options={
                'verbose_name': '应聘者',
                'verbose_name_plural': '应聘者',
                'db_table': 'candidate',
                'permissions': [('export', 'Can export candidate list'), ('notify', 'notify interviewer for candidate review')],
            },
        ),
    ]
