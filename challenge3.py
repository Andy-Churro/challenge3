import random 

# 1) Generate a random number between 1 and 100
number = random.randint(1, 100)

# 2) Prompt the user for their name and welcome to the game
name = input("What's your name? ")
print(f"Hi {name}, guess the number I'm thinking of (1-100). You have 8 tries!")

# 3) Allow the user eight tries to guess the number
max_attempts = 8

for attempt in range(max_attempts):
    guess = int(input("Your guess: "))

    # 4) Check if the guess is within the valid range (1-100)
    if guess < 1 or guess > 100:
        print("Out of range! Choose a number between 1 and 100.")
        continue

    # 5) Check the guess
    if guess == number:
        print("Congratulations! You guessed it!")  # Congratulate them
        break
    elif guess < number:
        print("Too low! Try again.")
    else:
        print("Too high! Try again.")

# 6) If the user fails to guess correctly after eight attempts, reveal the number
if guess != number:
    print(f"Sorry! The number was {number}.")
