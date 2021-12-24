# P01. REQ : Append a List to second List

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
3. Assign the index value to each element in the list.
4. Write down the index value of a specified element
'''

# 1.Builtin functions
print("-----1. Builtin Functions--------")

list1 = [1,2,3,4,5,6]
list2= ['Karthick', 'Raja', 'Vinoth']
list2.extend(list1)
print(list2)

li1 = [1,2,3,4,5,6]
li2= ['Karthick', 'Raja', 'Vinoth']
li2.append(li1)
print(li2)



# 2. Algorithm
print("--------2. Algorithm----------")

list1 = [1,2,3,4,5,6]
list2= ['Karthick', 'Raja', 'Vinoth']
list3 = list1 + list2
print(list3)




# 3 Using Functions
print("--------3. Functions----------")

def merge():
    list1 = [1, 2, 3, 4, 5, 6]
    list2 = ['Karthick', 'Raja', 'Vinoth']
    list2.extend(list1)
    print(list2)
merge()











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