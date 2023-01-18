class Game():
    winner = {
        "p" : "r",
        "r" : "s",
        "s" : "p"
    }

    def intro(arg):
        arg = print('Welcome to Rock Paper Scissors!')

    def play_game(self):
        player_1 = self.validate_input("Player 1")#firstMove)
        player_2 = self.validate_input("Player 2")

        if self.winner[player_1] == player_2:
            print("Player 1 Wins")
        elif self.winner[player_2] == player_1:
            print("Player 2 Wins")
        else:
            print("Game Tied")

    def validate_input(self, player_string):
        while(True):
            user_input = input(f'{player_string}: Enter (r) for Rock (p) for Paper or (s) for Scissors: ')
            if (user_input != "r") and (user_input != "p") and (user_input != "s"):
                print("Input invalid, please try again!")
            else:
                break
        return user_input

new_game = Game()
new_game.intro()
new_game.play_game()
