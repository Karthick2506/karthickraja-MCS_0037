'''The Assert statement'''

# Assert statement is useful to ensure that a given condition is true. If it is not true, it raises AssertionError.

# Syntax:
# assert condition, message


'''try:
    x = int(input("Enter a number between 5 and 10"))
    assert x>=5 and x<=10
    print("The number entered", x)
except AssertionError:
    print('The condition is not fulfilled')'''

'''Output
Enter a number between 5 and 10 7
The number entered 7

Enter a number between 5 and 10 15
The condition is not fulfilled
'''

try:
    x = int(input("Enter a number between 5 and 10"))
    assert x>=5 and x<=10, "your input is not correct"
    print("The number entered", x)
except AssertionError as obj:
    print(obj)

'''Output
Enter a number between 5 and 10 15
your input is not correct'''