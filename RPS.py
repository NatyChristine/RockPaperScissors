#Rock Paper Scissors game
import random

game = ("Rock", "Paper", "Scissors")
result = random.choice(game)

while True:
    player = input("Choose Rock, Paper or Scissors: ")
    player = player.capitalize()
    print(f"The computer choose: {result}, You choose: {player}")
    if player == result:
        print("DRAW!")
        break
    elif player == "Rock" and result == "Paper":
        print("YOU LOOSE!")
        break
    elif player == "Paper" and result == "Scissors":
        print("YOU LOOSE!")
        break
    elif player == "Scissors" and result == "Rock":
        print("YOU LOOSE!")
        break
    elif player == "Rock" and result == "Scissors":
        print("YOU WIN!")
        break
    elif player == "Paper" and result == "Rock":
        print("YOU WIN!")
        break
    elif player == "Scissors" and result == "Paper":
        print("YOU WIN!")
        break
    else:
        print("Please choose the correct value.")
        break