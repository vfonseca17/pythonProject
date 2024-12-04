import random

def get_word_list():
    return ["python", "programming", "coding"]

def choose_random_word(word_list):
    return random.choice(word_list)

def display_word_progress(word, guessed_letters):
    return " ".join([letter if letter in guessed_letters else "_" for letter in word])

def is_valid_guess(guess, guessed_letters):
    if len(guess) != 1 or not guess.isalpha():
        return "Please enter a single letter."
    if guess in guessed_letters:
        return "You have already guessed that letter."
    return None

def hangman():
    print("Welcome to Hangman!")
    word_list = get_word_list()
    secret_word = choose_random_word(word_list)
    guessed_letters = set()
    attempts_remaining = 6

    print(f"The word has {len(secret_word)} letters.")
    print("_ " * len(secret_word))

    while attempts_remaining > 0:
        print(f"\nAttempts remaining: {attempts_remaining}")
        print(f"Guessed letters: {', '.join(sorted(guessed_letters))}")
        print(f"Word progress: {display_word_progress(secret_word, guessed_letters)}")

        guess = input("Guess a letter: ").lower()
        validation_error = is_valid_guess(guess, guessed_letters)
        if validation_error:
            print(validation_error)
            continue

        guessed_letters.add(guess)

        if guess in secret_word:
            print(f"Good guess! '{guess}' is in the word.")
            if all(letter in guessed_letters for letter in secret_word):
                print(f"\nCongratulations! You guessed the word: {secret_word}")
                break
        else:
            print(f"Oops! '{guess}' is not in the word.")
            attempts_remaining -= 1

    if attempts_remaining == 0:
        print(f"\nGame over! The word was: {secret_word}")

if __name__ == "__main__":
    hangman()
