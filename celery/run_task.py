#coding = utf-8

from tasks import add

result = add.delay(4, 4) # 调用任务
print('Is task ready: %s' % result.ready()) # ready()方法返回任务是否已完成处理

run_result = result.get(timeout=1)
print('task result: %s' % run_result)