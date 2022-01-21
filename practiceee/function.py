'''
The included code stub will read an integer, n, from STDIN.

Without using any string methods, try to print the following:


Note that "" represents the consecutive values in between.

Example
 n=5

Print the string.
12345
'''


num = int(input("Enter Your Number"))
for i in range(1,num+1):
    print(i, end='')
    '''for a in range(0,num):
        if i == a:
            sum = i * a
            print(sum)'''