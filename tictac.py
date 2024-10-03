from random import choice

class TicTacToe:

  def __init__(self):
    self.__board = [[None, None, None] for i in range(3)]
    self.__turn = choice(["o", "x"])

  def __str__(self):
    ReturnedString = ""
    for row in self.__board:
      ReturnedString += "["
      for place in row:
        if place is not None:
          ReturnedString += f" {place},"
        else:
          ReturnedString += "  ,"
      ReturnedString += "]\n"
    return ReturnedString


  def __check_win(self):
    # Checking horizontal lines for win
    for Hl in self.__board:
      try:
        horiz_line = Hl[0] + Hl[1] + Hl[2]
      except:
        continue
      if (horiz_line == "xxx") or (horiz_line == "ooo"):
        return True
    # Checking vertical lines for win
    for Vl in range(3):
      try:
        vert_line = self.__board[0][Vl] + self.__board[1][Vl] + self.__board[2][Vl]
      except:
        continue
      if (vert_line == "xxx") or (vert_line == "ooo"):
        return True
    # Checking diagonal lines for win
    diag_line = "placholder"
    try:
      diag_line = self.__board[0][0] + self.__board[1][1] + self.__board [2][2]
    except:
      pass
    if (diag_line == "xxx") or (diag_line == "ooo"):
      return True
    try:
      diag_line = self.__board[0][2] + self.__board[1][1] + self.__board [2][0]
    except:
      pass
    if (diag_line == "xxx") or (diag_line == "ooo"):
      return True
    
    return False
      

  def place_token(self, userinp):
    placement = userinp.split()
    y, x = self.__convert(placement)
    if self.__board[y][x] is not None:
      return True
    else:
      self.__board[y][x] = self.__turn

  def is_winner(self):
    winner = self.__check_win()
    if winner is False:
      if self.__turn == "o":
        self.__turn = "x"
      else:
        self.__turn = "o"
    else:
      return True

  def geturn(self):
    return self.__turn

  def __convert(self, placement):
    if placement[0] == 't':
      y = 0
    elif placement[0] == 'm':
      y = 1
    elif placement[0] == 'b':
      y = 2
    else:
      y = iho

    if placement[1] == 'l':
      x = 0
    elif placement[1] == 'm':
      x = 1
    elif placement[1] == 'r':
      x = 2
    else:
      x = iho

    return y, x