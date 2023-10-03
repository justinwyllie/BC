#example one - only accept digits
n1 = ''

while not n1.isdigit():
    print("Enter only numbers please")
    n1 = input("Type a number: ")
   
print("You entered", n1)

#example two - keep getting user data until user enters a certain char (and fill a list)
shoppingList = [] #a list

print("Enter shopping list items and X when finished")
item = ''

while item != 'X':
    item = input("Enter item: ") 
    #do not enter 'X'
    if item != "X":
        shoppingList.append(item)

print("Shopping list", shoppingList)

