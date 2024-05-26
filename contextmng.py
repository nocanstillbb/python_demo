#打开文件
def method_a():
    with open("hbb.log","a") as file:#类似c++的raii
        file.write("不是吧哥门儿")

method_a()


#使用锁
from threading import Lock
def  multiplethreadlock():
    l = Lock()
    with l:
        print("do stuff")


multiplethreadlock()

#使用类 自定义context
class customContextClass:
    def __enter__(self):
        print("enter")
    def __exit__(self,exc_type,exc_value,exc_backtrace):
        if exc_type is not None:
            print("exception is be handeled")
            #return False #如果返回false,则不会处理异常
        print(f"exit, exc_type:{exc_type}, exc_value:{exc_value}")
        return True


with customContextClass():
    print("do stuff")
    z = 0
    a = 100/z

print("continue")



#使用方法+ try catch + yield+ generator自定义上下文

from contextlib import contextmanager

@contextmanager
def customContextMethod(file):
    try:
        yield file
        print("try arg:",file)
        print("try body")
    except Exception as ex:
        print(ex)
        print("try except")
    else:
        print("try else")
    finally:
        print("try finally")


with customContextMethod("file str") as c:
    print("customContextMethod body")
    z = 0
    a = 3/z
    print(c)