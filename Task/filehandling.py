print("1. Write")
print("1. Read")
ch = int(input("Enter your Choice"))
if (ch==1):
    fname = input("Enter the File Name")
    fdata = input("Enter the Content")
    f = open(fname, "w")
    f.write(fdata)
    print("File Saved...")
    f.close()
elif (ch==2):
    fname= input("Enter file name")
    f = open(fname, "r")
    data = f.read()
    print(data)
    f.close()
else:
    print("Invalid choice")