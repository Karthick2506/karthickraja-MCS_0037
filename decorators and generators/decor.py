# Class Decorators

'''
decorator as a class in order to do that, we have to use a __call__ method of classes. When a user needs to create an object that acts as a function then function decorator needs to return an object that acts like a function,
so __call__ can be useful'''

def decorator(func):
    def inner():
        str1=func()
        return str1.upper()
    return inner

@decorator
def greet():
    return "good morning"

print(greet.__name__)  # it will print output as inner

'''In order to know the original function name. the changes to be made

import functools
def decorator(func):
    @functools.wraps(func)      # it will print output as greet'''


# decorator function on methods
def check_name(method):
    def inner(name_ref):
        if name_ref.name == "Karthick":
            print("Same Name")
        else:
            method(name_ref)
    return inner       


class Printing:
    def __init__(self,name):
        self.name = name
    @check_name
    def print_name(self):
        print("Entered user name is:", self.name)

p = Printing("Karthick")
p.print_name()
 
'''In class decorators __call__ method is important
It is used call a object in function form'''

'''Class decorator'''

class Check_div:
    def __init__(self,func):
        self.func = func
    def __call__(self,*args,**kwargs):
        list1 = []
        list1 = args[1:]
        for i in list1:
            if i==0:
                return "Change the input"
        else:
            return self.func(*args,**kwargs)
            
@Check_div
def div(a,b):
    return a/b

@Check_div
def div1(a,b,c):
    return a/b/c

print(div(10,5))
print(div(10,10,5))


#built-in Decorators

1) @property

2) @classmethod

3) @staticmethod

'''if we change the value of an attribute of a class other attributes which are derived
from that class is not updated'''
 



 


































