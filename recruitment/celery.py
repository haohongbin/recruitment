from __future__ import absolute_import, unicode_literals

import os

from celery import Celery, shared_task

# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings.base')

app = Celery('recruitment')

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='CELERY') # 在配置文件中需要以CELERY开头

# Load task modules from all registered Django app configs.
app.autodiscover_tasks()


@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))

from celery.schedules import crontab

@app.on_after_configure.connect # 系统启动完成之后，再去执行此方法
def setup_periodic_tasks(sender, **kwargs):
    # Calls test('hello') every 10 seconds.
    # 添加定时任务，每10秒运行一次
    sender.add_periodic_task(10.0, test.s('hello'), name='hello every 10')

    # Calls test('world') every 30 seconds
    sender.add_periodic_task(30.0, test.s('world'), expires=10)

    # Executes every Monday morning at 7:30 a.m.
    sender.add_periodic_task(
        crontab(hour=7, minute=30, day_of_week=1),
        test.s('Happy Mondays!'),
    )

@app.task
def test(arg):
    print(arg)


from recruitment.tasks import add

app.conf.beat_schedule = {
    'add-every-10-seconds': {
        'task': 'recruitment.tasks.add',
        'schedule': 10.0,
        'args': (16, 4, )
    },
}

# import json
# # 导入定时任务的类
# from django_celery_beat.models import PeriodicTask, IntervalSchedule
#
# # 先创建定时策略 每隔10秒运行一次的任务
# schedule, created = IntervalSchedule.objects.get_or_create(every=10,period=IntervalSchedule.SECONDS,)
#
# # 再创建任务 PeriodicTask的model来创建一个对象
# # name 任务的名称  task 要执行的方法  json格式的参数
# task = PeriodicTask.objects.create(interval=schedule, name='say welcome 2021-01', task='recruitment.celery.test', args=json.dumps(['welcome']))

@app.task
def test(arg):
    print(arg)

app.conf.timezone = "Asia/Shanghai"