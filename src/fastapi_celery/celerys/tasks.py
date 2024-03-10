from fastapi_celery.celerys.celery import app
import time
@app.task
def add(n, m):
    print(n)
    print(m)
    time.sleep(10)
    print('n+m的结果：%s' % (n + m))
    return n + m

@app.task
def low(n, m):
    print(n)
    print(m)
    print('n-m的结果：%s' % (n - m))
    return n - m