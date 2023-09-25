import os.path
class4B = []

print(type(class4B))

print("Enter student names and X when finished")
studentName = ''

while studentName != 'X':
    studentName = input("Enter name: ")  
    class4B.append(studentName)

numberStudents = len(class4B)

print(f"There are now {numberStudents} students in Class 4B")

action = input("Would you like to save the class to file? Enter Y or N: cls")
if (action == "Y"):
    fileName = os.path.join("D:\\Data\\clients\\screen4\\tutorials\\python\\", "Class4B.txt")
    classFile = open(fileName, 'w')
    for item in class4B:
        classFile.write(item)
        classFile.write("\n")
    classFile.close()