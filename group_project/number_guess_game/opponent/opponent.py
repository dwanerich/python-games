import random

class Opponent:
    gave_strong_hint = False
    
    def random_number(self, min_range, max_range) -> int:
        random_number = random.randint(min_range, max_range)
        return random_number
    
    def __init__(self, min_range, max_range):
        self.__number = self.random_number(min_range, max_range)
        
    @property
    def number(self):
        return self.__number
    
    def check_nearness_of_guess(self, previous_guess, current_guess):
        if isinstance(previous_guess, int): # first round check
            difference_between_previous_guess = abs(previous_guess - self.__number)
            difference_between_current_guess = abs(current_guess - self.__number)    
            
            if current_guess == previous_guess:
                print("You guessed the same number twice!")
            elif difference_between_current_guess < difference_between_previous_guess:
                print("Hotter!")
            elif difference_between_current_guess > difference_between_previous_guess:
                print("Colder!")
            else: # difference_between_current_guess == difference_between_previous_guess
                print("Lukewarm!")
            return True
        else: return False
        
    def give_hints(self, number_of_guesses, previous_guess, current_guess) -> None:
        number = self.__number
        if (number_of_guesses < 5):
            if not self.gave_strong_hint:
                if len(str(abs(number))) > 2:
                    print(f"It begins in a {str(abs(number))[0]} and ends in a {str(number)[-1:]}")
                if len(str(abs(number))) == 2:
                    print(f"It ends in a {str(abs(number))[-1:]}")
                elif len(str(abs(number))) == 1:
                    print("It's a very short one!")
                self.gave_strong_hint = True
            else:
                return self.check_nearness_of_guess(previous_guess, current_guess)
        else:
            return self.check_nearness_of_guess(previous_guess, current_guess)