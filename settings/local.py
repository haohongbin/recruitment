from .base import *

DEBUG = True

ALLOWED_HOSTS = ["127.0.0.1"]

## 务必修改以下值，确保运行时系统安全:
SECRET_KEY = "w$46bks+b3-7f(13#i%v@jwejrnxc$^^#@#@^t@fofizy1^mo9r8(-939243423300"

## 如果仅使用数据库中的账号，以下 LDAP 配置可忽略
## 替换这里的配置为正确的域服务器配置，同时可能需要修改 base.py 中的 LDAP 服务器相关配置:
LDAP_AUTH_URL = "ldap://xxxxx:389"
LDAP_AUTH_CONNECTION_USERNAME = "admin"
LDAP_AUTH_CONNECTION_PASSWORD = "your_admin_credentials"

INSTALLED_APPS += (
    # other apps for production site
)

# 缓存设置
CACHES  =  {
    "default" :  {
        "BACKEND" :  "django_redis.cache.RedisCache" ,
        "LOCATION" :  "redis://127.0.0.1:6379/1" ,
        'TIMEOUT': 60,
        "OPTIONS" :  {
            "CLIENT_CLASS" :  "django_redis.client.DefaultClient" ,
            "SOCKET_CONNECT_TIMEOUT": 5,  # redis连接的超时时间 秒
            "SOCKET_TIMEOUT": 5,  # 每次读写数据的超时时间 秒
            # 'PASSWORD': 'mysecret', # redis服务未设置密码，所以不需要
        }
    }
}

## 钉钉群的 WEB_HOOK， 用于发送钉钉消息
DINGTALK_WEB_HOOK = "https://oapi.dingtalk.com/robot/send?access_token=1e85e96073b2ba70d0e403f05b9fa20c7dce27a3e28b3ddcdc18c4edf02865a5"

# pip install --upgrade sentry-sdk
import sentry_sdk
from sentry_sdk.integrations.django import DjangoIntegration

sentry_sdk.init(
    dsn="http://252cba25520842eab719d87ffb1834c1@127.0.0.1:9000/4",
    integrations=[DjangoIntegration()],

    # Set traces_sample_rate to 1.0 to capture 100%
    # of transactions for performance monitoring.
    # We recommend adjusting this value in production.
    # performance tracing sample rate, 采样率, 生产环境访问量过大时，建议调小（不用每一个URL请求都记录性能）
    traces_sample_rate=1.0, # 日志采样率 1.0表示所有的请求都会做采样

    # If you wish to associate users to errors (assuming you are using
    # django.contrib.auth) you may enable sending PII data.
    send_default_pii=True # 是不是发送个人标识的信息。发送的话，在sentry中可以进行不同维度的聚类（用户名、浏览器、客户端版本、操作系统做聚类分析）
)


CELERY_BROKER_URL = 'redis://127.0.0.1:6379/0'
CELERY_RESULT_BACKEND = 'redis://127.0.0.1:6379/1'
CELERY_ACCEPT_CONTENT = ['application/json']
CELERY_RESULT_SERIALIZER = 'json'
CELERY_TASK_SERIALIZER = 'json'
CELERY_TIMEZONE = 'Asia/Shanghai'
CELERYD_MAX_TASKS_PER_CHILD = 10
CELERYD_LOG_FILE = os.path.join(BASE_DIR, "logs", "celery_work.log")
CELERYBEAT_LOG_FILE = os.path.join(BASE_DIR, "logs", "celery_beat.log")