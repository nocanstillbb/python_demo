#  set 无序容器

print("\n>>>>  创建")
set_a = {1,1,2,2,3,3} 
print(set_a) # 只有 1 2 3 

print("\n>>>> 可以通过string创建")
set_a = set("hello word")
print(set_a) #乱序被改变了,但不是有序的 ,并且相同的元素被合并覆盖了


print("\n>>>> 坑,空的{}类型为dic")
set_a = {}
print("empty set type is : " ,type(set_a))

print("\n>>>> 所以最好用set()代替想要给set的{}")
set_a = set()
print("empty set type is : " ,type(set_a))


print("\n>>>> add remote")
set_a = set()
set_a.add(1)
set_a.add(2)
set_a.add(3)
set_a.add(4)

set_a.remove(2)
print(set_a)
print("\n>>>> 如果remove了不存在的元素会异常")
try:
    set_a.remove(5) #异常,不存在5
except:
    print("异常,不存在5")

print("\n>>>> 但是可以用discard代替remove,防止异常")
try:
    set_a.discard(5) 
    print("没有异常,即使不存在5")
except:
    print("异常,不存在5")


print("\n>>>> pop 弹出,好像是总是弹先添加的")
avalue = set_a.pop()
print(avalue)
print(set_a)

print("\n>>>> 循环迭代")
for item in set_a:
    print(item)



print("\n>>>> 检查是否存在某个值")
set_a = set()
set_a.add(1)
set_a.add(2)
set_a.add(3)
set_a.add(4)

if 3 in set_a:
    print("exist 3")
else:
    print("not exist 3")
if 9 in set_a:
    print("exist 9")
else:
    print("not exist 9")



print("\n>>>> 并集")
set_a = {1,3,5,7,9}
set_b = {2,4,6,8,10}

set_u = set_b.union(set_a) # 另一种写法
print(set_a)
print(set_b)
print(set_u)


print("\n>>>> 交集")
set_a = {1,2,3,4,5,6,7}
set_b = {3,4,5,6,7,8,9,10}

set_n = set_a.intersection(set_b)
print(set_a)
print(set_b)
print(set_n)

print("\n>>>> 差集")
set_a = {1,2,3,4,5,6,7}
set_b = {3,4,5,6,7,8,9,10}
set_d = set_a.difference(set_b) # 只在a中的
print(set_a)
print(set_b)
print(set_d)

print("\n>>>> 差异")
set_a = {1,2,3,4,5,6,7}
set_b = {3,4,5,6,7,8,9,10}
set_d = set_a.symmetric_difference(set_b) # 只在a或只b中的
print(set_a)
print(set_b)
print(set_d)



print("\n>>>> 更新") 
set_a = {1,2,3,4,5,6,7}
set_b = {3,4,5,6,7,8,9,10}
print(set_a)
print(set_b)
set_a.update(set_b) # 像union
print(set_a)

print("\n>>>> 把交集更新到a") 
set_a = {1,2,3,4,5,6,7}
set_b = {3,4,5,6,7,8,9,10}
print(set_a)
print(set_b)
set_d = set_a.intersection_update(set_b) 
print(set_a)


print("\n>>>> 把只存在a更新到a") 
set_a = {1,2,3,4,5,6,7}
set_b = {3,4,5,6,7,8,9,10}
print(set_a)
print(set_b)
set_d = set_a.difference_update(set_b) 
print(set_a)

print("\n>>>> 把只存在a或只存在b的更新到a") 
set_a = {1,2,3,4,5,6,7}
set_b = {3,4,5,6,7,8,9,10}
print(set_a)
print(set_b)
set_d = set_a.symmetric_difference_update(set_b) 
print(set_a)


print("\n>>>> a是不是b的子集, b是不是a的超集") 
set_a = {1,2,3}
set_b = {1,2,3,4}
print(set_a)
print(set_b)
print("is a b's subset:",set_a.issubset(set_b))
print("is b a's superset:",set_b.issuperset(set_a))

print("\n>>>> 修改数据再来一次,a是不是b的子集, b是不是a的超集") 
set_a = {1,2,3}
set_b = {2,3,4} #去掉1再试一次
print(set_a)
print(set_b)
print("is a b's subset:",set_a.issubset(set_b))
print("is b a's superset:",set_b.issuperset(set_a))


print("\n>>>> a和b是否并不相关") 
set_a = {1,2,3}
set_b = {2,3,4} #去掉1再试一次
print(set_a)
print(set_b)
print("是滞不相关:",set_a.isdisjoint(set_b))

print("\n>>>> 修改数据再来一次,a和b是否并不相关") 
set_a = {1}
set_b = {2,3,4} #去掉1再试一次
print(set_a)
print(set_b)
print("是滞不相关:",set_a.isdisjoint(set_b))

print("\n>>>> 浅复制") 
set_a = {1,2,3}
set_b = set_a 
print(set_a)
print(set_b)
set_b.add(5)
print(set_a)
print(set_b)


print("\n>>>> 深复制") 
set_a = {1,2,3}
set_b = set_a.copy()
print(set_a)
print(set_b)
set_b.add(5)
print(set_a)
print(set_b)

print("\n>>>> 只读的集") 
set_a = frozenset([1,2,3,4])
try:
    set_a[0] = 3
except:
    print("error, frozenset is readonly")
print(set_a)