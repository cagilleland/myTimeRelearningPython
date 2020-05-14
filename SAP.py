#Shipping Accounts Program

users = [ "cag", "fag", "gag", "bag", "jag"]
print("Welcome to the Shipping Accounts Program.")

username = input("What is your username? ").lower().strip()

if username in users:
    print("Hello " + username + ". Welcome back to your account.")
    print("Current shipping prices are as follows:")
    print("\nShipping order 0-100:\t\t $5.10 each")
    print("Shipping order 100-500:\t\t $5.00 each")
    print("Shipping order 500-1000:\t $4.95 each")
    print("Shipping order over 1000:\t $4.80 each")
    order = int(input("\nHow many items would you like to ship? "))
    if order < 100:
        price = round(order * 5.1,2)
    elif order < 500:
        price = round(order * 5.0,2)
    elif order < 1000:
        price = round(order * 4.95,2)
    else:
        price = round(order * 4.80,2)
    print("To ship " + str(order) + " items it will cost you $" + str(price) + " at poopy per item")

    confirm = input("Would you like to place this order? ").lower()
    if confirm.startswith('y'):
        print("Okay, shipping your " + str(order) + " items")
    else:
        print("Okay, no order is being shipped out at this time.")

else:
    print("Sorry,you do not have an account. Goodbye")
