import random
from art import logo
print(logo)

EASY_LEVEL = 5
HARD_LEVEL = 10
print("Welcome to the number guessing game! \nI'm thinking of a number between 1 and 100.")

def guess_a_num():
    num = random.randint(0, 100)
    print(num)
    lives = tries
    print(lives)
    guess = input("Choose a number between 0 and 100: ")
    while guess != num:
        lives -= 1
        if lives > 0:
            guess = int(input((f"Your guess is {guess} and is incorrect. Guess another number: ")))
        elif guess == num:
            print("Well done. You guessed correctly.")
        else:
            print("Sorry, you lose.")
            return
    
def start():
    level = input("Choose a level. Type 'easy' or 'hard': ")
    if level == "easy":
        return EASY_LEVEL
    else:
        return HARD_LEVEL
    
tries = start()
guess_a_num()
