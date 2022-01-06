'''
Decorators:
Decorators are used to modify the behaviour of function or class. In Decorators, functions are taken as the argument into another function and
then called inside the wrapper function.

Any Python Callable objects that is used to modify the function or class without disturbing that function

Types:
---> Function Decorators
---> Class Decorators


Function Decorator:

1) Nested Function
2) Function can return another function
3) Functions are reference
4) Functions are parameter

Decorator rules:

1) Need to take function as parameter
2) add functionality to function
3) function need to return another function
'''

# Nested Function:

def outer():
    n1=3
    def inner():
        n2=6
        res=n1+n2
        return res
    return inner   #function are reference

obj=outer()
print(obj())  # 9
print(obj.__name__) # inner

#passing function as parameter

def func1():
    print("This is function1")
def func2(fun):
    print("I am fun2 calling fun1()")
    fun()
func2(func1)


# Implementing Decorator without parameter

def strupper(func):
    def inner():
        str1=func()  # hello
        return str1.upper()
    return inner

@strupper
def printstr():
    return "Hello"

print(printstr()) # upper

'''obj = strupper(printstr) # Functions are reference
print(obj())'''


# Decorator with parameter

def divdec(fun):
    def inner(x,y):
        if y==0:
            return "give value greater than zero"
        return fun(x,y)
    return inner

@divdec
def div(a,b):
    return a/b
print(div(4,2))

def outer(expr):
    def upper_d(func):
        def inner():
            return func() + expr
        return inner
    return upper_d

@outer("Karthick")
def ordinary():
    return "good morning  "
print(ordinary())


# Multiple decorator in single function:

def upper_dec(func):
    def inner():
        str1 = func()
        return str1.upper()
    return inner

def split_dec(func):
    def wrapper():
        str2 = func()
        return str2.split()
    return wrapper

@split_dec
@upper_dec
def ordinary():
    return "good evening"
print(ordinary())

'''if the decorator order changes in the above pgm it will throw error
@upper_dec
@split_dec
here first the split_dec func will take place and it converts in to the list in list we cannot perform upper operation
so it will throw error
Correct order of decorator is
@split_dec
@upper_dec'''

# general decorator works on multiple functions

def div_decor(func):
     def inner(*args):
         list1 = []
         list1 = args[1:]
         for i in list1:
             if i==0:
                 return "Give Proper Input"
         return func(*args)
     return inner
        
       
@div_decor
def div1(a,b):
    return a/b

@div_decor
def div2(a,b,c):
    return a/b/c

print(div1(10,5))
print(div2(10,2,0))

# To print the original function name:

import functools
def dec(func):
    @functools.wraps(func)
    def inner():
        str1 = func()
        return str1.upper()
    return inner

@dec
def greet():
    return "good morning"

print(greet.__name__)



 








          


