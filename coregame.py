
def play_game():
    print("Welcome to Word Guess!")
    while True:
        guess = input("Guess a letter: ")
        print(f"You guessed: {guess}")

if __name__ == "__main__":
    play_game()

class Hangman:

    def __init__(self, word):

        self.word = word.upper()
 
        self.guessed_letters = set()
 
        self.max_attempts = 6

        self.wrong_guesses = 0

    def display_word(self):

        display = ""

        for letter in self.word:

            if letter in self.guessed_letters:

                display += letter + " "

            else:

                display += "_ "

        return display.strip()
    
    def make_guess(self, letter):
        letter = letter.upper()

        # Validation
        if len(letter) != 1 or not letter.isalpha():
            return "Please guess a single letter"

        if letter in self.guessed_letters:
            return "You already guessed that letter"

        # Track the guess
        self.guessed_letters.add(letter)

        # Check if it's correct
        if letter in self.word:
            # If all letters have been guessed, player wins
            if all(l in self.guessed_letters for l in self.word):
                return "Correct! You've guessed the word."
            return "Correct guess"
        else:
            # Wrong guess
            self.wrong_guesses += 1
            if self.wrong_guesses >= self.max_attempts:
                return f"Game over. The word was {self.word}"
            return "Incorrect guess"
    
    def quit_game(self):
        self.quit_game = True

        if self.quit_game:
            return "Thanks for playing! Goodbye!"    

