import random


def get_choices():
    player_choice =input("Enter a choice (rock, paper, scissors): ")
    options = ["rock", "paper", "scissors"]
    computer_choice = random.choice(options)
    choices = {"player": player_choice, "computer": computer_choice}
    return choices

def check_win(player, computer):
    # print("You chose: "+ player + " computer chose: "+ computer)
    print(f"You chose: {player} and computer chose: {computer}")
    if player == computer:
        return "It's a tie!"
    elif player == "rock":
        if computer == "scissors":
         return "Rock beats scissors. You are the winner!"
        else:
            return "Paper beats rocks. You Lose!"
        
    elif player == "paper":
        if computer == "scissors":
         return "Scissors beats paper. You Lose!"
        else:
            return "Paper beats rocks. You Win!"
    
    elif player == "scissors":
        if computer == "rock":
         return "Rock beats scissors. You Lose!"
        else:
            return "Scissors beats paper. You Win!"
    

choices = get_choices()

result = check_win(choices["player"], choices["computer"])
print(result)