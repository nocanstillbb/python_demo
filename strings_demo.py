print('\n>>>> string可以用""括起来,但如果字符串中包含"时,需要在"前面添加\\')
string_a = "他说:\"我没有说话\"" #也可以用''
print(string_a)
print('\n>>>> 或最外层的引号用三个,左右各6个')
string_a = """他说:"我没有说话" """ 
print(string_a)


print("\n>>>> string可以用''括起来,但如果字符串中包含'时,需要在前面添加\\")
string_a = 'hi sayd : "I\'am not him"' 
print(string_a)

print("\n>>>> 或最外层引号用三个,左右各六个")
string_a = '''hi sayd : "I'am not him"'''
print(string_a)

print("\n>>>> 一旦使用了外层6个引号的写法,就可以像c++一样的跨行字符串写法")
string_a = """第1行
第2行 
第3行 
第4行"""
print(string_a)

print("\n>>>> 否则你只能在每一行行尾加\\n\\")
string_a = "第1行\n\
第2行 \n\
第3行 \n\
第4行"
print(string_a)


print("\n>>>> 支持[]操作符,取出char符号")
string_a = "0123456"
char_a = string_a[3]
print(char_a)
char_a = string_a[6] #不支持c++那样取出字符串尾巴的\0
print(char_a)

print("\n>>>> string中的char是只读的")
string_a = "0123456"
try:
    string_a[3] = '9'
except:
    print("string 's char unsuppored write")

print("\n>>>> 切片操作")
string_a = "0123456"
string_b = string_a[1:-1] # 左1字符到右1字符
print(string_b)
string_b = string_a[::2]  #  左0字符开始,每2取1
print(string_b)
string_b = string_a[::-1]  #  左0字符开始,往左,每1取1,相当于翻转字符串
print(string_b)



print("\n>>>> 字符串拼接")
string_a = "Stirng_a"
string_b = "Stirng_b"
print( string_a +  string_b)


print("\n>>>> 字符串的char可以用for迭代")
for c in string_a+string_b:
    print(c)


print("\n>>>> 也可以判断字符串中是否包含了某个char")
if 'c' in "ab":
    print(" string contains c")
else:
    print(" string not contains c")

print("\n>>>> 把c加入再试一次,也可以判断字符串中是否包含了某个char")
if 'c' in "abc": #把c加入再试一次
    print(" string contains c")
else:
    print(" string not contains c")

print("\n>>>> 也可以判断字符串中是否包含了某个短一点的字符串")
if "bc" in "abc": #这里也可以改为一个短一点的字符串
    print(" string contains bc")
else:
    print(" string not contains bc")


print("\n>>>> 修剪两边的字符,如果不写参数,默认修剪两边的空白格")
string_a = "  abcd   "
print(string_a) 
print(string_a.strip()) #先把两边的空白格修剪掉
string_a = string_a.strip()
print(string_a.strip('d')) #再把两边的d修剪掉

print("\n>>>> 大小写转换")
string_a = "abcd"
print(string_a.upper())
print(string_a.upper().lower())
print(string_a) # 不会改变原来的字符串

#省略endwidth startwidth find count


print("\n>>>> 把字符串列表组成单个字符串")
string_args = ["aaa","bbb"]
string_merge = ",".join(string_args)
print(string_merge)



print("\n>>>> 使用timer 做性能诊断")
from timeit import default_timer as timer
start = timer()
string_args = ["aaa","bbb"]
string_merge = ",".join(string_args)
print(string_merge)

stop = timer()
print(stop - start) #单位是秒


print("\n>>>> 格式化字符串 1")
string_a = "a str var"
double_a = 1.23456
print("this is  %.3f"  % double_a)#好像只能写一个变量
print("this is {:.3f}".format(double_a)) #好像也只能写一个变量

print("this is {} and {:.3f}".format(string_a,double_a)) #这种可以写更多变量

print(f"this is {string_a} and {double_a:.3f}")#更进一步

print(f"this is {string_a * 2 } and {double_a * 2 :.3f}")#可以是表达式