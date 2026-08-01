import random

print("🎮 Welcome to the Number Guessing Game!")

number = random.randint(1, 100)
attempts = 0

while True:
    guess = int(input("Enter your guess (1-100): "))
    attempts += 1

    if guess < number:
        print("Too Low! Try Again.")
    elif guess > number:
        print("Too High! Try Again.")
    else:
        print("🎉 Congratulations! You guessed the correct number.")
        print("Total Attempts:", attempts)
        break
    