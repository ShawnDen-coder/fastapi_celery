from fastapi_celery.celerys import tasks

# 添加立即执行任务(异步)
t1 = tasks.add.delay(10, 20)
t2 = tasks.low.delay(100, 50)
print(t1.id)    # 2d4ad592-9548-4c7c-8df4-7f8583e8a1b1


# # 添加延迟任务
# from datetime import datetime, timedelta
# # 需要utc时间
# eta=datetime.utcnow() + timedelta(seconds=10)  # 延迟10秒
# # eta=datetime.utcnow() + timedelta(days=1)  # 延迟1天
# ret = tasks.low.apply_async(args=(200, 50), eta=eta)   # 通过args向任务函数low中传递参数
# print(ret.id)    # 44bbf79c-0e34-41ed-a092-5d37e51d6cfa