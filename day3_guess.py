import random

# Pick a random number between 1 and 10
secret = random.randint(1, 10)

# Start the game
print("I'm thinking of a number between 1 and 10...")

while True:
    guess = int(input("Take a guess: "))

    if guess == secret:
        print("Correct! 🎉")
        break  # exit the loop
    elif guess < secret:
        print("Too low, try again.")
    else:
        print("Too high, try again.")
