import time,sys,queue
from multiprocessing.managers import BaseManager

# task_worker.py


# 创建类似的QueueManager
class QueueManager(BaseManager):
    pass

# 由于这个QueueManager只从网络上获取queue，所以注册时只提供名字
QueueManager.register("get_task_queue")
QueueManager.register("get_result_queue")

# 连接到服务器，即运行task_manager.py的机器
server_ip = '127.0.0.1'
print("Connect to server %s" % server_ip)

# 端口和验证码注意要和task_manager.py注册的一致
m = QueueManager(address=(server_ip, 5000), authkey=b'abc')
# 从网络连接
m.connect()

# 获取queue对象
task = m.get_task_queue()
result = m.get_result_queue()

# 从task队列取任务并把结果写入result队列
for i in range(10):
    try:
        n = task.get(timeout=10)
        print("Run task %d * %d" % (n, n))
        r = '%d * %d = %d' % (n, n, n*n)
        time.sleep(1)
        result.put(r)
    except queue.Empty:
        print("Queue is empty.")

# 处理结束
print("worker exit...")
