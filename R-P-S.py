# we wana to build a game
import random

print("rock......")
print("paper......")
print("scissors......")


randomNumber = random.randint(0, 2)

if randomNumber == 0:
    computerMove = "rock"
elif randomNumber == 1:
    computerMove = "paper"
elif randomNumber == 3:
    computerMove = "scissors"

Player_1 = input('player_1 make your move : ').lower()
print(f'player_2 make your move : {computerMove}')
Player_2 = computerMove
computerMove = Player_2
if Player_1 == Player_2:
    print("the result is tie \n equal")
if Player_1 == "rock":
    if Player_2 == "scissors":
        print("player_1 win the game")
    elif Player_2 == "paper":
        print("player_2 win the game")


elif Player_1 == "paper":
    if Player_2 == "rock":
        print("player_1 win the game")
    elif Player_2 == "scissors":
        print("player_2 win the game")


elif Player_1 == "scissors":
    if Player_2 == "paper":
        print("player_1 win the game")
    elif Player_2 == "rock":
        print("player_2 win the game")


else:
    print("something went wrong!")



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
