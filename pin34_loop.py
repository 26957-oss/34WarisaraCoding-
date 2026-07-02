import random

secret_number = random.randint(1, 100)
count = 0  

print("=== Welcome to the Number Guessing Game (1-100) ===")

while True:
    guess = int(input("Enter your guess: "))  
    count = count + 1 

    if guess < secret_number:
        print("Too low! Try again.")
    elif guess > secret_number:
        print("Too high! Try again.")
    else:
        print("Congratulations! You guessed it right.")
        print("Total number of guesses:", count)
        break 