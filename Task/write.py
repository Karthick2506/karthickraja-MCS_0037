"""a = input("Enter Your name")
b = input("Enter Your age")
c = input("Enter Your mobile no")
aa = open("details", "w")
aa.write(a)
aa.write(b)
aa.write(c)
print("File Saved")
aa.close()"""

bb = open("details", "r")
print("Is this File is in Read Mode", bb.readable())
print("Is this File is in Write Mode", bb.writable())
bb.close()
