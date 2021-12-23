# P01. REQ : Check whether the list is empty or not

"""
1. CRUD
2. STATE      - Data types/structures
3. BEHAVIOR   - DTS / Operators / DM or Loops
"""
'''
1. CRUD       -->  update
2. STATE      -->  List
3. BEHAVIOR   -->  display  |  for  |   for   
'''

# 0. Mathematics
'''
1. First implement the solution on the paper 
2. write a list 
3. check whether there is any elements present.
4. write down the result according to that
'''

# 1.Builtin functions
print("-----1. Builtin Functions--------")
list1 = []
li2 = bool(list1)
print(li2)
print("False means List is Empty")


# 2. Algorithm
print("--------2. Algorithm----------")
list1 = []
if len(list1) == 0:
    print("List is Empty")
else:
    print("List is not Empty")






# 3 Using Functions
print("--------3. Functions----------")
def empty():
    list1 = []
    if len(list1) == 0:
        print("List is Empty")
    else:
        print("List is not Empty")
empty()

def empty1(li1):
    if len(li1) == 0:
        print("List is Empty")
    else:
        print("List is not Empty")
empty1([1, 2, 3, 4])





# 4 OOPS
print("--------4 Object Oriented----------")

# 5 Exception handling
print("--------5 Exception handling----------")

# 6 File Handling
print("--------6 File Handling----------")

# 7 Database interaction MVC
print("--------7 Database interaction----------")

# 8 UI Interaction
print("--------8 UI Interaction----------")