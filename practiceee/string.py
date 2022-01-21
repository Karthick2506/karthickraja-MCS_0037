'''st = input("Enter a String")
#a = st
if st.isalnum():
    print("True")
else:
    print("False")
if st.isalpha():
    print("True")
else:
    print("False")
if st.isdigit():
    print("True")
else:
    print("False")
if st.islower():
    print("True")
else:
    print("False")
if st.isupper():
    print("True")
else:
    print("False")'''

S = input("Enter a String")
a = 0
for i in range(len(S)):
    if S[i].isalnum():
        print(S[i].isalnum())
# if a > 0:
#     print ('True')
# else:
#     print ('False')
#
# a = 0
# for i in range(len(S)):
#     if S[i].isalpha():
#         a += 1
# if a > 0:
#     print ('True')
# else:
#     print ('False')
#
# a = 0
# for i in range(len(S)):
#     if S[i].isdigit():
#         a += 1
# if a > 0:
#     print ('True')
# else:
#     print ('False')

'''a = 0
for i in range(len(S)):
    if S[i].islower():
        a += 1
if a > 0:
    print ('True')
else:
    print ('False')

a = 0
for i in range(len(S)):
    if S[i].isupper():
        a += 1
if a > 0:
    print ('True')
else:
    print ('False')'''

