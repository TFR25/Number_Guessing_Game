import random
from art import logo
print(logo)

print("Welcome to the number guessing game! \nI'm thinking of a number between 1 and 100.")

def guess_a_num():
    num = random.randint(0, 100)
    print(num)
    guess = input("Choose a number between 0 and 100: ")
    while guess != num:
        guess = int(input((f"Your guess is: {guess} and is incorrect. Guess another number: ")))
        if guess == num:
            print("Well done. You guessed correctly.")
    
def start():
    level = input("Choose a level. Type 'easy' or 'hard': ")
    if level == "easy":
        print("You have 5 guesses.")
    else:
        print("You have 10 guesses.")
    guess_a_num()
start()