#!coding=utf-8

from celery import Celery

# 第一个参数 是当前脚本的名称，第二个参数 是 broker 服务地址
# 创建Celery的实例，名称叫做tasks
# backend 把每一个异步任务运行的结果，存储在什么地方。存储可以用redis也可以用数据库也可以用RPC的消息队列
# broker存储任务的系统，它的代理，也是一个消息队列，使用redis
app = Celery('tasks', backend='redis://127.0.0.1', broker='redis://127.0.0.1')


@app.task
def add(x, y):
    return x + y
