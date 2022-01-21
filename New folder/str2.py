'''
Task
Read a given string, change the character at a given index and then print the modified string.
Function Description

Complete the mutate_string function in the editor below.

mutate_string has the following parameters:

string string: the string to change
int position: the index to insert the character at
string character: the character to insert
Returns

string: the altered string
Input Format

The first line contains a string, string.
The next line contains an integer position, the index location and a string chracter, separated by a space.

Sample Input

STDIN           Function
-----           --------
abracadabra     s = 'abracadabra'
5 k             position = 5, character = 'k'
Sample Output

abrackdabra
'''

a = "abracadabra"
print("original string", a)
li = list(a)
li[5] = 'k'
a = ''.join(li)
print("String after converting", a)
