import json


dict1 = {
    "Name": "Sachin",
    "Rollno": 35,
    "CGPA": 8.0,
    "Contactnumber": "9878654432"
}

dict2 = {
    "Name": "Vinoth",
    "Rollno": 36,
    "CGPA": 8.2,
    "Contactnumber": "8940355676"
}


xx = json.dumps(dict1, indent=4)
xy = json.dumps(dict2, indent=4)

with open("content.json", "w") as outfile:
    outfile.write(xx)
    outfile.write(xy)