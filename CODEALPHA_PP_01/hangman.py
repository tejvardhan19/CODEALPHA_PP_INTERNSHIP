import random


def choose_word():
    words = ['python', 'hangman', 'programming', 'challenge', 'code']
    return random.choice(words)


def display_word(word, guessed_letters):
    return ' '.join([letter if letter in guessed_letters else '_' for letter in word])


def hangman():
    word = choose_word()
    guessed_letters = set()
    incorrect_guesses = 0
    max_incorrect_guesses = 6

    print("Welcome to Hangman!")

    while incorrect_guesses < max_incorrect_guesses:
        print("\nWord to guess: " + display_word(word, guessed_letters))
        print("Guessed letters: " + ' '.join(guessed_letters))
        print(f"Incorrect guesses left: {max_incorrect_guesses - incorrect_guesses}")

        guess = input("Guess a letter: ").lower()

        if guess in guessed_letters:
            print("You already guessed that letter.")
        elif guess in word:
            guessed_letters.add(guess)
            if set(word) == guessed_letters:
                print(f"Congratulations! You've guessed the word: {word}")
                break
        else:
            guessed_letters.add(guess)
            incorrect_guesses += 1
            print(f"Incorrect guess! {max_incorrect_guesses - incorrect_guesses} incorrect guesses left.")

    if incorrect_guesses == max_incorrect_guesses:
        print(f"Sorry, you've run out of guesses. The word was: {word}")


if __name__ == "__main__":
    hangman()
