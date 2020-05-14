#Rock, Paper, Scissors App

import random

print("Welcome to Rock, Paper, Scissors! ")
total_rounds = int(input("\nHow many rounds would you like to play? "))
moves = ['rock','paper','scissors']
player_score = 0
computer_score = 0

for round_number in list(range(1,total_rounds+1)):
    print("Round " + str(round_number))
    print("Player: " + str(player_score) + "\tCompter: " + str(computer_score))
    player_choice = input("Would you like to pick rock, paper, or scissors? ").lower()
    choice_number = random.randint(0,2)
    computer_choice = moves[choice_number]
    print("Computer: "+ computer_choice)
    print("Player: " + player_choice)
    if computer_choice == player_choice:
        winner = 'tie'
    elif computer_choice == 'rock':
        if player_choice == 'paper':
            winner = 'player'
        elif player_choice == 'scissors':
            winner = 'computer'
    elif computer_choice == 'paper':
        if player_choice == 'scissors':
            winner = 'player'
        elif player_choice == 'rock':
            winner = 'computer'
    elif computer_choice == 'scissors':
        if player_choice == 'rock':
            winner = 'player'
        elif player_choice == 'paper':
            winner = 'computer'
    if winner == 'tie':
        print("It was a tie.")
    elif winner == 'player':
        print("You won this round!")
        player_score +=1
    elif winner == 'computer':
        print("You lost this round!")
        computer_score += 1
print("\nFinal Game Results")
print("\tRounds Played:\t" + str(total_rounds))
print("\tPlayer Score:\t" +str(player_score))
print("\tComputer Score:\t" + str(computer_score))

if player_score == computer_score:
    print("\tWinner:\tNobody")
elif player_score > computer_score:
    print("\tWinner:\tYou")
elif player_score < computer_score:
    print("\tWinner:\tComputer")
