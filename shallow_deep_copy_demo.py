import json

#值类型 赋值操作为deep copy
value_a = 5
value_b = value_a
value_b = 6
print(f"value_a : {value_a}, value_b:{value_b}")

#引用类型,赋值操作为shallow copy
list_a = [1,2,3]
list_b = list_a
list_b[0] = 4
print(f"flist_a:{list_a}, list_b:{list_b}")

#使用切片操作复制
list_a = [1,2,3]
list_b = list_a[:]
list_b[0] = 4
print(f"flist_a:{list_a}, list_b:{list_b}")

#使用构造复制
list_a = [1,2,3]
list_b = list(list_a)
list_b[0] = 4
print(f"flist_a:{list_a}, list_b:{list_b}")

#使用 copy 模块复制
import copy
list_a = [1,2,3]
list_b = copy.copy(list_a)
list_b[0] = 4
print(f"flist_a:{list_a}, list_b:{list_b}")



#更深层的引用复制测试

#使用切片操作复制
list_a = [[1,2,3],[4,5,6]]
list_b = list_a[:]
list_b[0][0] = 4
print(f"flist_a:{list_a}, list_b:{list_b}")

#使用构造复制
list_a = [[1,2,3],[4,5,6]]
list_b = list(list_a)
list_b[0][0] = 4
print(f"flist_a:{list_a}, list_b:{list_b}")

#使用 copy 模块复制
import copy
list_a = [[1,2,3],[4,5,6]]
list_b = copy.copy(list_a)
list_b[0][0] = 4
print(f"flist_a:{list_a}, list_b:{list_b}")

#使用 copy 模块复制
import copy
list_a = [[1,2,3],[4,5,6]]
list_b = copy.deepcopy(list_a)
list_b[0][0] = 4
print(f"flist_a:{list_a}, list_b:{list_b}")


#类测试

class Company:
    def __init__(self,name,boss=None)->None:
        self.name = name
        self.boss = boss

class Person:
    def __init__(self,name,age,company)->None:
        self.name = name
        self.age = age
        self.company = company


print("\n>>>> 浅复制类 ")
company_a = Company("deepvision")
p_a = Person("hbb",32,company_a)
p_b = p_a
p_b.age = 1
p_b.company.name = "xyy"
#lambda_a = lambda p: {"name" :p.name,"age":p.age, "company":p.company.name} 
lambda_a = lambda p: p.__dict__ 
print(f"p_a:{json.dumps(p_a,default=lambda_a)} \n p_b:{json.dumps(p_b,default=lambda_a)}")



print("\n>>>> copy.copy复制类 ")
company_a = Company("deepvision")
p_a = Person("hbb",32,company_a)
p_b = copy.copy(p_a)
p_b.age = 1
p_b.company.name = "xyy"
#lambda_a = lambda p: {"name" :p.name,"age":p.age, "company":p.company.name} 
lambda_a = lambda p: p.__dict__ 
print(f"p_a:{json.dumps(p_a,default=lambda_a)} \n p_b:{json.dumps(p_b,default=lambda_a)}")



print("\n>>>> copy.deepcopy复制类 ")
p_boss =  Person("boss",99,company_a)
company_a = Company("deepvision",p_boss)
p_a = Person("hbb",32,company_a)
p_b = copy.deepcopy(p_a)
p_b.age = 1
p_b.company.name = "xyy"
p_b.company.boss.name = "nobody is boss of me"
#lambda_a = lambda p: {"name" :p.name,"age":p.age, "company":p.company.name} 
lambda_a = lambda p: p.__dict__ 
print(f"p_a:{json.dumps(p_a,default=lambda_a,indent=4)} \n p_b:{json.dumps(p_b,default=lambda_a,indent=4)}")


