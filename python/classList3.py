import os.path
import sys
print(sys.version)

action = input("Would you like to read the class to file? Enter Y or N: ")
if (action == "Y"):
    fileName = os.path.join("D:\\Data\\clients\\screen4\\tutorials\\python\\", "Class4B.txt")

    class4B = []

    classFile = open(fileName, 'r')
    for line in classFile:
        student = line.rstrip()
        print(student)
        class4B.append(student)
    classFile.close()

    print("All students", class4B)

    #variant  - what does := do? walrus operator
    #with - no need to close ?
    #with open(fileName) as file:
    #    while line := file.readline():
    #        print(line.rstrip())


   