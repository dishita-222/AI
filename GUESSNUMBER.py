import random

# Generate a random number between 1 and 100 so that the number is limited and loop doesn't go to infinite

secret_number = random.randint(1, 100)

# Initialize the number of guesses to 0
num_guesses = 0

# Loop until the player guesses the number
while True:
    # Get the player's guess from them 
    guess = int(input("Guess the number between 1 and 100: "))
    
    # Increment the number of guesses
    num_guesses += 1
    
    # Check if the player guessed the correct number
    if guess == secret_number:
        print("Congratulations! You guessed the number in", num_guesses, "guesses.")
        break
    
    # Give the player a hint if their guess was too high or too low
    if guess < secret_number:
        print("Too low. Guess again.")
    else:
        print("Too high. Guess again.")
