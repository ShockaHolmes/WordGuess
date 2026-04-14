import random

def get_word():
    words = ["python", "dragon", "castle", "wizard", "adventure", "advice", "computer", "programming", "challenge", "mystery"]
    return random.choice(words)

def display_word(secret_word, guessed_letters):
    display = ""
    for letter in secret_word:
        if letter in guessed_letters:
            display += letter + " "
        else:
            display += "_ "
    return display.strip()

def get_guess(guessed_letters):
    while True:
        guess = input("Guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Enter ONE letter only.")
        elif guess in guessed_letters:
            print("Already guessed.")
        else:
            return guess

def check_win(secret_word, guessed_letters):
    for letter in secret_word:
        if letter not in guessed_letters:
            return False
    return True

def update_game(secret_word, guess, wrong_guesses):
    if guess in secret_word:
        print("Correct!")
    else:
        print("Wrong!")
        wrong_guesses += 1
    return wrong_guesses

def play_game():
    secret_word = get_word()
    guessed_letters = []
    wrong_guesses = 0
    max_guesses = 5

    print("Welcome to Word Guess!")

    while wrong_guesses < max_guesses:
        print("\nWord:", display_word(secret_word, guessed_letters))
        print("Guesses left:", max_guesses - wrong_guesses)

        guess = get_guess(guessed_letters)
        guessed_letters.append(guess)

        wrong_guesses = update_game(secret_word, guess, wrong_guesses)

        if check_win(secret_word, guessed_letters):
            print("\nYou WIN! Word was:", secret_word)
            return

    print("\nYou LOST! Word was:", secret_word)

if __name__ == "__main__":
    play_game()

    question = input("Play again? (y/n): ").lower()
    if question == 'y':
        play_game()     

        