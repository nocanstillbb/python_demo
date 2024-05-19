print("\n>>>>列表构造")
list = ["banana", "cheery","apple",False,False]
print(list)

print("\n>>>>列表中可以有不同的类型的元素")
list2 = [True, "aaa",333, 44.4,False,False]
print(list2)

print("\n>>>>列表索引")

print(list2[0]) #第一个元素
print(list2[1]) #第二个元素
print(list2[-1])  # 倒数第一个元素
print(list2[-2]) #倒数第二个元素

print("\n>>>>循环列表中的元素")
for item in list2:
    print(item)

print("\n>>>>判断列表中是否存在元素") 
if "aaa"  in  list2:
    print("aaa is in list2")
if False  in  list2:
    print("False is in list2")
else :
    print("False isn't in list2")

print("\n>>>>列表的元素个数") 
print (len(list2))

print("\n>>>>元素增删") 
list2.append(3.14159) #添加元素到末尾
print(list2)
list2.insert(0,"插入到第index 0的位置")
print(list2)
lastele = list2.pop() # 移除最后一个元素
print(lastele)
print(list2)
list2.remove(False) # 删除一个flase
print(list2)
list2.clear() #清除所有
print(list2)


print("\n>>>>反转列表的顺序")
list2.append(1)
list2.append(2)
list2.append(3)
list2.reverse() 
print(list2)


print("\n>>>>列表排序")
list.clear();
list.append(1)
list.append(4)
list.append(3)
list.append(7)
list.append(7)
list.append(5)
list.sort; # 第1种排序
list_sort1 = sorted(list); #第二种排序
print(list)
print(list_sort1)
list_sort1[0] = 99 # sorted会复制,所以这里只会修改list_sort1的
print(list)
print(list_sort1)



print("\n>>>>初始化10个0的列表")
list = [0] * 10
print (list)
print("\n>>>>两个列表拼接")
list2 = [3] * 10
list_merge = list2+list
list_merge[1] = 99 #修改元素,只会修改合并后的,由此可知拼接时发生了复制
print (list)
print (list2)
print(list_merge)

print("\n>>>> 切片操作")
list = [0,1,2,3,4,5,6,7,8,9,10]
list_cut = list[0:5] # 0-4个元素
list_cut[0] = 99 #只修改切片后的列表,所以切片会复制
print(list)
print(list_cut)

list_cut = list[:5] # 开始到第5个元素
print(list)
print(list_cut)

list_cut = list[5:] # 第5个元素到最后一个元素
print(list)
print(list_cut)
list_cut = list[3::] # 从3开始,每1取1   同3::1
print(list)
print(list_cut)
list_cut = list[3::2] # 从3开始, 每2取1
print(list)
print(list_cut)
list_cut = list[::4] # 从第0个,每4取1, 同1::4
print(list)
print(list_cut)
list_cut = list[::-1] # 从0开始,往左边每1取1,  相当于反转列表
print(list)
print(list_cut)


print("\n>>>> 深浅复制")
list = [0,1,2,3,4,5,6,7,8,9,10]
list2 = list 
list2[0] = 99 # 修改后两个数组都被修改了,所以=操作符为浅复制
print(list)
print(list2)

list = [0,1,2,3,4,5,6,7,8,9,10]
list2 = list.copy()
list2[0] = 99 # 因为调用了copy,所以只修改了list2
print(list)
print(list2)


list = [0,1,2,3,4,5,6,7,8,9,10]
list2 = list[:]  #切片:表示取所有元素
list2[0] = 99 # 因为调用使用了切片也会发生复制,,所以只修改了list2
print(list)
print(list2)

list = [0,1,2,3,4,5,6,7,8,9,10]
list2 =[i*10 for i in list]  #复制时,每个元素*=10 
print(list)
print(list2)