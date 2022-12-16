import random

def get_choices():
  player_choice = input("Enter a choice (rock, paper, scissors):")
  options = ["rock", "paper", "scissors"]
  computer_choice = random.choice(options)
  choices = {"player": player_choice, "computer": computer_choice}
  return choices

def check_win(player, computer):
  print(f"You chose {player}, computer chose {computer}")
  if player == computer:
    return "It's a tie!"
  elif player == "rock" and computer == "scissors":
    return "Rock smashes scissors! You win!"
  elif player == "rock" and computer == "paper":
    return "Paper covers rock :( you lose!"
  elif player == "paper" and computer == "rock":
    return "Paper covers rock! You win!"
  elif player == "paper" and computer == "scissors":
    return "The computer cut right through you! Damn computer!"
  elif player == "scissors" and computer == "rock":
    return "The computer smashed you! What the heck computer >:( "
  elif player == "scissors" and computer == "paper":
    return "You cut through that computer! You win!"

choices = get_choices()
result = check_win(choices["player"], choices["computer"]) 
print(result)

