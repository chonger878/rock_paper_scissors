import random

#Assuming that the player wants to keep playing the game
game = ["rock","paper", "scissors"]
answer = 'y'
while answer.casefold() != 'n':
    computer_move = random.choice(game)
    your_move = input("Choose rock, paper, or scissors: ")
    if computer_move == your_move.casefold():
        print("It's a tie.")
    elif((computer_move == 'rock') and your_move.casefold() == 'scissors') or \
        ((computer_move == 'scissors') and your_move.casefold() == 'paper') \
        or ((computer_move=='paper') and your_move.casefold() =='rock'):
            print("Computer wins")
    else:
        print("You won this round!")
    answer = input('Wanna play again? Type n to exit: ')