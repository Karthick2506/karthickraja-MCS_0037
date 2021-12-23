# P01. REQ : To sort (ascending and descending) a dictionary by value

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
3. Arrange it in ascending and descending order based on the values in the dictionaries.
4. Write down the result

'''

# 1.Builtin functions
print("-----1. Builtin Functions--------")
dict1 = {'a': 15, 'b': 10, 'c': 13}
dict2 = sorted ([(value, key) for (key, value) in dict1.items()])
print(dict2)






# 2. Algorithm
print("--------2. Algorithm----------")
dict1 = {'a': 15, 'b': 10, 'c': 13}
li = list(dict1.items())
li.sort()
print("Ascending order based on values is:", li)
li.sort(reverse=True)
print("Descending order based on values is:", li)

# 3 Using Functions
print("--------3. Functions----------")
def sor():
    dict1 = {'a': 15, 'b': 10, 'c': 13}
    dict2 = sorted([(value, key) for (key, value) in dict1.items()])
    print("After Sorting based on values:", dict2)
sor()

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