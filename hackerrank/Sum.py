'''
The list of non-negative integers that are less than n=3 is [0,1,2].
Print the square of each number on a separate line.

0
1
4
'''

'''nums = [2,7,11,15]
target = int(input("Enter the number"))
for i in nums:
    if nums[i] == target:
        print(nums[i])'''


num = int(input("Enter Your Number"))
for i in range(0,num):
    for a in range(0,num):
        if i == a:
            sum = i * a
            print(sum)



'''n = 2
a = n**n
print(a)'''

