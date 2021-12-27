'''data = "This is Python program"
f = open("reverse.txt", "w")
f.write(data)
print("file Saved")
f.close()'''

aa = open("reverse.txt", "r")
b = aa.read()
print("The Content Present in the File")
print(b)
b = b.split(" ")
c = ""
for i in range(len(b)-1,-1,-1):
    c = c+b[i]+" "
print("The Content After Reversing the Sentence")
print(c)
c = c[::-1]
print("The Content After Reversing the Each Alphabets in the sentence")
print(c)
aa.close()
