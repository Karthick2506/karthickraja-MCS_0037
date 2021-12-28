# P03. REQ : Reverse list of elements and print in upper case

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
2. write a list.
3. reverse the elements and write it in upper case



'''

# 1.Builtin functions
print("-----1. Builtin Functions--------")
li1 = 'hello'
print("Before reversing", li1)
print("After Reversing", li1[::-1])

# 2. Algorithm
print("--------2. Algorithm----------")
li2 = ['hello', 'world']
print("Before Reversing", li2)
li3 = []
for a in li2:
    li3.append(a[::-1])
print(li3)


# 3 Using Functions
print("--------3. Functions----------")
def func():
    li2 = ['hello', 'world']
    print("Before Reversing", li2)
    li3 = []
    for a in li2:
        li3.append(a[::-1])
    print(li3)
func()

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