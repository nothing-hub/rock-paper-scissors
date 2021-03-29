# we wana to build a game
import random

print("rock......")
print("paper......")
print("scissors......")


randomNumber = random.randint(0, 2)
computerMove = "rock"
if randomNumber == 0:
    computerMove = "rock"
elif randomNumber == 1:
    computerMove = "paper"
elif randomNumber == 2:
    computerMove = "scissors"
conpyterMove = "rock"
player1_wins = 0
player2_wins = 0
wining_score = 4
while player1_wins < wining_score and player2_wins < wining_score:

    print('----------------------------------------------------------------')
    print(f"player1 wins : {player1_wins} and player2 wins : {player2_wins}")
    print('----------------------------------------------------------------')
    Player_1 = input('player_1 make your move : ').lower()
    print(f'player_2 make your move : {computerMove}')
    Player_2 = computerMove
    if Player_1 == "q" or Player_1 == "quit":
        break
    if Player_1 == Player_2:
        print("the result is tie \n equal")
    if Player_1 == "rock":
        if Player_2 == "scissors":
            print("player_1 win the game")
            player1_wins += 1
        elif Player_2 == "paper":
            print("player_2 win the game")
            player2_wins += 1
    elif Player_1 == "paper":
        if Player_2 == "rock":
            print("player_1 win the game")
            player1_wins += 1
        elif Player_2 == "scissors":
            print("player_2 win the game")
            player2_wins += 1
    elif Player_1 == "scissors":
        if Player_2 == "paper":
            print("player_1 win the game")
            player1_wins += 1
        elif Player_2 == "rock":
            print("player_2 win the game")
            player2_wins += 1
    else:
        print("something went wrong!")



print(f"final score ===>  player1 wins : {player1_wins} and player2 wins : {player2_wins}")





#if Player_1 == 'rock' and Player_2 == 'scissors':
#    print('player_1 win the game')
#elif Player_1 == "rock" and Player_2 == "paper":
#    print("the player_2 win the game")



#elif Player_1 == "paper" and Player_2 == "rock":
#    print("player_1 win the game")
#elif Player_1 == "paper" and Player_2 == "scissors":
#    print("player_2 win the game")





#elif Player_1 == "scissors" and Player_2 == "paper":
##    print("player_1 win the game")
#elif Player_1 == "scissors" and Player_2 == "rock":
#    print("player_2 win the game")

#elif Player_1 == Player_2:
#    print("the result is tie \n equal")


#else:
#    print("something went wrong!")
