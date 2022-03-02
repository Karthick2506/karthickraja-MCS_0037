s = 'django'
#d
#o
#djan
#jan
#go

print(s[0])
print(s[-1])
print(s[:4])
print(s[1:4])
print(s[4:])
print(s[::-1])

l = [3,7,[1,4,'hello']]
#reassign hello to goodbye
l[2][2] = 'goodbye'
print(l)

d1 = {'simple_key':'hello'}
d2 = {'k1':{'k2':'hello'}}
d3 = {'k1':[{'nest_key':['this is deep',['hello']]}]}

print(d1['simple_key'])
print(d2['k1']['k2'])
print(d3['k1'][0]['nest_key'][1])


mylist = [1,1,1,1,2,2,2,2,3,3,3,3]
print(set(mylist))


# For example:

# arrayCheck([1, 1, 2, 3, 1]) → True
# arrayCheck([1, 1, 2, 4, 1]) → False
# arrayCheck([1, 1, 2, 1, 2, 3]) → True

def arrayCheck(nums):


    for i in range(len(nums)-2):

        if nums[i]==1 and nums[i+1]==2 and nums[i+2]==3:
            return True
    return False

res = arrayCheck([1,2,3,3,1])
print(res)


def doubleChar(str):
  result = ''
  for char in str:
    result += char * 2
  return result

out = doubleChar("The")
print(out)


#Return the number of even integers in the given array.

def even(num):
    count = 0
    for element in num:
        if element % 2==0:
            count += 1
        return count



output = even([2,1,2,3,4])
print(output)