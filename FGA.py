#Factor Generation App

print("Welcome to the factor generation app.")

running = True

while running:
    user_number = int(input("What number would you like the factors for? "))
    factors = []
    for num in list(range(1,user_number+1)):
        remainder = user_number%num
        if not remainder:
            factors.append(num)
    print("\nThe factors of " + str(user_number) + " are:")
    for factor in factors:
        print(factor)
    for i in range(int(len(factors)/2)):
        print(str(factors[i]) + " * " + str(factors[-i-1]) + " = " + str(user_number))
    choice = input("Would you like to run again? ").lower().strip()
    if choice.startswith('n'):
        running = False

print("Thanks for running the program")
