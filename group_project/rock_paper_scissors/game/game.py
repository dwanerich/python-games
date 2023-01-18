import stats

class Game():
    winner = {
        "p" : "r",
        "r" : "s",
        "s" : "p"
        }

    def intro(self):
        print('Welcome to Rock Paper Scissors!')

    def play_game(self):
        player1_name = input("Player 1, what is your name? ")
        
        while(True):
            player2_name = input("Player 2, what is your name? ")    
            if player2_name == player1_name:
                print(f"Sorry player 2, you have to choose a name different from player 1, ('{player1_name}')!")
            else: break
        
        #firstMove
        player_1 = self.validate_input(player1_name)
        player_2 = self.validate_input(player2_name)

        if self.winner[player_1] == player_2:
            print(f"{player1_name} Wins")
            stats.sendStats(-1, 1, 1)
            
        elif self.winner[player_2] == player_1:
            print(f"{player2_name} Wins")
            stats.sendStats(-1, 1, 1)
        else:
            print("Game Tied")
            stats.sendStats(-1, 1, 0)

    def validate_input(self, player_string):
        while(True):
            user_input = input(f'{player_string}: Enter (r) for Rock (p) for Paper or (s) for Scissors: ')
            if (user_input != "r") and (user_input != "p") and (user_input != "s"):
                print("Input invalid, please try again!")
            else:
                break
        return user_input