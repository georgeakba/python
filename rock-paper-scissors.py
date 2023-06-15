import random

choices = ("rock", "paper", "scissors")
computer_choice = random.choice(choices)

user_choice = input('Do you want - rock, paper, scissors?\n')

print("computer chose: " + computer_choice)

if computer_choice == user_choice:
    print('TIE')
elif user_choice == choices[0] and computer_choice == 'scissors':
    print('WIN')
elif user_choice == choices[1] and computer_choice == 'rock':
    print('WIN')
elif user_choice == choices[2] and computer_choice == 'paper':
    print('WIN')
else:
    print('You loose :( Computer wins :D')