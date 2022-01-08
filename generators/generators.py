# Python generators

'''
There is a lot of work in building an iterator in Python. We have to implement a class with __iter__() and __next__() method,
keep track of internal states, and raise StopIteration when there are no values to be returned.

This is both lengthy and counterintuitive. Generator comes to the rescue in such situations.

Python generators are a simple way of creating iterators. All the work we mentioned above are automatically handled by generators in Python.

Simply speaking, a generator is a function that returns an object (iterator) which we can iterate over (one value at a time).'''


# Creating generators

'''
It is fairly simple to create a generator in Python. It is as easy as defining a normal function, but with a yield statement instead of a return statement.

If a function contains at least one yield statement (it may contain other yield or return statements), it becomes a generator function. Both yield and return will return some value from a function.

The difference is that while a return statement terminates a function entirely, yield statement pauses the function saving all its states and later
continues from there on successive calls.
'''

'''Generators dont hold the entire result in memory it yields
one result at a time'''




def square(numbers):
    for i in numbers:
        yield (i*i)

my_numbers = square([1,2,3,4,5])

for num in my_numbers:
    print(num)



def num_generator():
    a = 1
    b = 2
    c = a+b
    yield c
    yield a

var1=num_generator()
print(next(var1))
print(next(var1))
    
    
def demo():
    yield 5
a =demo()
print(a.__next__())


def sample():
    n = 1
    while n<=10:
        val = n*n
        yield val
        n += 1
aa = sample()
for i in aa:
    print(i)


def rev_str(my_str):
    length = len(my_str)
    for i in range(length - 1, -1, -1):
        yield my_str[i]


# For loop to reverse the string
for char in rev_str("hello"):
    print(char)

    




    
























