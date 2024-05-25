import functools

print("\n>>>>   函数装饰器")
def func_wrapper(func):

    @functools.wraps(func) #解决打印func_a.__name__显示不对的问题
    def inner_func(*a,**b): #加这两个参数会传递参数进装饰器
        print("start exec func")
        result = func(*a,**b)
        print("end")
        return result
    return inner_func;

print("\n>>>>   类装饰器")
class  CountDecorator:
    def __init__(self,func) -> None:
        self.func = func
        self.count = 0

    def __call__(self, *args, **kwds):
        self.count +=1
        self.__name__ = "hbbclass"
        print(self.count)
        return self.func((args,kwds))



@CountDecorator
@func_wrapper #使用装饰器后,调用func_a会把func_wrapper里的逻辑也执行了
def func_a(p1):
    print(p1)
    return True


#f = func_wrapper(func_a)#这一步可以省掉,在使用decorator之后
#f()

r = func_a("abc")
print(r)

print(func_a.__name__) # inner_func
print(func_a.__name__) # inner_func
#print(help(func_a)) 


#for _ in range(3): #记录一下python 写类似c++的for循环 