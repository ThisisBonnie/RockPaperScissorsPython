import random
import getpass
print("Welcome to Rock, Paper, Scissors.")
Player1N = input("Please enter your name player A: \n")
Player2N = input("Please enter your name player B: \n")
RoundNumber = int(input("Please enter the ammount of rounds you want to play! \n"))
def GetPlayerWepons(Player1Nn, Player2Nn,firstplayer) :
  if firstplayer == 1 :
    print(Player1N + " has been randomly selected to start the game.")
    Player1W = int(getpass.getpass(Player1Nn + " please choose your weapon: \n 1. Rock \n 2. Paper \n 3. Scissors \n"))
    Player2W = int(getpass.getpass(Player2Nn + " please choose your weapon: \n 1. Rock \n 2. Paper \n 3. Scissors \n"))
  else:
    print(Player2N + " has been randomly selected to start the game.")
    Player2W = int(getpass.getpass(Player2Nn + " please choose your weapon: \n 1. Rock \n 2. Paper \n 3. Scissors \n"))
    Player1W = int(getpass.getpass(Player1Nn + " please choose your weapon: \n 1. Rock \n 2. Paper \n 3. Scissors \n"))
  weaponcombo = (Player1W,Player2W)
  return(weaponcombo)
def GetWinner(Player1wep, Player2wep):
  #0 = Tie
  #1 = Player 1 win
  #2 = Player 2 win
  #3 = Something went wrong
  #Ties
  #RR
  if Player1wep == 1 and Player2wep == 1:
    return 0
  #PP
  elif Player1wep == 2 and Player2wep == 2:
    return 0
  #SS
  elif Player1wep == 3 and Player2wep == 3:
    return 0
  #Rock
  #RP
  elif Player1wep == 1 and Player2wep == 2:
    return 2
  #PR
  elif Player1wep == 2 and Player2wep == 1: 
    return 1
  #Paper
  #SR
  elif Player1wep == 3 and Player2wep == 1:
    return 2
  #RS
  elif Player1wep == 1 and Player2wep == 3:
    return 1
  #Scissors
  #SP
  elif Player1wep == 2 and Player2wep == 3:
    return 2
  #PS
  elif Player1wep == 3 and Player2wep == 2:
    return 1
  else :
    return 3
def FindWeponName(weapon):
  if weapon == 1:
    return("Rock")
  elif weapon == 2:
    return("Paper")
  elif weapon == 3:
    return("Scissors")
  else:
    return("A nuclear bomb!")

def gamestart(Rounds, P1N, P2N):
  P1Score = 0
  P2Score = 0
  for i in range(Rounds):
    first = int(random.randint(1,2))
    wepons = GetPlayerWepons(P1N,P2N,first)
    winner = GetWinner(wepons[0],wepons[1])
    print("With",P1N,"using",FindWeponName(wepons[0]),"and",P2N,"Using",FindWeponName(wepons[1]),".....")
    if winner == 1:
      print(P1N,"won the battle")
      P1Score +=1
    elif winner == 2:
      print(P2N,"won the battle")
      P2Score +=1
    elif winner == 0:
      print("Game was a tie!")
    else:
      print("Screw you for entering a stupid number")
  if P1Score == P2Score:
    print("The game was a tie!")
  elif P1Score > P2Score:
    print(P1N," Won!")
  else:
    print(P2N," Won!")
gamestart(RoundNumber, Player1N, Player2N)