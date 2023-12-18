classAges = []



def averageAge(classAges):


    total = 0
    for age in classAges:
        total = total + age
    result = total / len(classAges)


    
    return result


className = input("Enter name of class: ")  


inputAge = ''

while inputAge != 'x':
    inputAge = input("Enter age then x ")  
    if (inputAge != 'x'): 
        inputAge = int(inputAge)
        classAges.append(inputAge)

result = averageAge(classAges)
print(f"The average age of students in {className} is {result}")



