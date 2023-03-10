import random

def get_choices():
  player_choice = input("Enter a choice (rock, paper or scissors): ")
  options = ["rock","paper", "scissors"]
  computer_choice = random.choice(options)
  choices = {"player": player_choice , "computer": computer_choice}
  
  return choices

def check_win(player, computer):
  print(f"You Chose: {player}, the computer chose: {computer} .")
  if player == computer:
    return "It's a tie!"
  elif player == "rock": 
    if computer == "scissors":
      return "Rock smashes scissors, YOU WIN!!!"
    else:
      return "Paper covers rock, YOU LOSE."
  elif player == "paper": 
    if computer == "rock":
      return "Paper covers rock, YOU WIN!!!"
    else:
        return "Paper gets cut by scissors, YOU LOSE."
  elif player == "scissors":
      if computer == "paper":
        return "Scissors cuts paper, YOU WIN!!!"
      else:
        return "Scissors gets smashed by rock, YOU LOSE."

# gets player & computer choice
choices = get_choices()
# gets key from dictionary
result = check_win(choices["player"], choices["computer"])
print(result)
