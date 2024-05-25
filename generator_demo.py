def mygenerator():
    yield 3
    yield 5
    yield 2
    yield 6


print("""\n\n\n=====================
g = mygenerator()
print(list(g))
=====================""")
g = mygenerator()
print(list(g))


print("""\n\n\n=====================
g = mygenerator()
list(g)
=====================""")
g = mygenerator()
print(list(g))#虽然可以这样做,但不要,因为generator的优势就是不占用大量内存也能迭代

print("""\n\n\n=====================
g = mygenerator()
list(g)
for i in g:
    print(i)
=====================""")
g = mygenerator()
for i in g:
    print(i)


print("""\n\n\n=====================
g = mygenerator()
value_a = next(g) 
print("value_a:",value_a)
for i in g:
    print(i)
=====================""")
g = mygenerator()
value_a = next(g) 
print("value_a:",value_a)
for i in g:
    print(i)



print("""\n\n\n=====================
g =  mygenerator()
gs = sorted(g)
for i in g: 
    print(i)
for i in gs: 
    print(i)
=====================""")
g =  mygenerator()
gs = sorted(g)
for i in g: 
    print(i)
for i in gs: 
    print(i)


import sys
print("""\n\n\n=====================简化写法和表列简化写法类似,但[]改为()
g =  (i*2 for i in range(10000) if i%2 ==0)
l =  [i*2 for i in range(10000) if i%2 ==0]
print("size of g:",sys.getsizeof(g))
print("size of g:",sys.getsizeof(l))
===============================================================""")
g =  (i*2 for i in range(10000) if i%2 ==0)
l =  [i*2 for i in range(10000) if i%2 ==0]
print("size of g:",sys.getsizeof(g))
print("size of g:",sys.getsizeof(l))
