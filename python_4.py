#map,filter, zip and reduce 
#map
"""my_list=[1,2,3]
def multiply_by2(item):
    return item*2
    
print(list(map(multiply_by2,my_list)))
print(my_list)"""
#filter
"""my_list=[1,2,3]
def multiply_by2(item):
    return item*2

def check_odd(item):
    return item % 2 !=0
    
print(list(filter(check_odd,my_list)))
print(my_list)"""
#zip
"""my_list=[1,2,3]
your_list=[10,20,30]
there_list=[1,4,7]
def multiply_by2(item):
    return item*2

def check_odd(item):
    return item % 2 !=0
    
print(list(zip(my_list,your_list,there_list)))
print(my_list)"""
#reduce
"""from functools import reduce
my_list=[1,2,3]

def multiply_by2(item):
    return item*2

def check_odd(item):
    return item % 2 !=0

def accumalator(acc, item):
    print(acc, item)
    return acc + item
    
print(reduce(accumalator, my_list, 0))
print(my_list)"""
#exercise
"""from functools import reduce
my_pets=['sisi','bibi','titi','carla']
def cap(item):
    return item.upper()
print(list(map(cap, my_pets)))

my_strings=['a','b','c','d','e']
my_numbers=[5,4,3,2,1]
print(list(zip(my_strings,my_numbers)))

scores=[73,20,65,19,76,100,88]
def define(item):
    return item > 50

print(list(filter(define,scores)))

def sum(acc, item):
    print(acc, item)
    return acc + item

print(reduce(sum,(my_numbers + scores)))"""
#lambda expresssion
"""from functools import reduce
my_list=[1,2,3]
print(reduce(lambda acc, item: acc+item ,my_list))
print(my_list)"""

"""my_list=[5,4,3]
print(list(map(lambda item:item * item,my_list)))

a=[(0,2), (4,3), (10,-1), (9,9)]
a.sort(key=lambda x: x[1])
print(a)"""
#list comprehensions
#list, set, dictionary
"""my_list=[char for char in 'hello']
my_list2=[num for num in range(0,100)]
my_list3=[num**2 for num in range(0,100)]
my_list4=[num**2 for num in range(0,100)if num%2==0]
print(my_list)
print(my_list4)"""

#set comprehensions 
"""my_list={char for char in 'hello'}
my_list2={num for num in range(0,100)}
my_list3={num**2 for num in range(0,100)}
my_list4={num**2 for num in range(0,100)if num%2==0}
print(my_list)
print(my_list4)"""
#dictionary comprehensions 
"""simple_dict={
    'a':1,
    'b':2
}
my_dict= {key:value**2 for key, value in simple_dict.items() if value%2==0 }
my_dict2={num:num*2 for num in [1,2,3]}
print(my_dict2)"""

#exercise 
"""some_list=['a','b','c','b','d','m','n','n']
duplicates=set([value for value in some_list if some_list.count(value)>1 ])
print(duplicates)"""