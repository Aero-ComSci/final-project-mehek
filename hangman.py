import random

def choose_word():
    words = ["summer", "heatwave", "beach", "popsicle", "exciting", "vacation", "sunny"]
    return random.choice(words)
    
class Hangman:
    def __init__(self):
        self.words = ["summer", "heatwave", "beach", "popsicle", "exciting", "vacation", "sunny"]
        self.word_to_guess = random.choice(words))
        self.word_letters = set(self.word_to_guess)
        self.alphabet = set(chr(i) for i in range(ord('a'), ord('z') + 1))
        self.used_letters = set()
        self.lives = 6

def display_word(word, guessed_letters):
    displayed_word = ""
    for letter in word:
        if letter in guessed_letters:
            displayed_word += letter + " "
        else:
            displayed_word += "_ "
    return displayed_word.strip()
def hangman():
    word_to_guess = choose_word()
    word_letters = set(word_to_guess)
    alphabet = set(chr(i) for i in range(ord('a'), ord('z') + 1))
    used_letters = set()
    lives = 6

    print("Schools out, summer is here, if your ever bored and have nothing to do, play a quick game of hangman!")

    while len(word_letters) > 0 and lives > 0:
        print"You have", lives, "lives left."
        print"Used letters:", " ".join(used_letters)
        current_display = display_word(word_to_guess, used_letters)
        print"Current word:", current_display

        guess = input("Guess a letter: ").lower()
        if len(guess) == 1 and guess.isalpha():
            if guess in used_letters:
                print"This letter has alreayd been guessed, try again!!"
            elif guess not in alphabet:
                print"Invalid input, please enter a letter!"
            elif guess in word_letters:
                used_letters.add(guess)
                word_letters.discard(guess)
            else:
                used_letters.add(guess)
                lives -= 1
                print"This letter is not in the word."
        else:
            print("Invalid input, please enter a letter!")

    if lives == 0:
        print"OOF...YOUR DEAD! The word was", word_to_guess
    else:
        print"CONGRATSSS! You guessed the word ", word_to_guess, "!"

hangman()
