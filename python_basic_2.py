#boolean 
"""is_string=bool('')
is_number=bool(0)
print(is_number)
print(is_string)"""

#Ternary_operator
#condition_if_true if condition else condition_if_else
"""is_doorbell=input()
bell_ringing='Open the door 'if is_doorbell else "Keep door closed"
print(bell_ringing)"""

#short circuting
"""Prasad=True
His_friend=True
if Prasad and His_friend:
   print("best friend forever")"""

"""is_expert=True
is_magician=True
if is_magician and is_expert:
    print("you are a master magician")
elif is_magician or is_expert:
    print("at least you'r getting there")
elif not(is_magician and is_expert):
    print("You need magic powers")"""

"""user={
    'Name':'Soham',
    'Age':12,
    'Can_dance':True
}
for key,values in user.items():
    print(key, values)

my_list=[1,2,3,4,5,6,7,8,9,10]
count=0
for items in my_list:
    count=count+items
print(count)"""

"""for i in range(2):
    print(list(range(10)))""" 

"""for char in enumerate('hello'):
    print(char)
for i,char in enumerate(list(range(100))):
    if char ==50:
        print(f'Indexof {i} is: {char}')"""

"""i=50
while i<50:
    print(i)
    i+=1
    break
else:
    print('Bye Have a nice day')"""    

"""Picture= [
   [0,0,0,1,0,0,0],
    [0,0,1,1,1,0,0],
    [0,1,1,1,1,1,0],
    [1,1,1,1,1,1,1],
   [0,0,0,1,0,0,0],
   [0,0,0,1,0,0,0]
]
for image in Picture:
    for pixel in image:
     if pixel==1:
        print('*',end='')
     else:
        print('',end=' ')
    print('')"""
    
"""some_list=['a','b','c','b','d','m','n','n']
duplicates=[]
for items in some_list:
    if some_list.count(items) >1:
        duplicates.append(items)

print(duplicates)"""

#parameters
#default parameters 
"""def say_hello(name='Ghost Rider',emoji=':)'):
    print(f'hello {name}{emoji}')"""

#positional agruments
"""say_hello('Abhijeet',':)')
say_hello('Kunal',':)')
say_hello('Soham',':)')"""

#keywords arguments
"""say_hello(name='Prasad',emoji=':)')"""

#return function
"""def sum(num1, num2):
    def another_sum(n1, n2):
        return n1+n2
    return num1+num2
print(sum(4,5))"""

"""def func(*args, **kwargs):
    print(kwargs)
    total=0
    for i in kwargs.values():
        total+=i
    return sum(args)"""
    
#func(1,2,3,4,5,n=5,n1=9)
#Rule:params, *args, Default parameters, **kwargs

"""def highest_even(li):
    hiEvNum=[]
    for items in li:
     if items%2==0:
         hiEvNum.append(items)
    return max(hiEvNum)
print(highest_even([24,10,2,3,4,8,11]))"""

#walrus method ':='
"""a='Prasad'
if ((n:=len(a))>10):
    print(f'the given length of string is {a}')

x='Hello'[0]
print(x)"""