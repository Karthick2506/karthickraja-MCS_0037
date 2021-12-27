f = open("text.txt", "r")
# the second parameter of the seek method is by default 0
f.seek(100)
# now, we will print the current position
print("current position: ", f.tell())

print("pointer will start at next position:", f.readline())
print(f.readlines())
f.close()


fi = open("text.txt", "r+")
print("Name of the file: ", fi.name)

line_1 = fi.readline()
print("Read Line: %s" % line_1)

# Again, set the pointer to the beginning
fi.seek(0, 2)
line_2 = fi.readline()
print("Read Line: %s" % line_2)

# Close open file
fi.close()


print("__negative offset__")
fi = open("text.txt", "rb")

# the user is setting the reference point to thirtieth position to the left from
# end
fi.seek(-70, 2)

# now print the current position
print(fi.tell())

# now the user will Convert the binary to string
print(fi.readline().decode('utf-8'))

fi.close()
