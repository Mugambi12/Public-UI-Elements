import random

MAX_WORD_LENGTH = 10
MAX_GUESSES = 3

# Get the word to guess
word = input(f"Enter a word for someone to guess (Max {MAX_WORD_LENGTH}): ").lower()
while len(word) > MAX_WORD_LENGTH:
    print(f"The word should not be longer than {MAX_WORD_LENGTH} characters.")
    word = input(f"Enter a word for someone to guess (Max {MAX_WORD_LENGTH}): ").lower()

# Set up the game
guessed_letters = set()
incorrect_guesses = 0
hangman_correct = "😄"
hangman_incorrect = "😔"

# Start the game
while True:
    # Print out the partially guessed word
    word_display = ""
    for letter in word:
        if letter in guessed_letters:
            word_display += letter
        else:
            word_display += "_"
    print(word_display)

    # Get the player's guess
    guess = input("Guess a letter or the entire word: ").lower()

    # Check if the guess is the entire word
    if guess == word:
        print("Congratulations, you have won!")
        break

    # Check if the guess is a single letter
    if len(guess) != 1:
        print("Please enter a single letter or the entire word.")
        continue

    # Check if the guess has already been made
    if guess in guessed_letters:
        print(f"You have already guessed {guess}.")
        continue

    # Check if the guess is correct
    if guess in word:
        guessed_letters.add(guess)
        print(f"Correct!\n\n{hangman_correct}\n")
    else:
        incorrect_guesses += 1
        print(f"Incorrect! You have {MAX_GUESSES - incorrect_guesses} guesses left.\n\n{hangman_incorrect}\n")

    # Check if the player has won
    if all(letter in guessed_letters for letter in word):
        print(f"Congratulations, you have won! {word}.")
        break

    # Check if the player has lost
    if incorrect_guesses == MAX_GUESSES:
        print(f"Sorry, you have lost. The word was {word}.")
        break
