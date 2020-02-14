import random
import getpass
print("Welcome to Rock, Paper, Scissors.")
Player1N = input("Please enter your name player A: \n")
Player2N = input("Please enter your name player B: \n")
firstplayer = int(random.randint(1,2))
gamestate = 3
# if 0 = tie
# if 1 = Player 1 win
# if 2 = Player 2 win
Player1W = int(0)
Player2W = int(0)
def GetPlayerWepons(Player1Nn, Player2Nn) :
  global Player1W
  global Player2W
  if firstplayer == 1 :
    print(Player1N + " has been randomly selected to start the game.")
    Player1W = int(getpass.getpass(Player1Nn + " please choose your weapon: \n 1. Rock \n 2. Paper \n 3. Scissors \n"))
    Player2W = int(getpass.getpass(Player2Nn + " please choose your weapon: \n 1. Rock \n 2. Paper \n 3. Scissors \n"))
  else:
    print(Player2N + " has been randomly selected to start the game.")
    Player2W = int(getpass.getpass(Player2Nn + " please choose your weapon: \n 1. Rock \n 2. Paper \n 3. Scissors \n"))
    Player1W = int(getpass.getpass(Player1Nn + " please choose your weapon: \n 1. Rock \n 2. Paper \n 3. Scissors \n"))
def GetWinner(Player1wep, Player12wep):
  #0 = Tie
  #1 = Player 1 win
  #2 = Player 2 win
  #3 = Something went wrong
  #Ties
  #RR
  if Player1wep == 1 and Player12wep == 1:
    return 0
  #PP
  elif Player1wep == 2 and Player12wep == 2:
    return 0
  #SS
  elif Player1wep == 3 and Player12wep == 3:
    return 0
  #Rock
  #RP
  elif Player1wep == 1 and Player12wep == 2:
    return 2
  #PR
  elif Player1wep == 2 and Player12wep == 1: 
    return 1
  #Paper
  #SR
  elif Player1wep == 3 and Player12wep == 1:
    return 2
  #RS
  elif Player1wep == 1 and Player12wep == 3:
    return 1
  #Scissors
  #SP
  elif Player1wep == 2 and Player12wep == 3:
    return 2
  #PS
  elif Player1wep == 3 and Player12wep == 2:
    return 1
  else :
    return 3
def Fight(Player1Nn, Player2Nn):
  global gamestate
  GetPlayerWepons(Player1Nn, Player2Nn)
  gamestate = int(GetWinner(Player1W, Player2W))
  while gamestate == 0:
    GetPlayerWepons(Player1Nn, Player2Nn)
    gamestate = GetWinner(Player1W, Player2W)
  if gamestate == 1:
    print(Player1Nn + " Is the winner!")
  elif gamestate == 2:
    print(Player2Nn + " Is the winner!")
  else :
    print("Something went wrong")

Fight(Player1N,Player2N)