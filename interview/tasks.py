from __future__ import absolute_import, unicode_literals # 避免我们导入的包有命名冲突

from celery import shared_task 
from .dingtalk import send

# 该@shared_task装饰可以让你无需任何具体的应用程序实例创建任务
@shared_task
def send_dingtalk_message(message):
    send(message)