#dictionary 无序关联容器
print("\n>>>>  创建")
#方法1
dic = {"key": "value","key2":2 , "key3" : 3.3 , 1:2}
print(dic)
#方法2
#dic = dict(key="value", key2=2 , key3= 3.3 ) #key只能是字符串
#print(dic)


print("\n>>>>  取值")
print("key = 1   value = ",dic[1])
print("key = 'key3'   value = ",dic["key3"])
#print("key = 'notExsit'   value = ",dic["notExsit"]) #如果不存在的key 会异常,不像c++ std::map会创建


print("\n>>>>  添加")
dic["add"] = "aaa.bbb"
print("key = 'add'   value = ",dic["add"]) 

dic["add"] = "aaa.bbbcc" #再添加一次,会覆盖,而不不是创建一个同样的key
print("key = 'add'   value = ",dic["add"]) 


print("\n>>>>  删除一对 key value")
del dic["add"]
print(dic)


print("\n>>>>  pop,取出+删除")
dic["add"] = "aaa.bbb" 
print(dic)
v = dic.pop("add") #注意,取出来的是value,不中key value pair
print(v)
print(dic)



print("\n>>>>  popitem")
dic["new"] = "new item";
print(dic)
v = dic.popitem() #3.7之前,会随机弹出,  3.7之后,只弹出最后插入的key value
print(v)
print(dic)



print("\n>>>>  检查是否存在key")
dic["new"] = "new item";
if "new" in dic: # 取value时先判断是否存在key
    print("exist")
else:
    print("not exist")

try:
    print(dic["not exist"])
except:
    print("not exist key ")



print("\n>>>>  迭代key")
for key in dic:
    print(key,"\t\t: ",dic[key])

import sys
print("python version : ",sys.version)

#for k,v in dic.items:  #这种语法在python 3.12中好像不支持,其他版本好像可以
#    print(k,"\t\t: ",v)



print("\n>>>>  浅复制")
dic2 = dic
print("dic : ",dic)
print("dic2:" ,dic2)
dic2["tst copy key"] = "tst copy value" #这将会添加到dic 和dic2中
dic2["tst copy key"] = "tst copy value 22"  # 这行也会修改到两个dic中
print("dic : ",dic)
print("dic2:" ,dic2)

print("\n>>>>  copy深复制")
dic.popitem()
dic2 = dic.copy() #copy
print("dic : ",dic)
print("dic2:" ,dic2)
dic2["key"] = "tst copy value" #这将会添加到dic2中,但不会添加dic2中
dic2["key"] = "tst copy value 22"  #修改也是仅作用在dic2
print("dic : ",dic)
print("dic2:" ,dic2)

print("\n>>>>  构造函数深复制")
dic2 = dict(dic) # 构造函数传dict也是深复制
print("dic : ",dic)
print("dic2:" ,dic2)
dic2["key"] = "tst copy value" #这将会添加到dic2中,但不会添加dic2中
dic2["key"] = "tst copy value 22"  #修改也是仅作用在dic2
print("dic : ",dic)
print("dic2:" ,dic2)


print("\n>>>>  拼接两个dic")
dic = {1:"a",  2:"b",   3:"c"}
dic2 = {"a":1, "b":2,   "c":3}
print("dic : ",dic)
print("dic2:" ,dic2)
dic.update(dic2)
dic2["a"] = 99 # 修改值后没有影响拼接后的dic1,所以dic2部分已经复制了
print("dic : ",dic)
print("dic2:" ,dic2)



print("\n>>>>  list和tuple作为key的测试")
#tuple是只读的,所以可以作为dict的key , 
dic[(1,3)] = 2
print(dic)

#list是不是只读的,可能会在创建后修改,所以不能作为dict 的key 
list = [1,3]
try:
    dic[list] = 4
except:
    print('not support')