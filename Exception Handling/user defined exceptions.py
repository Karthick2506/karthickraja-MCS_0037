'''User Defined Exceptions'''

'''Like the built-in exceptions of python, programmer can also create his own exceptions called user-defined exceptions'''


class myException(Exception):
    def __init__(self, arg):
        self.msg = arg
# myexception class is the sub class for exception. class has constructor where variable 'msg' is defined.

'''
when we write a code. if we suspects possibility of exception, we can raise our own exception using raise statement
'''

# raise MyException('message')

