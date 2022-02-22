'''def py_fun():
    return "Karthick"

obj = py_fun()
print(obj)  #---->Karthick
print(py_fun()) #---->Karthick'''


def outer():
    k = 3
    def inner():
        k1 = 2
        res = k+k1
        return res
    return inner()

ob = outer()
print(ob)

print("----Nested Function----")
def outer():
    k = 3
    def inner():
        k1 = 2
        def innermost():
            res = k + k1
            return res
        return innermost()
    return inner()

ob = outer()
print(ob)

print("----Passing function as a parameter----")

def func1():
    print("This is Function 1")
def func2(fun):
    print("I am fun2 calling fun1()")
    fun()
func2(func1)

def add():
    print("Addition")
def val(a,b):
    print(a+b)

val(1,2)

def fun(txt):
    result = txt("I am from Bangalore")
    return result

#function 1
def fun1(str):
    return str.lower()

#function 2
def fun2(str):
    return str.upper()

# passing function 1 as an argument to an fun() function
str1 = fun(fun1)
print(str1)

# passing function 2 as an argument to an fun() function
str2 = fun(fun2)
print(str2)

print("----Passing class method as argument----")

class demo:
    def method1(self):
        print('Method1 is running')
        return "Karthick"

    def method2(self,arg):
        print('Method2 is running')
        ress = arg()
        return ress

aa = demo()

bb = aa.method2(aa.method1)
print(bb)

print("----Decorator 1----")

def decorator_function(original_func):
    def wrapper_function():
        print("Wrapper executed before")
        return original_func()
    return wrapper_function

@decorator_function
def display():
    print("display function ran")

display()

#decorated_display = decorator_function(display)
#decorated_display()
print("----Decorator 2----")

def strupper(func):
    def inner():
        str1=func()  # hello
        return str1.upper()
    return inner

@strupper
def printstr():
    return "Hello"

print(printstr()) # upper

print("----Decorator 3----")

def upper_dec(func):
    def inner1():
        strr = func()
        return strr.upper()
    return inner1

def split_dec(func):
    def wrapper1():
        str2 = func()
        return str2.split()
    return wrapper1

@split_dec
@upper_dec #here this decorator operation takes place first
def display1():
    return "Hello World"
print(display1())

print("----Class Decorator----")

class Divide:
    def __init__(self,funcc):
        self.funcc = funcc
    def __call__(self, *args, **kwargs):
        li1 = []
        li1 = args[1:]
        for i in li1:
            if i == 0:
                return "Change the input"
            else:
                return self.funcc(*args, **kwargs)

@Divide
def div(a,b):
    return a/b


print(div(10,5))







