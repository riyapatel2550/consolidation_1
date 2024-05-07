# Word Guessing Game (Code)

import os
import random

# Chooses a word from the word bank
def choose_word():
    word_bank = ["christmas", "thanksgiving", "halloween", "easter", "kwanzaa"]
    return random.choice(word_bank)

# Welcomes player into the game
word = choose_word()
print("Welcome to the Word Guessing Game!")
print("The theme of the words is Holidays!")
print(f"The word has {len(word)} letters.")
# Variables needed for counters and guesses
letters_guessed = []
words_guessed = []
letter_counter = 0
word_counter = 0

# The while loop that processes the entire game with its conditionals and counters
while word_counter in range (3):
    guess = input("Guess a letter or guess the secret word: ")
    if len(guess) == 1:
        if guess in word:
            letters_guessed.append(guess)
            count = word.count(guess)
            if count == 1:
                print(f"The letter {guess} appears once in the word.")
                letter_counter += 1
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
            if len(words_guessed) == 3:
                print(f"You have used up all your tries for the word. The secret word was {word}.")
                break

# The results, which incude letters guessed, words guessed, and the final score.
print(f"This is the number of letters you guessed: {letter_counter}")
print(f"This is the number of words you guessed: {word_counter}")
print(f"Your final score is {letter_counter}.")
print ("hello world")