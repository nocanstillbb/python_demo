import random

print("\n>>>>  生成一个0至1的伪随机数flaot")
num_a = random.random();
print(num_a)


print("\n>>>>  生成一个1至2的伪随机数float")
num_a = random.uniform(1,2);
print(num_a)

print("\n>>>>  生成一个1至3的伪随机数int")
num_a = random.randint(1,3); #包含3
num_b = random.randrange(1,3); #不包含3
print(num_a)
print(num_b)

print("\n>>>>  正态分布随机数")
num_a = random.normalvariate(1,1); #参数1,平均值  参数2,标准差  
print(num_a)


print("\n>>>>  随机选择列表中的1个元素")
list_a = [1,3,5,7,9]
num_a = random.choice(list_a)  
print(num_a)

print("\n>>>>  随机选择列表中的多个元素")
list_a = [1,3,5,7,9]
num_a = random.sample(list_a,3)  #不会重复
num_b = random.choices(list_a,k=3)  #会重复
print(num_a)
print(num_b)


print("\n>>>>  洗牌,打乱列表顺序")
list_a = [1,2,3,4,5,6,7,8,9]
random.shuffle(list_a)
print(list_a)


print("\n>>>>  伪随机数重复实验") #以上都是伪随机方法,seed设置一样都能重现随机结果
random.seed(1)
list_a = [1,2,3,4,5,6,7,8,9]
random.shuffle(list_a)
print(list_a)
random.seed(1)
list_a = [1,2,3,4,5,6,7,8,9]
random.shuffle(list_a)
print(list_a)



import secrets #相对伪随机数,更耗时,但更安全 
print("\n>>>>  int随机数")
num_a = secrets.randbelow(3) #0,1,2 不包含3
print(num_a)


print("\n>>>>  k位数的随机0101二进制数")
num_a = secrets.randbits(2) # 00 - 11
print(num_a)


print("\n>>>>  列表中随机取一")
list_a = list("abcd")
num_a = secrets.choice(list_a) 
print(num_a)

import numpy as np

np.random.seed(1)
print("\n>>>>  numpy 3    0-1")
numpy_a = np.random.rand(3) 
print(numpy_a)
print("\n>>>>  numpy 3*4  0-1")
numpy_a = np.random.rand(3,4) 
print(numpy_a)
print("\n>>>>  numpy 3*4*5  0-1")
numpy_a = np.random.rand(3,4,5) 
print(numpy_a)


print("\n>>>>  numpy 3*4*5  int 10-20")
numpy_a = np.random.randint(10,20,(3,4,5)) #如果是单维的话,可以不写元组只写标量
print(numpy_a)
print("\n>>>>  numpy 3*4*5  shuffle")
np.random.shuffle(numpy_a) 
print(numpy_a)