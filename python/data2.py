def addTwo(n1, n2):
    result = int(n1) + int(n2)
    return result


n1 = input("Type a number: ")

while not n1.isdigit():
    print("Enter only numbers please")
    n1 = input("Type a number: ")

n2 = input("Type another number: ")

while not n2.isdigit():
    print("Enter only numbers please")
    n2 = input("Type a number: ")



sum = addTwo(n1, n2)

print("The sum is: ", sum)


##simple example unit test for function addTwo 

def testAddTwo():
    print("Run Tests")
    testResult = addTwo(2, 2)
    #assertion
    if (testResult == 4):
        print("OK")
    else:
        print("TEST FAILED")

testAddTwo()