# P01. REQ : Shuffle the List and print the list

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
2. write a list a in paper 
3. change the position of the value in a random manner.
4. write down the new list
'''

# 1.Builtin functions
print("-----1. Builtin Functions--------")
li1 = [1,2,3,4,5,6,7,8,9,10]
print("Original list:", li1)
li1.sort(reverse = True)
print("List After shuffling:", li1)






# 2. Algorithm
print("--------2. Algorithm----------")
li1 = [1,2,3,4,5,6,7,8,9,10]
print("Original list:", li1)
li2 = []
for i in li1:
    li2.append(i)
li2.sort(reverse = True)
print("List After shuffling:", li2)




# 3 Using Functions
print("--------3. Functions----------")
def shuff():
    li1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print("Original list:", li1)
    li2 = []
    for i in li1:
        li2.append(i)
    li2.sort(reverse=True)
    print("List After shuffling:", li2)
shuff()






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