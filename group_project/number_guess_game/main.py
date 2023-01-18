## Author: Mustafa Radheyyan
## Date: 01/12/2023
## Assignment: Cognixia JUMPro Python Project 1

from number_guess_game.game_engine.game_engine import GameEngine

def main():
    number_guessing_game = GameEngine(0, 500, 10)
    number_guessing_game.play_game()

if __name__ == "__main__":
    main()