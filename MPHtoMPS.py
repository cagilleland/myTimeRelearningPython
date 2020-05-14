#Mile Per Hour conversion App

print("Welcome to the miles per hour conversion app.")

#collect user input
mph = float(input("\nWhat is your speed in mph? "))

#convert mph to mps
mps = round(mph * .4474,2)

print("Your speed in meters per second is " + str(mps))
