# P07. REQ : Get maximum and minimum values in a dictionary

"""
1. CRUD
2. STATE      - Data types/structures
3. BEHAVIOR   - DTS / Operators / DM or Loops
"""
'''
1. CRUD       -->  retrieve
2. STATE      -->  Dictionary 
3. BEHAVIOR   -->  display  |  for  |   for   
'''

# 0. Mathematics
'''
1. First implement the solution on the paper. 
2. write down the dictionary with keys and values.
3. Write down the least value and big value from that dictionary.

'''

# 1.Builtin functions
print("-----1. Builtin Functions--------")
a = {"A": 100, "B": 200, "C": 300, "D": 400}
ma = max(a.values())
mi = min(a.values())

print("Maximum Value in the Dictionary is:", ma)
print("Minimum Value in the Dictionary is:", mi)



# 2. Algorithm
print("--------2. Algorithm----------")
a = {"A": 100, "B": 200, "C": 300, "D": 400}
li1 = []
for i in a.values():
    li1.append(i)
print(li1)
largest_no = li1[0]
for i in range (1, len(li1)):
    if li1[i] > largest_no:
        largest_no = li1[i]
print("The Largest value in the list is:", largest_no)
small_no = li1[0]
for i in range (1, len(li1)):
    if li1[i] < small_no:
        small_no = li1[i]
print("The Largest value in the list is:", small_no)


# 3 Using Functions
print("--------3. Functions----------")
def val():
    a = {"A": 100, "B": 200, "C": 300, "D": 400}
    li1 = []
    for i in a.values():
        li1.append(i)
    print(li1)
    largest_no = li1[0]
    for i in range(1, len(li1)):
        if li1[i] > largest_no:
            largest_no = li1[i]
    print("The Largest value in the list is:", largest_no)
    small_no = li1[0]
    for i in range(1, len(li1)):
        if li1[i] < small_no:
            small_no = li1[i]
    print("The Largest value in the list is:", small_no)
val()




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