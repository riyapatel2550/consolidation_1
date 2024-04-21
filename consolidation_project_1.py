# Word Guessing Game (Code)

import os
import random

# Chooses a word from the word bank
def choose_word():
    word_bank = ["christmas", "thanksgiving", "halloween", "easter", "kwanzaa"]
    return random.choice(word_bank)

# Welcomes player into the game
print("Welcome to the Word Guessing Game!")

word = choose_word()
letters_guessed = []
words_guessed = []
letter_counter = 0
word_counter = 0

# The while loop that processes the entire game
while word_counter in range (3):
    guess = input("Guess a letter or guess the secret word: ")
    if len(guess) == 1:
        if guess in word:
            letters_guessed.append(guess)
            count = word.count(guess)
            if count == 1:
                print(f"The letter {guess} appears once in the word.")
            else:
                print(f"The letter {guess} appears {count} times in the word.")
                letter_counter += 1
        else:
            print(f"The letter {guess} is not in the word.")
            letters_guessed.append(guess)
            letter_counter += 1 
    elif len(guess) > 1:
        if guess == word:
                print(f"You have guessed the word! The secret word is {word}.")
                word_counter += 1
                break
        else:
            print("That is not the word.")
            words_guessed.append(guess)
            word_counter += 1
            if len(word_counter) == 3:
                print(f"You have used up all your tries for the word. The secret word was {word}.")
                break