import random


def getChoice():
    user_choice = input("Enter your choice(rock, paper, scissors):")
    options = ["rock", "paper", "scissors"]
    computer_choice = random.choice(options)
    choices = {"player": user_choice, "computer": computer_choice}

    return choices


def check_win(player, computer):
    print(f"You chose {player}, computer chose {computer}")
    if player == computer:
        return "It's a tie!"
    elif player == "rock":
        if computer == "scissors":
            return "Rock smashes scissors! You win!"
        else:
            return "Paper covers rock! You Lose"
    elif player == "paper":
        if computer == "rock":
            return "Paper covers rock! you win!"
        else:
            return "Scissors cuts paper! You lose!"
    elif player == "scissors":
        if computer == "paper":
            return "Scissors cuts paper! you win!"
        else:
            return "Rock smashes scissors! You lose!"


choice = getChoice()

result = check_win(choice["player"], choice["computer"])
print(result)
