#Coin Flip App

import random

print("Welcome to the Coin Flip App")

flip_amount = int(input("\nHow many times would you like  me to flip a coin? "))
flips = list(range(1,flip_amount+1))
show_result = input("Would you like to see each flip results? ").lower()

heads = 0
tails = 0

for i in flips:
    flip_int = random.randint(0,1)
    if flip_int == 0:
        heads += 1
        if show_result.startswith('y'):
            print("HEADS")
    else:
        tails += 1
        if show_result.startswith('y'):
            print("TAILS")
    if heads == tails:
        print("At " + str(i) + " flips, the amount of heads and tails were equal at " + str(heads) + " each.")

heads_percent = round((heads/flip_amount)*100,2)
tails_percent = round((tails/flip_amount)*100,2)

print("\n\nResults of flipping a coin " + str(flip_amount) + " times:")
print("\nSide\tCount\tPercentage")
print("Heads\t" + str(heads) + "/" + str(flip_amount) + "\t" + str(heads_percent) + "%")
print("Tails\t" + str(tails) + "/" + str(flip_amount) + "\t" + str(tails_percent) + "%")        
