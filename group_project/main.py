## Author: Mustafa Radheyyan, Dwane Richards, David James
## Date: 01/12/2023
## Assignment: Cognixia JUMPro Python Project 1

from stats import (getAllStats)
from number_guess_game.main import main as ngg
from rock_paper_scissors.main import main as rps
from tic_tac_toe.main import main as ttt

if __name__ == "__main__":
    while(True):
        user_input = input("""What game do you want to play?
('ngg' for Number Guess Game, 'rps' for Rock Paper Scissors, 'ttt' for Tic Tac Toe) """)

        if user_input == 'ngg':
            ngg()
        elif user_input == 'rps':
            rps()
        elif user_input == 'ttt':
            ttt()
        elif user_input == 'v':
            print('\n',getAllStats().to_string(index=False))
        elif user_input == 'q':
            break
        print("\nKeep playing or press 'v' to view stats and 'q' to quit!\n")
