classAges = []
className = ''

def averageAge():
    


className = input("Enter name of class: ")  


inputAge = ''

while inputAge != 'X':
    inputAge = input("Enter age of students one by one and press X when finished: ")  
    if (inputAge != 'X'):
        inputAge = int(inputAge)
        classAges.append(inputAge)

result = averageAge(classAges)
print(f"The average age of students in {className} is {result}")



