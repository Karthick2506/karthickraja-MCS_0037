# P01. REQ : to format number with percentage

"""
1. CRUD
2. STATE      - Data types/structures
3. BEHAVIOR   - DTS / Operators / DM or Loops
"""
'''
1. CRUD       -->  update
2. STATE      -->  float 
3. BEHAVIOR   -->  display  |  for  |   for   
'''

# 0. Mathematics
'''
1. First implement the solution on the paper 
2. write down the numbers with comma seperator
'''

# 1.Builtin functions

print("-----1. Builtin Functions--------")


num = int(input("Enter a Number"))
percentage_output = "{:.0%}".format(num)
print("The output is:", percentage_output)







# 2. Algorithm

print("--------2. Algorithm----------")
num1 = int(input("Enter a Number"))
percentage_output1 = "{:.0%}".format(num1)
print("The output is:", percentage_output1)





# 3 Using Functions
print("--------3. Functions----------")
def percent_convert():
    percent_num2 = int(input("Enter a Number"))
    percent_output2 = "{:.0%}".format(percent_num2)
    print("The output is:", percent_output2)
percent_convert()
















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