print("\n>>>> 计数器")
from collections import Counter
str_a = "hbbccc"
hbbcounter = Counter(str_a)
print("hbb计数结果: ", hbbcounter)
print("计数器类型为:", type(hbbcounter))
print("计数器.items() :", hbbcounter.items())
print("计数器.keys() :", hbbcounter.keys())
print("计数器.values() :", hbbcounter.values())
print("计数器.most_common() :", hbbcounter.most_common(1)) # 返回1个元组列表
print("计数器.elements() :", hbbcounter.elements()) # 迭代器
print("list(计数器.elements()) :", list(hbbcounter.elements())) # list(迭代器)可以访问输入counter的所有数据





print("\n>>>> 命名元组 namedtuple")
from collections import namedtuple
Point = namedtuple("Point", "x,y")
pt = Point(3.14, "yyy")
print("pt:",pt)
print("pt.x:",pt.x)
print("pt.y:",pt.y)






print("\n>>>> 有序关联容器 ordered_dict") #记住插入顺序的dict,
#3.7以来,dict已经可以记住插入顺序了 ,所以这个类一般只在版本低的python中有用
# 记住插入顺序主要影响的是 pop, popitem
from collections import OrderedDict

print("普通字典") 
dic = dict()
dic["a_key"] = "a_value"
dic["c_key"] = "c_value"
dic["b_key"] = "b_value"
print(dic)
for item in dic:
    print(item)

print("有序字典") 
odic = OrderedDict()
odic["a_key"] = "a_value"
odic["c_key"] = "c_value"
odic["b_key"] = "b_value"
print(odic)
for item in odic:
    print(item)







print("\n>>>> 默认关联容器 default_dict") #有默认值的容器
from collections import defaultdict
ddict = defaultdict(int) #默认的value的类型需要指定,否则取不存在的key的value时会异常
print("获取一个不存在的key,会自动创建",ddict["a"])







print("\n>>>> 队列 deque")  #支持两端插入, 从两端删除
from collections import deque

deq = deque()

#添加元素到右边
deq.append(0)
deq.append(0)
deq.append(0) #添加单个
deq.extend([4,5,6]) #一次添加多个
#添加元素到左边
deq.appendleft(7)
deq.extendleft([8,9,10])
print(deq)
right = deq.pop() #弹出右边元素
left = deq.popleft() #弹出左边元素
print("left:",left)
print("right:",right)
print("deque:",deq)

#支持循环位移操作
deq.rotate(1) #向右循环移位1位
print("after rotate to the right:",deq)
deq.rotate(-2) #再向左循环移位2位
print("after rotate to the left:",deq)