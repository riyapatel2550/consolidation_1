# Word Guessing Game Consolidation Project
Riya Patel

The Rules of Word Guessing Game and how it works:

1. The player is prompted a welcome message at the beginning of the game, a message correlating to the theme of the words (holidays), and the number of letters in the randomly selected word.
2. The player is allowed to guess a letter or a word in every round.
3. The player can guess as many letters as it would like, but only has three word guesses before the game quits.
4. After every round, the game will tell the player how many times the letter appears in the word.
5. When the player guesses the word, it will tell them they are correct, end the game, and provide scores.
6. The game will output the number of letters guessed, number of words guessed, and the final score (# of letters guessed).

How to run the code (technological aspect):
1. You must begin to run your code and the first few print messages will appear.
2. The last print message is an input message where you enter a letter or a word.
3. This letter or word is taken into account and added to a letter or word counter.
4. If the input was a letter, it will send an output print message stating whether or not the letter appears in the secret word. If it is, it will state how many times the letter appears. It will also add 1 to an invisible letter counter.
5. If the input was a word, it will send an output print message stating whether the word was correct or not. It will also add 1 to an invisible word counter.
6. The user will be asked this input message again until the user finally gets the word.
7. The user will only be able to input three word guesses into the program. It will exit the while loop after reaching a max of 3 guesses. This is done through updating the word counter variable.
8. At the end of the game, whether the word was guessed or not, there will be an output message for how the letter guesses, word guesses, and final score.
9. The letter guesses and the final score are determined by the letter counter in the while loop and within the if-else statements.
10. The word guesses are determined by the word counter in the while loop and within the if-else statements.
11. This code involves a single while loop that runs until the range reaches 3 and the game must break.


Important Key Notes:
- import os and import random are used in the beginning in order for it to be an interactive operating system and for the word from the word bank to be random.
- letters_guessed and words_guessed were put in a list and used the append() method for adding the of letters and words guessed into a list.
- the variables letter_counter and word_counter were assigned as int and set to 0 to allow the counters evaulate how many rounds the game goes for.
- len(guess) == 1 is used to determine whether the guess was a letter or a word.
- The format method in the print statements are useful to easily implement certain values from variables into outputs and messages.

Future Goals:
- Add a list of letters used to remind the player
- The word bank will change the words over time