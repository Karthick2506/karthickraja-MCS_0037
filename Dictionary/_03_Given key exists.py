# P03. REQ : Check whether the given key already exists or not

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
2. write a dictionary with key and values.
3. Check whether the key exists or not and write the result.

'''

# 1.Builtin functions
print("-----1. Builtin Functions--------")



# 2. Algorithm
print("--------2. Algorithm----------")
dict1 = {
  "brand": "MRF",
  "wood": "Willow",
  "year": 1995
}
if "brand" in dict1:
    print("The key brand is present in the dictionary")
else:
    print("The key brand is not present in the dictionary")



# 3 Using Functions
print("--------3. Functions----------")

def checkk():
    dict1 = {
        "brand": "MRF",
        "wood": "Willow",
        "year": 1995
    }
    if "player" in dict1:
        print("The key player is present in the dictionary")
    else:
        print("The key player is not present in the dictionary")
checkk()







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