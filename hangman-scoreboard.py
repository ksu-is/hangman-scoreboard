import random
import sys

hangman = ['''
  
     +---+
     |   |
         |
         |
         |
         |
 =========''', '''
 
    +---+
    |   |
    O   |
        |
        |
        |
=========''', '''
 
    +---+
    |   |
    O   |
    |   |
        |
        |
  =========''', '''
 
    +---+
    |   |
    O   |
   /|   |
        |
        |
  =========''', '''
 
    +---+
    |   |
    O   |
   /|\  |
        |
        |
  =========''', '''
 
    +---+
    |   |
    O   |
   /|\  |
   /    |
        |
  =========''', '''
 
    +---+
    |   |
    O   |
   /|\  |
   / \  |
        |
  =========''']

answerlist = [
"honda", "toyota", "ford", "chevrolet", "jeep", "lexus", "audi", "bmw", "nissan", "jaguar", "dodge", "volvo", "cadillac", "kia", "hyundai", "chrysler", "mercedes", "tesla", "porsche", "lincoln", "mazda"
           ]

guess_word = []
word = random.choice(answerlist) 
length_word = len(word)
letter = "abcdefghijklmnopqrstuvwxyz"
letter_Guessed = []

player_name = input("Enter your name: ").title()
player_score = 0


def beginning():
    print("Hello",player_name.title(),"\n")

beginning()

def newFunc():
    print("Ready or not...here we go!\n")

newFunc()

def change():

    for letter in word: 
        guess_word.append("-")

    print("NOTE: The word contains", length_word, "letters. You may only guess 1 letter at a time.\n")

    print(guess_word) 

def guessing():
    
    guess_taken = 1
    guess_taken = 0

    while guess_taken < 6:

        guess = input("Guess a letter from A-Z:\n").lower()

        if not guess in letter: 
            print("Your guess is invalid, it must be a letter from A-Z. TRY AGAIN!")
        elif guess in letter_Guessed: 
            print("You have already guessed that letter. TRY AGAIN!")
        else: 

            letter_Guessed.append(guess)
            if guess in word:
                print("That is a correct guess, keep going!")
                for x in range(0, length_word):
                    if word[x] == guess:
                        guess_word[x] = guess
                        print(guess_word)

                if not '-' in guess_word:
                    player_score = 0
                    print("You won!")
                    player_score += 1
                    print(player_name,"score is",player_score)
                    print(player_name,"'s score is",player_score)
                    break
            else:
                print("This was a wrong Guess!")
                guess_taken += 1
                print(hangman[guess_taken])
                if guess_taken == 6:
                    print(" Sorry, You have lost the game. Better luck next time!\n The word was", word)
while True:
    change()
    guessing()
    play_again = input("Would you like to play again? yes or no: ").lower()
    if play_again.startswith('y'):
        word = random.choice(answerlist) 
        guess_word = []
        letter_Guessed = []
        guess_taken = 0
        guess = ('')
        change()
        guessing()
    else:
        break


change()
guessing()
