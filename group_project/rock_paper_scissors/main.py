## Author: Dwane Richards
## Date: 01/12/2023
## Assignment: Cognixia JUMPro Python Project 1

from rock_paper_scissors.game.game import Game

def main():
    new_game = Game()
    new_game.intro()
    new_game.play_game()

if __name__ == "__main__":
    main()