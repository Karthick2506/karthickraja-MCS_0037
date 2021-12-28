# P01. REQ : to print the following floating numbers upto 2 decimal places

"""
1. CRUD
2. STATE      - Data types/structures
3. BEHAVIOR   - DTS / Operators / DM or Loops
"""
'''
1. CRUD       -->  retrieve
2. STATE      -->  float 
3. BEHAVIOR   -->  display  |  for  |   for   
'''

# 0. Mathematics
'''
1. First implement the solution on the paper 
2. assign or take a float integer
3. write down the float value after decimal point (two numbers)
'''

# 1.Builtin functions

print("-----1. Builtin Functions--------")


float_num = float(input("Enter a Number"))
float_output = "{:.2f}".format(float_num)
print("The output is:", float_output)







# 2. Algorithm

print("--------2. Algorithm----------")
float_num1 = float(input("Enter a Number"))
float_output1 = "{:.2f}".format(float_num1)
print("The output is:", float_output1)





# 3 Using Functions
print("--------3. Functions----------")
def float_convert():
    float_num2 = float(input("Enter a Number"))
    float_output2 = "{:.2f}".format(float_num2)
    print("The output is:", float_output2)
float_convert()
















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