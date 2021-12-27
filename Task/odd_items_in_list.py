# P01. REQ : Printing odd elements in the list

"""
1. CRUD
2. STATE      - Data types/structures
3. BEHAVIOR   - DTS / Operators / DM or Loops
"""
'''
1. CRUD       -->  retrieve
2. STATE      -->  List 
3. BEHAVIOR   -->  display  |  for  |   for   
'''

# 0. Mathematics
'''
1. First implement the solution on the paper 
2. write a list 
3. write down the odd elements separately in another List.
4. Write down the index value of a specified element.
'''

# 1.Builtin functions
print("-----1. Builtin Functions--------")

list1 = [1, 2, 3, 4, 77, 89, 88, 7]
print("The odd elements in the list are", list1[::2])






# 2. Algorithm
print("--------2. Algorithm----------")
list1 = [1, 2, 3, 4, 77, 89, 88, 7]
print("The Odd items in the List")
for i in list1:
    if i % 2 != 0:
        print(i)




# 3 Using Functions
print("--------3. Functions----------")
def oddd():
    list1 = [1, 2, 3, 4, 77, 89, 88, 7]
    print("The Odd items in the List")
    for i in list1:
        if i % 2 != 0:
            print(i)
oddd()














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