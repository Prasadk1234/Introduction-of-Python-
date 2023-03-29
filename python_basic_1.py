#fundamentals of datatype
#int and float
#print(type(2+4))
#print(type(2-4))
#print(type(2*4))
#print(type(2/4)) #0.5
#print(type(20+1.1))
#print(2 ** 2)
#print(5 // 4)
#print(6 % 4)

#math functions 
#print(round(3.1))
#print(abs(-20))   for more functions google it 

#operator procedence 
#print((20-3)+2**4) 
#1]()
#2]**
#3]* /
#4]+ -
#print(10 // 2)

#complex datatype
#print(bin(5))
#print(int('0b101',2))

#variables
#a,b,c=1,2,3
#print(a,b,c)
#iq=190 
#print(iq)
#CONSTANTS
#PI=3.14
#__ dundales

#expression vs statements 
#iq=100 #statments
#user_age=iq/5 #this is the experssion 

#argumented assignment operator 
#some_value=5
#some_value+=2
#print(some_value)

#String
"""print(type("Hello there 24!"))
username='Prasad'
passsword='admin'
long_string='''
hellow How ar you.........?
'''"""
#print(long_string)
"""first_name='Prasad'
last_name=' Kate'
full_name=first_name+ last_name 
print(full_name)
#string concatinating 
print('hello' + 'there')
print(type(int(str(100))))""" #type conversion

#escape sequence 
#weather= "\tit\'s\"kind of\" sunny\nhope you have Goood day"
#print(weather)'''

#formatted string
"""name='Prasad'
age=21
print(f'hi {name}. You are {age} years old')"""

#string index
"""str='01234567'
print(str[0:8:2])"""

#imutability google it 

#built -in function + methods of strings google it for more
"""quote='to be or not to be '
print(quote.index('b'))"""

#booleans 
"""print(bool('True'))
print(bool(0))"""

#exercise1
"""birth_year=input('What year were yoou born?')
age= 2023-int(birth_year)
print(f"your age is {age}")"""

#exercise2
"""user_name=input("Enter your User Name")
password=input("Enter your Password")
password_length=len(password)
hidden_password='*' * password_length
print(f'{user_name} your passwoord is {hidden_password} is {len(password)} is long')"""

#list slicing
"""Flipkart=['MacBook',
'Marshall',
'Sony',
'Pendrive',
'Sneakers']
Flipkart[0]='Books'
print(Flipkart)
new_cart=Flipkart[:]
new_cart[0]='Gum'
print(new_cart , Flipkart)"""

#matrix us to machine learning 
"""matrix=[[
    1,2,3],
    [4,5,6],
    [7,8,9]]
print(matrix[0][1])
print(matrix)"""

#list methods
"""balles=['a','z','b','c','d','e']
print(balles)"""
#adding and removing
"""print('a' in balles)
print(balles.sort())
print(sorted(balles))
print(balles)
print(balles[::-1])
print(list(range(11)))
new_sentence=''.join(['hi','my','name','is','Prasad'])
print(new_sentence)
a,b,c, *other=[1,2,3,4,5,6,7]
print(a)
print(other)"""

#dictionary its a unoreded key value pair
"""dictionary={
    'Python': [40,50,89],
    'Cpp': 'Hello',
    'HTML':20
}
my_list=[{ 'Python': [40,50,89],
    'Cpp': 'Hello',
    'HTML':20}]
print(my_list[0])
print(dictionary['Python'])
user={
  'Basket':[1,2,3],
 'Green':'Hello',
  'age': 21
}
user2=dict(name='Prasad') # Second type of producing dictionary
print(user.get('age', 78))
print(user2)
print('Green' in user.keys())
print(user.items())
print(user.clear())
user_2=user.copy()
print(user_2)
print(user.popitem())"""

#tuples
"""my_tuples=(1,2,3,4,5)
print(5 in my_tuples)
print(len(my_tuples))"""

#sets 
"""my_list=[1,2,3,4,5,5]
print(set(my_list )) 
my_set={1,2,3,4,5}
my_set.add(100)
my_set.add(2)
print(my_set)
types of set google it for more""" 









