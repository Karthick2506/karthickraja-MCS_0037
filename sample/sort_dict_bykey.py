# P03. REQ : Reverse list of elements and print in upper case

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
1. First implement the solution on the paper 
2. write a dictionary with key and value.
3. sort it with key and write it.



'''

# 1.Builtin functions
print("-----1. Builtin Functions--------")
di1 = {1: 4, 2: 5, 4: 6, 3: 8}
print("Sorted based on Key", sorted(di1.keys()))


# 2. Algorithm
print("--------2. Algorithm----------")
di1 = {1: 4, 2: 5, 4: 6, 3: 8}
print("Values Sorted Based on Keys")
for i in sorted (di1):
    print(i, di1[i])


# 3 Using Functions
print("--------3. Functions----------")
def sortt():
    di1 = {1: 4, 2: 5, 4: 6, 3: 8}
    print("Values Sorted Based on Keys")
    for i in sorted(di1):
        print(i, di1[i])
sortt()

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