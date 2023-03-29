#a=list[range(10000000)]
#print(a)
"""def make_list(num):
    result =[]
    for i in range(num):
        result.append(i*2)
    return result

my_list=make_list(100)
print(list(range(100)))"""

#interable
#iterate 
#genrator 

#yeild keyword 
"""def genrator_function(num):
    for i in range(num):
        yield i*2

g=genrator_function(100)
next(g)
next(g)
print(next(g))"""

#genrators performance 
"""from time import time 
def gen_fun(num):
    for i in range(num):
        yield i

for item in gen_fun(100):
    print(item)"""

#below of genrators
"""def special_for(iterable):
    iterator= iter(iterable)
    while True:
        try:
            print(iterator)
            print(next(iterator)*2)
        except StopIteration:
            break

special_for([1,2,3])"""

#create a range function
"""class MyGen():
    current=0
    def __init__(self, first, last):
        self.first=first
        self.last=last
    
    def __iter__(self):
        return self

    def __next__(self):
        if MyGen.current<self.last:
            num=MyGen.current
            MyGen.current+=1
            return num
        raise StopIteration
gen=MyGen(0, 100)
for i in gen:
    print(i)
#next(gen)
#print(next(gen))"""

#exercise 
"""def fib(num):
    a=0 
    b=1
    for item in range(num):
        yield a
        temp = a
        a = b
        b = temp + a

for x in fib(20):
    print(x)"""
