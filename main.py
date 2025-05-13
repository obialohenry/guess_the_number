from art import logo
import random

EASY_LEVEL = 10
HARD_LEVEL = 5

number_list = []
for number in range(1,101):
    number_list.append(number)

actual_number = random.choice(number_list)

def attempt_word_form(level:int) -> str:
    """This method checks to see if a player have 1 attempt left,
       and returns the word 'attempt' in singular form,else it returns
       it in plural form.
    """
    if level == 1:
        return 'attempt'
    else:
        return "attempts"

def feedback(guessed_number:int, level:int)->bool:
    """This method gives feedback to the user based on a user inputted guessed number,
       and if a user have run out of attempts. It returns a boolean value which is used
       to continue or end the game.
    """
    if guessed_number == actual_number:
        print(f"You got it! The answer was {actual_number}. Guess again.")
        return False
    else:
        if level == 0:
            print("You've run out of guesses, you lose.")
            return False
        elif guessed_number > actual_number:
            print(f"Too high.\nGuess again")
            return True
        elif guessed_number < actual_number:
            print(f"Too Low.\nGuess again")
            return True

def easy_or_hard_level(level:int):
       """
       This method takes in an int datatype level, which stores the number of attempts
       according to the difficulty level a user picked, and it runs a loop according to
       the number of attempts, letting a user make a guess in attempt to get the actual
       number.It ends the loop based on the feedback it gets from the "feedback" method.
       """
       guess_again = True
       while guess_again:
        print(f"You have {level} {attempt_word_form(level)} remaining to guess the number.")
        guessed_number = int(input("Make a guess: "))
        level -= 1
        guess_again=feedback(guessed_number=guessed_number, level=level)



def guess_the_number():
    """
    This is the number guessing game.
    """
    print(logo)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    difficulty_type = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
    if difficulty_type == "hard":
        easy_or_hard_level(HARD_LEVEL)
    else:
        easy_or_hard_level(EASY_LEVEL)

guess_the_number()



