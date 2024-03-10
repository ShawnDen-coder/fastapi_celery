from fastapi_celery.celerys.celery import app

from celery.result import AsyncResult

id = '6b4b49fb-5df5-4cf9-b95e-2bbdca5a2b64'
if __name__ == '__main__':
    async_ = AsyncResult(id=id, app=app)
    if async_.successful():
        result = async_.get()
        print(result)
    elif async_.failed():
        print('任务失败')
    elif async_.status == 'PENDING':
        print('任务等待中被执行')
    elif async_.status == 'RETRY':
        print('任务异常后正在重试')
    elif async_.status == 'STARTED':
        print('任务已经开始被执行')
