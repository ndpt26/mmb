import random

def guess_number():
    number = random.randint(1, 100)
    attempts = 0
    
    print("I'm thinking of a number between 1 and 100. Can you guess what it is?")
    
    while True:
        guess = int(input("Enter your guess: "))
        attempts += 1
        
        if guess < number:
            print("Too low, try again!")
        elif guess > number:
            print("Too high, try again!")
        else:
            print(f"Congratulations! You've guessed the number {number} in {attempts} attempts!")
            break

guess_number()
