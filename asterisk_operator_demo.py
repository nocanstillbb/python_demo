#乘法
value_a = 1*2
print("value_a: ",value_a)
#指数
value_a = 2**3
print("value_a = 2**3: ",value_a)
#数组 重复
list_a = [1,2] * 2
print("list_a = [1,2] * 2  :",list_a)
#元组 重复
tuple_a = (1,2) * 2
print("list_a = (1,2) * 2  :",tuple_a)
#字符串 重复
str_a = "hbb " * 2
print("""str_a = "hbb " * 2  :""",str_a)
#可变参数
def method_a(*args,**kwargs):
    print(args)
    for key in kwargs:
        print(f"key:{key}, value:{kwargs[key]}")

method_a(1,2,3,a="b",c="d")

#list, tuple, dict 拆包为函数参数
def method_b(a,b):
    print(f"a = {a} , b = {b}")

list_a = [1,2]
tuple_a = (1,2)
dict_a = {"a":1,"b":2}
method_b(*list_a)
method_b(*tuple_a)
method_b(**dict_a)

#拆分list 和tuple
list_a = [1,2,3,4,5]
first,*array,last_pre,last= list_a 
print("first :",first)
print("array :",array) #不管是list还是tuple, 拆包后的数组都是一个新的list
print("last_pre : ",last_pre)
print("last : ",last)


#拼接两个列表,或元组,set
list_a = [1,2,3]
tuple_a = (4,5,6)
set_a = {7,8,9}
print([*list_a,*tuple_a,*set_a])
#拼接两个dictionary
dict_a = { "a" : 1 , "b":2}
dict_b = { "c" : 1 , "d":2}
print({**dict_a,**dict_b})