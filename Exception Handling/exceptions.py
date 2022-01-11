'''
Exceptions:
An exception is an event, which occurs during the execution of a program that disrupts the normal flow of the program's instructions. ... An exception is a Python object that represents an error. When a Python script raises an exception,
it must either handle the exception immediately otherwise it terminates and quits.
'''

'''
Exception Handling:
Purpose of handling errors is to make program efficient. When there is error in the program it will display message to
user and continue execution. When the errors can be handled, they are called exceptions.
'''

'''
Blocks:
try ------> possibility of exceptions, even if some exception occurs inside it, program will be terminated.
except ---> write the 'except' block where we should display the exception details to the user.when excep occurs
it jumps into except block.
finally ---> we should perform some cleanup actions like closing the files and terminating other processes.
specialty of finally block is it will executed irrespective of whether there is exception or not.
'''
'''try:
   # do something
   pass

except ValueError:
   # handle ValueError exception
   pass

except (TypeError, ZeroDivisionError):
   # handle multiple exceptions
   # TypeError and ZeroDivisionError
   pass

except:
   # handle all other exceptions
   pass'''

'''try:
    date = eval(input("Enter Date:"))
except SyntaxError:
    print("Invalid date Entered")
else:
    print('You Entered:', date)
'''

'''Output:
Enter Date: 2021, 10, 1
You Entered: (2021, 10, 1)

Enter Date:2021, 10b, 3
Invalid date Entered
'''

def avg(list):
    tot = 0
    for x in list:
        tot += x
    avg = tot/len(list)
    return tot, avg
try:
    t,a = avg([1,2,3,4,5,'a'])
    print('total = {}, Average = {}'.format(t,a))
except TypeError:
    print('type error provide numbers')
except ZeroDivisionError:
    print("zerodivisionerror, do not give empty list")


# try without except block

try:
    x = int(input("Enter a NUmber:"))
    y = 1/x
finally:
    print("We are not catching the exception")
print("The inverse is:", y)

try:
    num = int(input("Enter a number: "))
    assert num % 2 == 0
except:
    print("Not an even number!")
else:
    reciprocal = 1/num
    print(reciprocal)

'''Output:
Output

If we pass an odd number:

Enter a number: 1
Not an even number!
If we pass an even number, the reciprocal is computed and displayed.

Enter a number: 4
0.25
However, if we pass 0, we get ZeroDivisionError as the code block inside else is not handled by preceding except.

Enter a number: 0
Traceback (most recent call last):
  File "<string>", line 7, in <module>
    reciprocal = 1/num
ZeroDivisionError: division by zero
'''