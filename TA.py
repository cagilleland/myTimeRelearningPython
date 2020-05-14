#Thesaurus App

import random

thesaurus = {
    "hot" : ['balmy','summery','boiling'],
    "cold" :['chilly','cool','frigid'],
    "happy":['content','merry','cheery'],
    "sad" : ['unhappy','glum','miserable']
    }
print("Welcome to the Thesaurus\n\n Choose a word from below and I will give you a synonym.\n\nHere are the words in the thesaurus: ")
for k in thesaurus.keys():
    print("\t-"  + k )
choice = input("\nWhat word would you like a synonym for? ").lower().strip()
if choice in thesaurus.keys():
    index = random.randint(0,2)
    print("\nA synonym for " + choice + " is " + thesaurus[choice][index])
else:
    print("\nI'm sorry that word is not currently in the thesaurus")

choice = input("\nWould you like to see the whole thesaurus? ").lower().strip()
if choice.startswith('y'):
    for k,v in thesaurus.items():
        print("\n" + k.title())
        for value in v:
            print("\t-" + value)
else:
    print("Have a good day")
