def print_multiple_params(a,b,c,d=4):
#def print_multiple_params(a,b=2,c,d=4): #参数默认值需要写在最后,否则语法错误
    print(a,b,c)


print_multiple_params(c=3,a=1,b=4) #使用kv形式传参,顺序可以随意
print_multiple_params(1,c=2,b=4) #在普通参数后使用kv形式传参
#print_multiple_params(a=1,2,4) 不能在kv 后使用普通参数传参



#可变参数
def foo(a,b ,*args,**kwargs):
    print(f"a:{a},b:{b}")
    for args_item in args:
        print("args_item : ", args_item)
    for key in kwargs:
        print(f"key:{key}, value:{kwargs[key]}")



print("""\n\n\n============================      
foo("a","b")
============================""")
foo("a","b")

print("""\n\n\n============================      
foo("a","b","c")
============================""")
foo("a","b","c")

print("""\n\n\n============================      
foo("a","b",item="c")
============================""")
foo("a","b",item="c")


print("""\n\n\n============================      
foo("a","b","d","e","f",item="c")
============================""")
foo("a","b","d","e","f",item="c")

#字典折包成为普通参数
print("""\n\n\n============================      
def methoed_a(a,b):
    print(f"a:{a},b:{b}")

dic_a = {"b":1,"a":"2"}
methoed_a(**dic_a)
============================""")
def method_a(a,b):
    print(f"a:{a},b:{b}")

dic_a = {"b":1,"a":"2"}#顺序不重要
method_a(**dic_a)



#全局变量
print("""\n\n\n============================      
num = 1
def method_b():
    global num
    num = 3

method_b();
print("after call method_b, num is :",num)
============================""")
num = 1
def method_b():
    global num
    num = 3

method_b();
print("after call method_b, num is :",num)


#值对象和引用对象
# list , dict 属于引用对象,可以在方法中直接捕获修改,不需要添加global
print("""\n\n\n============================      
============================""")
num = 1
dic_a = {"a":1,"b":2}
list_a = []
def method_c():
    #dic_a = {"a":1,"b":2,"d":4} #没有加global时,如果重新赋值,则会创建局部变量
    dic_a["c"] = 3
    #list_a=[2,3,4,] #没有加global时,如果重新赋值,则会创建局部变量
    list_a.append(3)


method_c();
print("after call method_c, dic is :",dic_a)
print("after call method_c, list is :",list_a)
