#Pyhtonagachi Creature Game

import random

class Creature():
    """Creating a class for a creature"""
    def __init__(self,name):
        self.name = name.title()
        self.hunger = 0
        self.boredom = 0
        self.tiredness = 0
        self.dirtiness = 0
        self.food = 2
        self.is_sleeping = False
        self.is_alive = True

    def eat(self):
        if self.food > 0:
            self.food -= 1
            num = random.randint(1,5)
            self.hunger -= num
            print(self.name + " ate a great meal.")
        else:
            print(self.name + " has no food.")

    def play(self):
        num = random.randint(0,2)
        print(self.name + " wants to play a game.\n")
        guess = int(input(self.name + " is thinking of the number 0, 1, or 2"))
        if guess == num:
            print("You guessed correctly!!!")
            self.boredom -=3
        else:
            print("You guessed incorrectly.......")
            self.boredom -=1
        if self.boredom < 0:
            self.boredom = 0

    def sleep(self):
        self.is_sleeping = True
        self.tiredness -= 3
        self.boredom -=2
        print( self.name + " is sleeping......")
        if self.tiredness < 0:
            self.tiredness = 0
        elif self.boredom < 0:
            self.boredom = 0

    def awake(self):
        num = random.randint(0,2)
        if not num:
            print(self.name + " has woken up!")
            self.is_sleeping = False
            self.boredom = 0
        else:
            print(self.name + " won't wake up....")
            self.sleep()

    def clean(self):
        self.dirtiness = 0
        print(self.name + " took a bath.")

    def forage(self):
        food_found = random.randint(0,4)
        self.food += food_found
        self.dirtiness += 2
        print(self.name + " has found " + str(food_found))

    def show_values(self):
        print("Name: " + self.name + "\nHunger: " + str(self.hunger) + "\nBoredom: " + str(self.boredom))
        print("Tiredness: " + str(self.tiredness) + "\nDirtiness: " + str(self.tiredness))
        print("Food Inventory: " + str(self.food) + "\nSleeping Status: " + str(self.is_sleeping))

    def increment_values(self,diff):
        self.hunger += random.randint(0,diff)
        if not self.is_sleeping:
            self.boredom += random.randint(0,diff)
            self.tiredness += random.randint(0,diff)
        self.dirtiness += random.randint(0,diff)

    def kill(self):
        if self.hunger >= 10:
            print(self.name + " starved to death.")
            self.is_alive = False
        elif self.dirtiness >= 10:
            print(self.name + " got an infection and died.")
            self.is_alive = False
        elif self.boredom >= 10:
            self.boredom = 10
            print(self.name + " got bored and is falling asleep....")
            self.is_sleeping = True
        elif self.tiredness >= 10:
            self.tiredness = 10
            print(self.name + " got sleepy and is falling asleep....")
            self.is_sleeping = True

def show_menu(creature):
    if creature.is_sleeping:
        choice = input("Press [6] to attempt to wake up: ")
        choice = '6'
    else:
        print("\nPress [1] to eat\nPress [2] to play\nPress [3] to sleep\nPress [4] to take a bath\nPress [5] to forage for food")
        choice = str(input("What would you like to do? "))
    return choice

def call_action(creature,choice):
    if choice == '1':
        creature.eat()
    elif choice == '2':
        creature.play()
    elif choice == '3':
        creature.sleep()
    elif choice == '4':
        creature.clean()
    elif choice == '5':
        creature.forage()
    elif choice == '6':
        creature.awake()
    else:
        print("Your choice was invalid.")

print("Welcome to the Pythonagachi Game!\n\n")
diff = int(input("\nWhat difficulty would you like to play at?(1-5) "))

if diff > 5:
    diff = 5
elif diff < 1:
    diff = 1

running = True
while running:
    name = input("\nWhat would you like to name your creature? ").lower().strip()
    player = Creature(name)
    rounds = 1
    while player.is_alive:
        print("\n------------------------------------------------------------------\n")
        print("Round #" + str(rounds))
        player.show_values()
        round_move = show_menu(player)
        call_action(player,round_move)
        print("\nRound #" + str(rounds) + " Summary: ")
        player.show_values()
        input("\nPress [ENTER] to continue.")
        player.increment_values(diff)
        player.kill()
        rounds += 1
    
    print("\nR.I.P.")
    print(player.name + " survived a total of " + str(rounds-1) + " rounds.")
    choice = input("Would you like to play again (y/n): ").lower()
    if choice != 'y':
        running = False
        print("Thank you for playing Pythonagachi!")
