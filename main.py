# Donovan Farley-Freeman
# 9/27/24
# Creating a game of tic-tac-toe
from tictac import TicTacToe as board
# Had to import random twice because it kept trying to call randint as an attribute
from random import randint
from random import choice
from time import sleep

toeboard = board()

def askinp():
  userinp = input(f"It is your turn, your token is \'{toeboard.geturn()}\'. " 
  "Please enter where you would like to place your token on the board. For some examples-\n m m for middle middle(The center square), "
  "t l for top left, b r for bottom right.\t")
  print()
  return userinp

def DoTurn():
  FalseMove = True
  while FalseMove is True:
    try:
      userinp = askinp()
      FalseMove = toeboard.place_token(userinp)
      if FalseMove is True:
        print("That place on the board has a token on it already.\n")
    except:
      print("That is not a valid spot, please pick a valid spot.\n")
      FalseMove = True
  print("It is now the Computer's turn to place a token.\n")

def DoCompTurn():
  PossibleCompMoves = ["t l", "t m", "t r", "m l", "m m", "m r", "b l", "b m", "b r"]
  FalseMove = True
  while FalseMove is True:
    CompMove = choice(PossibleCompMoves)
    FalseMove = toeboard.place_token(CompMove)
  print("The Computer has placed its token, it's now your turn.\n")



def main():
  winner = False
  turn = randint(1,2)
  while winner is not True:
    turn += 1
    sleep(1.5)
    if turn % 2 == 1:
      DoTurn()
    else:
      DoCompTurn()
    winner = toeboard.is_winner()
    print(toeboard)
    print()
  print("The game has ended, someone has won...\n")
  sleep(2)
  if turn % 2 == 1:
    print("You have won congratulations!!!")
  else:
    print("The Computer has won better luck next time...")


  

if __name__ == "__main__":
  main()