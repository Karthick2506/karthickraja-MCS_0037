# P01. REQ : Map two lists into a dictionary

"""
1. CRUD
2. STATE      - Data types/structures
3. BEHAVIOR   - DTS / Operators / DM or Loops
"""
'''
1. CRUD       -->  update
2. STATE      -->  Dictionary 
3. BEHAVIOR   -->  display  |  for  |   for   
'''

# 0. Mathematics
'''
1. First implement the solution on the paper. 
2. Take two dictionaries with keys and values.
3. Map the dictionaries values and keys.
4. Write down the result

'''

# 1.Builtin functions
print("-----1. Builtin Functions--------")
li1 = [1, 2, 3, 4]
li2 = ['Karthick', 'Raja', 'Arun', 'Kumar']
di1= dict(zip(li1, li2))
print("The Dictionary is:", di1)



# 2. Algorithm
print("--------2. Algorithm----------")
li1 = [1, 2, 3, 4]
li2 = ['Karthick', 'Raja', 'Arun', 'Kumar']
output = {li1[i]:li2[i] for i in range(len(li1))}
print("The Dictionary is:", output)


# 3 Using Functions
print("--------3. Functions----------")
def mapp():
    li1 = [1, 2, 3, 4]
    li2 = ['Karthick', 'Raja', 'Arun', 'Kumar']
    di1 = dict(zip(li1, li2))
    print("The Dictionary is:", di1)
mapp()

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