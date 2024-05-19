print("\n>>>> 迭代工具 itertools 之product") #
from itertools import product
list_a = [1,2]
list_b = [3]
prod = product(list_a,list_b)  #默认重复一次,
print(list(prod)) 

prod = product(list_a,list_b,repeat=2) 
print(list(prod)) 

prod = product(list_a,list_b,repeat=3)
print(list(prod)) 



print("\n>>>> 迭代工具 itertools 之permutations") # 排序出所有可能性
from itertools import permutations
list_a = [1,2,3,4]
perm = permutations(list_a,2) #默认按元素长度1排列
print(list(perm))



print("\n>>>> 迭代工具 itertools 之combinations") 
from itertools import combinations
list_a = [1,2,3,4]
comb = combinations(list_a,2) #和permutations相似,但同元素顺序不一样也认为是同一种组合,并且一个组合中不会存在相同的元素
print(list(comb))





print("\n>>>> 迭代工具 itertools 之combinations_with_replacement") 
from itertools import combinations_with_replacement
list_a = [1,2,6,3,4]
comb_wr = combinations_with_replacement(list_a,2) #和combination相似,但同一组合中允许有相同的元素
print(list(comb_wr))


print("\n>>>> 迭代工具 itertools 之 accumulate") 
from itertools import accumulate
acc = accumulate(list_a) #每个元素叠加之前的所有元素的和
print(list(acc))

import operator
acc = accumulate(list_a,func=operator.mul) #可以指定操作符,
print(list(acc))

import operator
acc = accumulate(list_a,func=max) #可以指定操作符,
print(list(acc))









print("\n>>>> 迭代工具 itertools 之 groupby + preditor") 
list_a = [1,2,3,4,5,6]
from itertools import groupby

def smaller_then3(value): #定义一个predictor
    return value < 3;
grp = groupby(list_a,key=smaller_then3) #使用predictor方法
for key,value in grp:
    print("key:",key, "\tvalue:",list(value))


print("\n>>>> 迭代工具 itertools 之 groupby + lambda") 
from collections import namedtuple
St =  namedtuple("MyStruct","name,f1")
list_obj = [St("key1",1),
            St("key2",2),
            St("key2",2),
            St("key2",2),
            St("key3",3),
            St("key3",3),
            St("key3",3),
            St("key3",3),
            St("key4",4),
            St("key5",5)]
grp = groupby(list_obj,key=lambda st: st.name ) #使用lambda
for key,value in grp:
    print("key:",key, "\tvalue:",list(value))








print("\n>>>> 迭代工具 itertools 之 无穷迭代器count") 
from itertools import count
#从10迭代到15
c = count(10) 
for item in c:
    print(item)
    if item == 15:
        break






print("\n>>>> 迭代工具 itertools 之 无穷迭代器cycle") 
from itertools import cycle
list_a = [1,2,3]
cy = cycle(list_a)
i = 0
for item in cy:
    print(item)
    i += 1
    if(i == 9):
        break






print("\n>>>> 迭代工具 itertools 之 无穷迭代器repeat") 
from itertools import repeat
list_a = [1,2,3]
rep = repeat(list_a,4) #可以指定需要重复的次数
for item in rep:
    print(item)
    i += 1