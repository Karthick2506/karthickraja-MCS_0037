# P04. REQ : Merge Two Dictionaries

"""
1. CRUD
2. STATE      - Data types/structures
3. BEHAVIOR   - DTS / Operators / DM or Loops
"""
import math

'''
1. CRUD       -->  update
2. STATE      -->  Dictionary 
3. BEHAVIOR   -->  display  |  for  |   for   
'''

# 0. Mathematics
'''
1. First implement the solution on the paper. 
2. write two dictionaries with different keys and values.
3. Merge those two dictionaries and write down as single dictionary.

'''

# 1.Builtin functions
print("-----1. Builtin Functions--------")



dict1 = {"player": "Sachin", "Team": "India"}
print("Dict1 Before Merging:", dict1)
dict2 = {"Runs": 150, "Boundaries": 10}
print("Dict2 Before Merging:", dict2)
dict3 = dict1.copy()
dict3.update(dict2)
print("After merging two dictionaries:", dict3)


# 2. Algorithm
print("--------2. Algorithm----------")
di1 = {"player": "Sachin", "Team": "India"}
print("Dict1 Before Merging:", dict1)
di2 = {"Runs": 150, "Boundaries": 10}
print("Dict2 Before Merging:", dict2)
di3 = di1.copy()
for key,value in di2.items():
    di3[key] = value
print("After Merging Two Dictionaries:", di3)



# 3 Using Functions
print("--------3. Functions----------")

def merge():
    di1 = {"player": "Sachin", "Team": "India"}
    print("Dict1 Before Merging:", dict1)
    di2 = {"Runs": 150, "Boundaries": 10}
    print("Dict2 Before Merging:", dict2)
    di3 = di1.copy()
    for key, value in di2.items():
        di3[key] = value
    print("After Merging Two Dictionaries:", di3)
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