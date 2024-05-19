print('\n>>> 创建元组')
tuple_a = (1, True, "balabala",1,1,1)
print(tuple_a)

tuple_a = (1)
print(type(tuple_a)) #int
tuple_a = (1,)
print(type(tuple_a)) #tuple
tuple_a = tuple([1, True, "balabala",1,1,1]) #也可以从数组创建, tuple([...])
print(tuple_a)

print('\n>>> 取元组数据')
item = tuple_a[2] #从0开始第2个元素
print(item)

item = tuple_a[-2] #第右往左,第2个元素
print(item)

for i in tuple_a: # iterater
    print(i)

if "balabala" in tuple_a: # if contains
    print("exsit")
else:
    print("not exsit")


print(len(tuple_a)) #打印无组长度


print (tuple_a.count(1)) # 打印tuple中有几个1, true也会被统计进去,有点费解

print (tuple_a.index("balabala")) #打印元个元素的index
#print (tuple.index("not exsit")) #如果元素不存在异常


print('\n>>> 元组是只读的')
#tuple_a[0] = 2 #将会异常,因为是只读的



print('\n>>> 元组转为List')
list_a = list(tuple_a)
print(list_a)

print('\n>>> 元组切片操作和list一样,没什么好说的')


print('\n>>> 模式匹配')
tuple_a = (1,False,"str")
i,b,s = tuple_a
print("i:",i)
print("b:",b)
print("s:",s)

i,*b = tuple_a # 匹配变量可以少于,不可以大于元组元素长度, 加*号取出来会变成列表,从n到结尾
print("i:",i)
print("b:",b)



print('\n>>> 元组和list的区别')
print('\n>>> 1.元组是只读的')
print('\n>>> 2.元组内存占用比少')
tuple_a = (1,2,3)
list_a  = [1,2,3]
import sys
print ("size of tuple:",sys.getsizeof(tuple_a), "bytes")
print ("size of list:",sys.getsizeof(list_a)," bytes")
import timeit
print ("create tuple 1000000 times :", timeit.timeit(stmt="(1,2,3,4)",number=1000000))
print ("create lists 1000000 times :", timeit.timeit(stmt="[1,2,3,4]",number=1000000))