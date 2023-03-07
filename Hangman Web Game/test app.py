word = input("Enter a word for someone to guess: ")
word = word.lower()

guessed_letters = []
incorrect_guesses = 0

hangman = [
    """
    +---+
    |   |
        |
        |
        |
        |
    =========
    """,
    """
    +---+
    |   |
    O   |
        |
        |
        |
    =========
    """,
    """
    +---+
    |   |
    O   |
    |   |
        |
        |
    =========
    """,
    """
    +---+
    |   |
    O   |
   /|   |
        |
        |
    =========
    """,
    """
    +---+
    |   |
    O   |
   /|\  |
        |
        |
    =========
    """,
    """
    +---+
    |   |
    O   |
   /|\  |
   /    |
        |
    =========
    """,
    """
    +---+
    |   |
    O   |
   /|\  |
   / \  |
        |
    =========
    """
]

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
    guess = input("Guess a letter: ")
    guess = guess.lower()

    # Check if the guess is correct
    if guess in word:
        guessed_letters.append(guess)
        print("Correct!")
    else:
        incorrect_guesses += 1
        print("Incorrect!")
        print(hangman[incorrect_guesses])

    # Check if the player has won
    if all(letter in guessed_letters for letter in word):
        print("Congratulations, you have won!")
        break

    # Check if the player has lost
    if incorrect_guesses == len(hangman) - 1:
        print("Sorry, you have lost. The word was", word)
        break
