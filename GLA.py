#Grocery List App

import datetime

time = datetime.datetime.now()
month = str(time.month)
day = str(time.day)
hour = str(time.hour)
minute = str(time.minute)
grocery = [ "Meat", "Cheese"]

print("Welcome to the Grocery list app.")
print("The current date and time is:\t" + month + "/" + day + "\t" + hour + ":" + minute)
print("Your list currently has " + grocery[0] + " and " + grocery[1] + " in it.")

new_food = input("What food would you like to add to your list? ")
grocery.append(new_food.title())
new_food = input("What food would you like to add to your list? ")
grocery.append(new_food.title())
new_food = input("What food would you like to add to your list? ")
grocery.append(new_food.title())

print("Here is your grocery list:\n" + str(grocery))
grocery.sort()
print("Here is your grocery list sorted:\n" + str(grocery))

print("\nSimulating Grocery Shopping.........")
print("\nCurrent list length: " + str(len(grocery)))
print(grocery)
bought = input("What  food did you just buy? ").title()
grocery.remove(bought)
print("Removing " + bought + " from the list....")

print("\nCurrent list length: " + str(len(grocery)))
print(grocery)
bought = input("What  food did you just buy? ").title()
grocery.remove(bought)
print("Removing " + bought + " from the list....")

print("\nCurrent list length: " + str(len(grocery)))
print(grocery)
bought = input("What  food did you just buy? ").title()
grocery.remove(bought)
print("Removing " + bought + " from the list....")

print("\nCurrent list length: " + str(len(grocery)))
print(grocery)
out = grocery.pop()
print("\nSorry the store is out of " + out + ".")
new = input("What would you like to add instead of " + out + "? ").title()
grocery.insert(0, new)

print("\nHere is your grocery list: ")
print(grocery)
