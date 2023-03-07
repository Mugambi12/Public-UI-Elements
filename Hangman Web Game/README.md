# Hangman Game

This is a simple implementation of the classic Hangman game in Python🐍. The player tries to guess a hidden word by suggesting letters or the entire word. If the player guesses a letter that is not in the word, a part of a stick figure is drawn👨‍🎨. The game ends when the player guesses the word, or the stick figure is complete, indicating the player has lost😔.

## How to play 🕹️

1. Clone or download the repository to your local machine💻.
2. Open a terminal or command prompt and navigate to the directory containing the game code.
3. Run the ***hangman.py*** file using the command:

```bash
python hangman.py
```

4. The program will prompt you to enter a word for someone to guess. The word should not be longer than 10 characters.
5. Once you enter the word, the game will start🎉.
6. The program will display a series of underscores representing the letters in the word.
7. You can guess a letter or the entire word by typing it in the terminal and pressing Enter.
8. If the letter or word is in the word, it will replace the underscore(s) in the display.
9. If the letter or word is not in the word, part of the stick figure will be drawn and the number of incorrect guesses will be increased.
10. If you guess the entire word correctly, you can continue guessing until you have filled in all the letters.
11. If you make 3 incorrect guesses, the game ends and you lose.

## Run Locally 💻

To run this game locally, run this command on your git bash:

Linux and macOS:

```bash
git clone https://github.com/mugambi12/hangman-game.git
```

Windows:

```bash
git clone https://github.com/mugambi12/hangman-game.git
```

## Code explanation 🤖

The ***hangman.py*** file contains the Python code for the game. Here is a brief explanation of the main parts of the code:

<ol>
  <li>The program prompts the user to enter a word for someone to guess. The word should not be longer than 10 characters.</li>
  <li>The game begins, and the program displays a series of underscores representing the letters in the word.</li>
  <li>The player can guess a letter or the entire word by typing it in the terminal and pressing Enter.</li>
  <li>If the letter or word is in the word, it will replace the underscore(s) in the display.</li>
  <li>If the letter or word is not in the word, part of the stick figure will be drawn and the number of incorrect guesses will be increased.</li>
  <li>If the player guesses the entire word correctly, they can continue guessing until they have filled in all the letters.</li>
  <li>If the player makes 3 incorrect guesses, the game ends and they lose.</li>
  <li>The program prints out messages indicating whether the player's guess is correct or incorrect, and the number of guesses remaining.</li>
  <li>If the player wins or loses, the program prints out a message indicating the outcome and the correct word.</li>
</ol>

That's it! Have fun playing the game! 😄

### Acknowledgments 🙏

<li><a href="https://docs.python.org/3/index.html/">Python documentation</a>.</li>
<li><a href="https://ascii.co.uk/art">ASCII art</a>.</li>

#### License 📄

  <p>This project is licensed under the <a href="https://choosealicense.com/licenses/mit/">MIT</a>.</p>
