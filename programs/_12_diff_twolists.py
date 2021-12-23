# P01. REQ : Difference between two list

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
2. write a list in paper
3. write another list 
4. find the difference between two list.
5. write down the new list with differnce values
'''

# 1.Builtin functions
print("-----1. Builtin Functions--------")
li1 = [1,2,5,7,8]
li2 = [1,2,3,4,5]
set_diff = set(li1)-set(li2)
list_diff = list(set_diff)
print("The Difference between two list is:", list_diff)

# 2. Algorithm
print("--------2. Algorithm----------")
li1 = [1,2,5,7,8]
li2 = [1,2,3,4,5]
list_difference = []
for ele in li1:
    if ele not in li2:
        list_difference.append(ele)
print("The Difference between two list is:", list_difference)



# 3 Using Functions
print("--------3. Functions----------")
def diff():
    li1 = [1, 2, 5, 7, 8]
    li2 = [1, 2, 3, 4, 5]
    list_difference = []
    for ele in li1:
        if ele not in li2:
            list_difference.append(ele)
    print("The Difference between two list is:", list_difference)
diff()




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