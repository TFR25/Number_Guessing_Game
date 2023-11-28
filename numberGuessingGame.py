import random
from art import logo

print(logo)

EASY_LEVEL = 10
HARD_LEVEL = 5

print("Welcome to the number guessing game! \nI'm thinking of a number between 1 and 100.")

def guess_a_num():
    num = random.randint(0, 100)
    lives = tries
    guess = int(input("Choose a number between 0 and 100: "))
    while guess != num:
        lives -= 1
        if guess > num:
            print("Too high.")
        elif guess < num:
            print("Too low.")
        print(f"You have {lives} lives left.")
        if lives > 0:
            guess = int(input((f"Guess another number: ")))
        elif guess == num:
            print("Well done. You guessed correctly.")
        else:
            print(f"Sorry, you lose.\nThe answer was {num}")
            return
   
def start():
    level = input("Choose a level. Type 'easy' or 'hard': ")
    if level == "easy":
        return EASY_LEVEL
    else:
        return HARD_LEVEL
    
tries = start()
guess_a_num()
