# Donovan Farley-Freeman
# 9/27/24
# Creating a game of tic-tac-toe
from tictac import TicTacToe as board

PossibleCompMoves = ["t l", "t m", "t r", "m l", "m m", "m r", "b l", "b m", "b r"]
toeboard = board()

def askinp():
  userinp = input(f"It is your turn, your token is \'{toeboard.geturn()}\'. " 
  "Please enter where you would like to place your token on the board. For some examples-\n m m for middle middle(The center square), "
  "t l for top left, b r for bottom right.")
  print()
  return userinp

def DoTurn():
  FalseMove = True
  while FalseMove is True:
    userinp = askinp()
    FalseMove = toeboard.place_token(userinp)
    if FalseMove is True:
      print("That place on the board has a token on it already.\n")
  print("It is now the Computer's turn to place a token.\n")



def main():
  winner = False
  while winner is not True  :
    DoTurn()
    winner = toeboard.is_winner()
    print(toeboard)
    print(winner)


  





if __name__ == "__main__":
  main()