winner = {
  "p" : "r",
  "r" : "s",
  "s" : "p"
}

class Game():
  # def __init__(self, p1, p2, winner):
  #   self.winner = winner
  #   self.p1 = p1
  #   self.p2 = p2

  def intro(arg):
    arg = print('Welcome to Rock Paper Scissors!')

  def player_moves(self, firstMove, secondMove):

    firstMove = input(print('Player 1: Enter (r) for Rock (p) for Paper or (s) for Scissors: '))
    # result1 = self.validate_input(firstMove)


    secondMove = input(print('Player 2: Enter (r) for Rock (p) for Paper or (s) for Scissors: '))
    # result2 = self.validate_input(secondMove)


    if (firstMove == secondMove):
      print("Game Tied")
    elif (winner[firstMove] == [secondMove]):
      print("Player 1 Wins")
    else: print("Player 2 Wins")

  def validate_input():
    input = input('Player 1: Enter (r) for Rock (p) for Paper or (s) for Scissors: ')
    if (input != "r") or (input != "p") or (input != "s"):
      return "Input invalid, please re-enter: "

      # input = print(("Input invalid, please re-enter: "))
    else: input = True


new_game = Game()
new_game.intro()
new_game.player_moves("r", "p")
