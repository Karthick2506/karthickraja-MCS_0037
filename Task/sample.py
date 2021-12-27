'''from csv import *
h = ["Name", "id", "Department", "YOP"]
d = [["Karthick", 555, "EIE", 2018], ["Vinoth", 787, "CSE", 2017], ["Sathish", 100, "Mechanical", 2016]]
f = open("std.csv", "w", newline="")
c = writer(f)
c.writerow(h)
c.writerow(d)
print("Student Info Added")
f.close()'''

from csv import *
a = input("Enter Product Name")
b = input("Enter Product Brand")
c = input("Enter Product Price")
data1 = list(a)
data2 = list(b)
data3 = list(c)
ff = open("data.csv", "w", newline="")
k = writer(ff)
k.writerow(a) #data1 saved
k.writerow(b) #data2 saved
k.writerow(c) #data3 saved
print("Product Info Added and Saved")
ff.close()
