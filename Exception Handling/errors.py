'''Errors in python program'''
'''
---> Compile-time errors

---> Runtime errors

---> Logical errors
'''

'''
Compile-time errors:

when we forgetting a colon in statements like if, while, for, def etc will result in compile-time errors. This will
raise SyntaxError.
'''

'''x = 1
if x == 1
    print("fine")


Output:
    if x == 1
             ^
SyntaxError: expected ':'
'''

'''
Python statements are written in blocks using proper indentation. The default number of spaces is 4. If there is a
change in this spaces or missing indentation. It will raise Indentation Error.
'''

'''x = 10
if x%2 == 0:
    print("Divisible by 2")
         print("x is even number")
    
output:
  print("x is even number")
IndentationError: unexpected indent'''

'''
Runtime Errors

When PVM cannot execute the byte code. It flags runtime error. Insufficient memory to store something or inability
of PVM to execute some statements comes under runtime errors. runtime errors are not detected by python compiler
only at the runtime they are detected.
'''

'''def concat(a,b):
    print(a+b)
concat('hello', 25)

output:
concat('hello', 25)
print(a+b)
TypeError: can only concatenate str (not "int") to str'''

# In the above case we are passing one string and one number. Since the datatypes are not same, PVM shows "TypeError"
# Type checking is done by PVM during runtime

'''a = ['apple', 'mango', 'orange']
print(a[4])

output:
print(a[4])
IndexError: list index out of range'''

# here list contains only three elements. The index of the elements is from 0 to 3. when we refer index 4.
# It will show IndexError during runtime.

'''
Logical Errors:

These errors depict flaws in the logic of program. Logical error not detected by python compiler or PVM. The 
programmer is solely responsible for them.
'''

'''def increment(sal):
    sal = sal*15/100
    return sal
sal = increment(5000.00)
print("Incremented salary is:", sal)'''




