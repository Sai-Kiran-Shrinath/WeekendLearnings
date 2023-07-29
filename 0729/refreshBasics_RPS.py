import random


#Variables

player_choice = 'rock'
computer_choice = 'paper'

#Function

def get_choices():
    player_choice = input('Enter a choice: (rock, paper, scissors): ')
    options = ['rock', 'paper', 'scissors']
    computer_choice = random.choice(options)

    choices = {"player": player_choice, "computer": computer_choice}

    return choices

def check_win(player_choice, computer_choice):
    # print("You chose", player_choice, "\nComputer chose:", computer_choice)
    print(f"You chose {player_choice} \nComputer chose: {computer_choice}")

    if player_choice == computer_choice:
        print("Draw")
    elif player_choice == 'rock' and computer_choice == 'paper':
        print("Computer Win")
    elif player_choice == 'rock' and computer_choice == 'scissors':
        print('Player Win')
    elif player_choice == 'paper' and computer_choice == 'rock':
        print("Player Win")
    elif player_choice == 'paper' and computer_choice == 'scissors':
        print('Computer Win')
    elif player_choice == 'scissors' and computer_choice == 'rock':
        print("Computer Win")
    elif player_choice == 'scissors' and computer_choice == 'paper':
        print("Player Win")

def greeting():
    return "Hi"

response = greeting()
print(response)

choice = get_choices()
# print(choice)

result = check_win(choice['player'], choice['computer'])

#Dictionary

# dict = {"name": "sk", "color": "blue"}


#Lists

# food = ["biryani", "pizza", "sandwich"]
# dinner = random.choice(food)
# print("Lets have", dinner, "for Dinner")