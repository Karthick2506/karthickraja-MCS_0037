'''
#built-in Decorators

1) @property

2) @classmethod

3) @staticmethod
'''

# Property Decorators
'''
decorator is a built-in decorator in Python which is helpful in defining the properties effortlessly without manually calling the inbuilt function property().
Which is used to return the property attributes of a class from the stated getter, setter and deleter as parameters.'''


# Before using property decorator
class Student:
    def __init__(self,name,grade):
        self.name = name
        self.grade = grade
        self.msg = self.name + " got grade " + self.grade

stud1 = Student("Karthick", "B")
stud1.grade = "A"
print("Name:", stud1.name)
print("Grade:", stud1.grade)
print(stud1.msg)
        
'''Output
Name: Karthick
Grade: A
Karthick got grade B
'''
'''if we change the value of an attribute of a class other attributes which are derived
from that class is not updated'''

# After Using Property Decorator

class Student:
    def __init__(self,name,grade):
        self.name = name
        self.grade = grade

    @property   
    def msg(self):       
        return self.name + " got grade " + self.grade

stud1 = Student("Karthick", "B")
stud1.grade = "A"
print("Name:", stud1.name)
print("Grade:", stud1.grade)
print(stud1.msg)

# Property decorator allow us to use a method as attribute 


# setter method

'''Setter method allows us to set the attribute values'''

class Student:
    def __init__(self,name,grade):
        self.name = name
        self.grade = grade

    @property   
    def msg(self):       
        return self.name + " got grade " + self.grade
    
    @msg.setter
    def msg(self,msg):
        sent = msg.split(" ")
        print(sent)
        self.name = sent[0]
        self.grade = sent[-1]
        

stud1 = Student("Karthick", "B")
stud1.msg = "Karthick got grade A"
print("Name:", stud1.name)
print("Grade:", stud1.grade)
print(stud1.msg)




#setter and getter


class Student:
    def __init__(self,marks):
        self.marks = marks
    def percent(self):
        return (self.__marks/600)*100

    @property
    def marks(self):
        print("Getting Value:", end= " ")
        return self.__marks
    @marks.setter
    def marks(self,value):
        if value<0 or value>600:
            print("cant set value stick to pervious value")
        else:
            print("Setting Value:", value)
            self.__marks = value
        
        
s = Student(400)
s.marks = 600
print(s.marks)
print(s.percent(),"%")


# Using Property method

class Student:
    def __init__(self,marks):
        self.marks = marks
    def percent(self):
        return (self.__marks/600)*100

    
    def getter(self):
        print("Getting Value:", end= " ")
        return self.__marks
    
    def setter(self,value):
        if value<0 or value>600:
            print("cant set value stick to pervious value")
        else:
            print("Setting Value:", value)
            self.__marks = value
    marks = property(getter,setter)    
        
s = Student(400)
s.marks = 600
print(s.marks)
print(s.percent(),"%")



#@classmethod and @staticmethod

'''
1) instance method

2) class method

3)static method

Instance Variable:

*Owned by the instance of the class
*For Each object, instance variable are different
*Instance variable will be defined inside the method
'''

class Student:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def msg(self):  #instance method
        print(self.name+" "+self.age)

print("object 1:")
s1 = Student("Karthick", "20")
print(s1.name)
print(s1.age)
s1.msg()
print("*****************")
print("object 2:")
s2 = Student("Kumar", "25")
print(s2.name)
print(s2.age)
s2.msg()
print("*****************")


'''Class variables are constructed withion class construction and
they are owned by the class itself and class variables'''

#Class Variable

class Student:
    clg_name = "ABC" #class variable within class outside the method
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def msg(self):  #instance method
        print(self.name+" "+self.age)

print("object 1:")
s1 = Student("Karthick", "20")
print(s1.name)
print(s1.age)
s1.msg()
#print(s1.clg_name) 
print(Student.clg_name)

'''Here in the above code class variable can be called using class name
and using the object created'''

# Class method

'''class method dont need self as the argument instead we pass class as a
argument that is passing cls as a parameters''' 

#Syntax 

'''
class ....:
    @classmethod
    def method_name(cls,....):
    -------
    --------
'''


class Student:

    def __init__(self,name,marks):
        self.name = name
        self.marks = marks
        

    def msg(self):
        print(self.name+ " got " + self.marks,"%")

    @classmethod
    def get_per(cls,name,marks):
        return cls(name,str((int(marks)/600)*100))
    


s1 = Student("sia","93")
marks ="560"
name= "sia"
s2 = Student.get_per(name,marks)
s2.msg()

# @staticmethod

'''In Static method there is no need of using any specific parameter
it works as regular function'''


'''
class xxx:
    @staticmethod
    def func_name(parameter):
    ---------

'''    

class Student:

    def __init__(self,name,marks):
        self.name = name
        self.marks = marks
        

    def msg(self):
        print(self.name+ " got " + self.marks,"%")

    @classmethod
    def get_per(cls,name,marks):
        return cls(name,str((int(marks)/600)*100))

    @staticmethod
    def get_age(age):
        if age<17:
            print("School")
        else:
            print("Not belong to school")


s1 = Student("sia","93")
marks ="560"
name= "sia"
s2 = Student.get_per(name,marks)
s2.msg()
student.get_age(16) 

'''Differnce between class method and static method:

1) Class method takes cls as first parameter, while static method need no
specific parameters

2) Static methods knows nothing about thr class state, whilw class methods
can access and modify class state

3) @classmethod decoratos are used to create class method, @static method
decorators are used to create static methods 




















