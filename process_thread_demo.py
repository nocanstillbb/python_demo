#GIL 全局解释器锁, Python进程中,同一时间只能有一个线程在执行python代码,所以如果需要并发,通常需要开多个进程
#process
from multiprocessing import Process
import os
import time

#def myprocesses_main():
#    for i in range(3):
#        time.sleep(1)
#
#processes_num = os.cpu_count()
#processes = []
##创建cpu数量的进程
#
#if __name__ == "__main__": #因为子进程会import 主模块,所以需要加上这个if防止子进程递归创建process
#    for i in range(processes_num):
#        p = Process(target=myprocesses_main)
#        processes.append(p)
#
#    #启动进程们
#    for p in processes:
#        p.start()
#
#    #等待线程结束
#    for p in processes:
#        p.join()
#
#    print("运行结束")
#
#



# threads
from threading import Thread

threads = []
threads_num = 4

def thread_main():
    for i in range(3):
        time.sleep(1)

for i in range(threads_num):
    t = Thread(target=thread_main)
    threads.append(t)

for t in threads:
    t.start();

for t in threads:
    t.join();

print("threads end")