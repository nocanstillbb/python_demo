from multiprocessing  import Process, Value, Array, Lock, Queue ,Pool
import time
import os
from log import Logger
import string

#processes = []
#processes_num = 50
#logger = Logger()
#
#def thread_main(shared_value,shared_array,lock):
#    with lock:
#        shared_value.value += 1
#        for i in range(len(shared_array)):
#            shared_array[i] +=1
#    logger.info("value + 2")
#
#if __name__ == "__main__":
#    v = Value("i",0) #i 表示Int, d表示双精度 
#    a = Array("d",[1,2,3,4,5,6,7,8,9])
#    logger.info(a[:])
#    l = Lock()
#    for i in range(processes_num):
#        p = Process(target=thread_main,args=(v,a,l))
#        processes.append(p)
#
#    for p in processes:
#        p.start()
#
#
#    for p in processes:
#        p.join()
#
#    logger.info(a[:])
#    print("main end, value:",v.value)









##使用queue代替 共享数据 value 和 array

#processes = []
#processes_num = 10
#logger = Logger()
#
#def processes_main(input,queue):
#    for v in input:
#        queue.put((os.getpid(),v))
#
#
#
#if __name__ == "__main__":
#    input = range(1,10)
#    q = Queue()
#    for i in range(processes_num):
#        p = Process(target=processes_main,args=(input,q))
#        processes.append(p)
#
#    for p in processes:
#        p.start()
#
#
#    for p in processes:
#        p.join()
#
#    while not q.empty():
#        qitem = q.get();
#        print(f"pid:{qitem[0]},   v:{qitem[1]}")



#进程池


logger = Logger()
def  add10(number):
    result = number + 10
    logger.info(f"result is {result}")
if __name__ == "__main__":
    pool = Pool();
    inputs = [1,2,3,4,5,6]

    pool.map(add10,inputs)