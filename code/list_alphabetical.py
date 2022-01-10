# P01. REQ : Sort a list in Alphabetical Order.

"""
1. CRUD
2. STATE      - Data types/structures
3. BEHAVIOR   - DTS / Operators / DM or Loops
"""
'''
1. CRUD       -->  Retrieval
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
num ={
    "L1":["for", "pulse", "python"],
    "L2":["geological", "computer", "science"],
    "L3":["website", "for", "students"],
}
print("Before Sorting")
for i in num.items():
    print(i)
print("After Sorting")
for i,j in num.items():
    sor = {i:sorted(j)}
    print(sor)

# 2. Algorithm
print("--------2. Algorithm----------")

# 3 Using Functions
print("--------3. Functions----------")

def ide():
    num = {
        "L1": ["for", "pulse", "python"],
        "L2": ["geological", "computer", "science"],
        "L3": ["website", "for", "students"],
    }
    print("Before Sorting")
    for i in num.items():
        print(i)
    print("After Sorting")
    for i, j in num.items():
        sor = {i: sorted(j)}
        print(sor)
ide()




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