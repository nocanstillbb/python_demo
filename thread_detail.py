import sys
import time
from threading import Thread,Lock
from queue import Queue

thread_num = 10
threads = [ ]

#l = Lock()
#value = 0
#
#def  thread_main():
#    global value
#    global l
#    with l: #取代 l.acquire() l.release()
#        local_value = value
#        local_value += 1
#        time.sleep(0.1)
#        local_value += 1
#        value = local_value
#
#
#
#for i in range(thread_num):
#    t = Thread(target=thread_main)# args需要传入元组
#    threads.append(t)
#
#for t in threads:
#    t.start()
#
#for t in threads:
#    t.join()
#
#
#print("程序运行结束,value",value)


#使用队列可以不需要用锁

from log import Logger
q = Queue()
logg = Logger()

def run_task_thread_main(q):
    while True:
        t = q.get() #如果q里没有任务,会阻塞
        logg.info(f"value : {t}")
        q.task_done()

for i in range(10) : #打开10个线程处理队列, 不需要锁
    t = Thread(target=run_task_thread_main,args=(q,))
    t.daemon = True #默认为false, 为true时进程结束时它会自动退出
    t.start()

for i in range(0,50):
    q.put(i)

q.join()


