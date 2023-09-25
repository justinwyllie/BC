def addTwo(n1, n2):
    result = int(n1) + int(n2)
    return result


n1 = input("Type a number: ")

if not n1.isdigit():
    print("Enter only numbers please")
    n1 = input("Type a number: ")

n2 = input("Type another number: ")

if not n2.isdigit():
    print("Enter only numbers please")
    n2 = input("Type a number: ")

sum = addTwo(n1, n2)

print("The sum is: ", sum)
