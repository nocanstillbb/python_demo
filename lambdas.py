print("\n>>>> lambda")
lam_add10 = lambda x:x+10  #基础用法
print("exec lambda:" , lam_add10(10))


print("\n>>>> lambda 用于排序")
point2D = [(1,2), (14,3), (12,3), (8,10), (16,3), (14,15),(4,3),(6,7),(8,8)]
print(point2D)
print(sorted(point2D))
#用lambda排序
print(point2D)
print(sorted(point2D,key=lambda x: x[0]*10 + x[1]))


print("\n>>>> lambda 用于映射")
list_a = [1,2,3,4]
print(list_a)
print(list(map(lambda x: x*10,list_a)))
print([item * 20 for item in list_a]) #一种比lambda更简洁的map写法


print("\n>>>> lambda 用于过滤")
list_a = [1,2,3,4,5,6,7,8,9]
print("filter by lambda:",list(filter(lambda x: x%2 == 0,list_a)))
print("filter not using lambda:", [item for item in list_a if item %2 ==1]) #一种比Lambda更简洁的过滤写法
print("filter + map not using lambda:", [item * 20 for item in list_a if item %2 ==1]) #一种比Lambda更简洁的过滤写法


print("\n>>>> lambda 用于reduce")# 和itetools中的accmulate 一样的作用,只是写法不一样
from functools import reduce
from itertools import accumulate

list_a = [10,9,8,7,6,5,4,3,2,1]
print(reduce(lambda x ,y :x*y ,list_a)) 
print(list(accumulate(list_a,func=lambda x,y: x*y))) 

