import os
import json
import stats
import datetime
from pathlib import Path
from number_guess_game.opponent.opponent import Opponent
from number_guess_game.input_handling.input_handling import input_handling

class GameEngine:
    previous_guess = None
    current_guess = None
    emp_file = Path("number_guess_game/game_results.json")
    
    def __init__(self, number_range_min = 0, number_range_max = 50, number_of_guesses = 10):
        self.winner = None
        self._number_range_min = number_range_min
        self._number_range_max = number_range_max
        self.number_of_guesses = number_of_guesses
        self.computer = Opponent(number_range_min, number_range_max)
    
    def write_to_empty_json(self, guesses_remaining):
        try:
            with open(self.emp_file, "a") as file:
                results_dictionary = {"game_results": [{'date': datetime.datetime.now().strftime("%d/%m/%Y, %H:%M:%S"),
                        'number_range': f"{self._number_range_min}-{self._number_range_max}",
                        'total guesses': self.number_of_guesses,
                        'guesses remaining': guesses_remaining,
                        'winner': self.winner,
                        'number': self.computer.number
                        }]}
                json.dump(results_dictionary, file)
        except: print("Error opening file")
    
    def append_to_json(self, guesses_remaining):
        try:
            with open(self.emp_file, "r+") as file:
                results_dictionary = {'date': datetime.datetime.now().strftime("%d/%m/%Y, %H:%M:%S"),
                                    'number_range': f"{self._number_range_min}-{self._number_range_max}",
                                    'total guesses': self.number_of_guesses,
                                    'guesses remaining': guesses_remaining,
                                    'winner': self.winner,
                                    'number': self.computer.number
                                    }
                    
                game_data = json.load(file)
                game_data["game_results"].append(results_dictionary)
                file.seek(0)
                json.dump(game_data, file)
        except: print("Error opening file")
    
    def write_to_log_file(self, guesses_remaining):
        if self.emp_file.is_file() and os.stat(self.emp_file).st_size != 0:
            self.append_to_json(guesses_remaining)
        else:
            self.write_to_empty_json(guesses_remaining)
    
    def announce_winner(self):
        print(f"The winner is {self.winner} and the number was {self.computer.number}!")

    def ask_player_for_number(self):
        return input_handling(int, f"Guess a number between {self._number_range_min} and {self._number_range_max}: ", [self._number_range_min, self._number_range_max])        
    
    def game_round(self, guesses_remaining):
        print(f"{guesses_remaining} guess{'es'[:2*(guesses_remaining)^2]} left!")
        
        self.previous_guess = self.current_guess
        self.current_guess = self.ask_player_for_number()
        
        if self.current_guess == self.computer.number:
            self.winner = "Player"
            stats.sendStats(0, 1, 1)
        elif guesses_remaining > 1:
            if self.computer.give_hints(guesses_remaining, self.previous_guess, self.current_guess) is False:
                print("Wrong!")
        else:
            print("Wrong!")
            
    def play_game(self):
        for i in range(self.number_of_guesses, 0, -1):
            self.game_round(i)
            if self.winner: break # player wins
        else: 
            self.winner = "Computer"
            stats.sendStats(0, 1, 0)
        self.announce_winner()
        self.write_to_log_file(i - 1)
        