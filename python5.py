#Decorators
"""def hello(func):
    func()
def greet():
    print('still here!')
a=hello(greet)
print(hello('A'))"""
#Hight Order Function HOC
"""def greet(func):
    func()

def greet2():
    def func():
        return 5
    return func"""

#creating decorator
"""def my_decorator(func):
    def wrap_func(*a,**b): #use *args, **kwargs
        func(*a,**b)
    return wrap_func

@my_decorator
def helllo(greeting, emoji=':('):
    print(greeting, emoji)

helllo('heelllllooooo')

def my_decorator(func):
    def wrap_func():
        print('*******')
        func()
        print('********')
    return wrap_func

@my_decorator
def hello():
    print('Hello')

print(hello())"""

#why we need decorators
"""from time import time
def performance(fn):
    def wrapper(*a,**b):
        t1=time()
        result = fn(*a,**b)
        t2=time()
        print(f'it took {t2-t1} s')
        return result
    return wrapper

@performance 
def long_time():
    for i in range(100):
        i*5

long_time()"""