# P01. REQ : Find the highest 3 values in a dictionary.

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
dict1 = {'F': 67, 'E': 23, 'C': 45, 'D': 56, 'B': 12, 'A': 69}
output = sorted(dict1, key=dict1.get, reverse=True)[:3]
print("The Keys having the first Three high value:'", output)
output1 = sorted(dict1, key=dict1.get, reverse=False)[:3]
print("The Keys having the least Three high value:'", output1)




# 2. Algorithm
print("--------2. Algorithm----------")
dict1 = {'F': 67, 'E': 23, 'C': 45, 'D': 56, 'B': 12, 'A': 69}
val = dict1.values()
maxx = max(val)
print(maxx)



# 3 Using Functions
print("--------3. Functions----------")

def maxi():
    dict1 = {'F': 67, 'E': 23, 'C': 45, 'D': 56, 'B': 12, 'A': 69}
    output = sorted(dict1, key=dict1.get, reverse=True)[:3]
    print("The Keys having the first Three high value:'", output)
    output1 = sorted(dict1, key=dict1.get, reverse=False)[:3]
    print("The Keys having the least Three high value:'", output1)
maxi()



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