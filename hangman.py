import random

def choose_word():
    words = ['python', 'hangman', 'programming', 'openai', 'chatgpt', 'developer', 'algorithm', 'debugging']
    return random.choice(words)

def display_hangman(tries):
    stages = [
        """
           -----
           |   |
           O   |
          /|\\  |
          / \\  |
               |
        --------
        """,
        """
           -----
           |   |
           O   |
          /|\\  |
          /    |
               |
        --------
        """,
        """
           -----
           |   |
           O   |
          /|\\  |
               |
               |
        --------
        """,
        """
           -----
           |   |
           O   |
          /|   |
               |
               |
        --------
        """,
        """
           -----
           |   |
           O   |
           |   |
               |
               |
        --------
        """,
        """
           -----
           |   |
           O   |
               |
               |
               |
        --------
        """,
        """
           -----
           |   |
               |
               |
               |
               |
        --------
        """
    ]
    return stages[tries]

def play_game():
    word = choose_word().lower()
    word_letters = set(word)
    guessed_letters = set()
    tries = 6

    print("Let's play Hangman!")
    print(display_hangman(tries))
    print(f"The word has {len(word)} letters.")
    print("_ " * len(word))

    while tries > 0 and word_letters:
        guess = input("Guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input. Please enter a single letter.")
            continue

        if guess in guessed_letters:
            print(f"You've already guessed '{guess}'. Try a different letter.")
            continue

        guessed_letters.add(guess)

        if guess in word_letters:
            word_letters.remove(guess)
            print(f"Good guess! The word contains '{guess}'.")
        else:
            tries -= 1
            print(f"Wrong guess! The word does not contain '{guess}'. You have {tries} tries left.")

        # Display the current word with guessed letters
        current_word = [letter if letter in guessed_letters else '_' for letter in word]
        print("Current word: " + " ".join(current_word))
        print(display_hangman(tries))

    if not word_letters:
        print(f"Congratulations! You've guessed the word: '{word}'!")
    else:
        print(f"Game Over! The word was: '{word}'.")

if __name__ == "__main__":
    play_game()
