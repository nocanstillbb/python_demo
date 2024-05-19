from log import Logger
print("\n>>>>  异常")

class MyCustomEroor(Exception):
    pass

class MyCustomWidthParametersEroor(Exception):
    def __init__(self,message,value):
        self.message = message
        self.value = value

    pass


try:
    raise MyCustomWidthParametersEroor("custom message", 3)
    raise MyCustomEroor("手动抛出异常") 
    a = 10 + "str"
    zero = 0
    a = 1/zero
    a = 1+ 1
except MyCustomEroor as e: #如果知道异常具体类型,写具体类型
    print("自定义的异常类",e)
except MyCustomWidthParametersEroor as e: 
    print("custom width parameters error:  msg:", e.message, "  value :", e.value)

except ZeroDivisionError as e: #如果知道异常具体类型,写具体类型
    print("zero divistion : ",e)
    print(e)
except TypeError as e: 
    print("type erro : ",e)
#except Exception as e: #尽量不要捕获exception类,否则会额外损耗性能
#    print( "未捕获异常类型",type(e),e)
else:
    print("如果没有异常打印这行")
finally:
    print("无论是否有异常都将打印")


def tst_loggin_from_another_module():
    l = Logger(__name__)
    l.info("hehe")
