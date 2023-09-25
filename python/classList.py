class4B = []

print(type(class4B))

print("Enter student names and X when finished")
studentName = ''

while studentName != 'X':
    studentName = input("Enter name: ")  
    class4B.append(studentName)

numberStudents = len(class4B)

print(f"There are now {numberStudents} students in Class 4B")