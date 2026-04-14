def is_won(self):

    """Check if all letters have been guessed"""

    return all(letter in self.guessed_letters for letter in self.word)



def is_lost(self):

    """Check if player is out of attempts"""

    return self.wrong_guesses >= self.max_attempts



def is_game_over(self):

    """Check if game should end"""

    return self.is_won() or self.is_lost()

def get_game_status(self):

    """Return a formatted status string"""

    status = f"Word: {self.display_word()}\n"

    status += f"Guessed: {', '.join(sorted(self.guessed_letters))}\n"

    status += f"Attempts remaining: {self.max_attempts - self.wrong_guesses}"

    return status
