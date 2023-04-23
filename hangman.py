import random


class HangmanEngine:
    """A class that implements the logic of the hangman game."""

    words = ["hello"]

    def __init__(self):
        self.secret_word = random.choice(self.words)
        self.guessed_letters = []
        self.display = ["*" for _ in range(len(self.secret_word))]
        self.remaining_guesses = 6

    def guess(self, letter):
        if letter in self.guessed_letters:
            return False

        self.guessed_letters.append(letter)
        if letter not in self.secret_word:
            self.remaining_guesses -= 1
            if self.remaining_guesses == 0:
                return False
        else:
            for i, c in enumerate(self.secret_word):
                if c == letter:
                    self.display[i] = letter

        return True

    def get_display(self):
        return "".join(self.display)

    def run(self):
        """Runs the game loop."""
        print("Welcome to Hangman!")
        while True:
            print(f"Word: {self.get_display()}")
            print(f"Guesses left: {self.remaining_guesses}")
            guess = input("Guess a letter: ").lower()

            if len(guess) != 1 or not guess.isalpha():
                print("Please enter a single letter.")
                continue

            if not self.guess(guess):
                print("Incorrect!")
            else:
                print("Correct!")

            if "*" not in self.display:
                print("You win!")
                break

        print(f"The word was {self.secret_word}.")

if __name__ == "__main__":
    engine = HangmanEngine()
    engine.run()