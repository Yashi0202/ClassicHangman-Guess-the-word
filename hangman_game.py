import random
import os
#TODO1 - Update the word list to use the 'word_list' from hangman_word.py
import hangman_words
logo = ''' _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _' | '_ \ / _' | '_ ' _ \ / _' | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/'''
stages = ['''
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
stage_counter = 0

lives = 7
wrong_guess = []

#Todo 2 - Import the logo from hangman art and print it at the starting of the game
print(logo)
chosen_word = random.choice(hangman_words.word_list)
placeholder = ""
for letter in chosen_word:
    placeholder += "_"
print(placeholder)
correct_letters = []
game_over = False

while not game_over:
    guess = input("Please guess a letter:\n").lower()
    os.system('cls' if os.name == "nt" else "clear")
    display = ""
#Todo 3: If user repeat the same guessed letter 
    if guess in correct_letters:
        print(f"You have already guessed {guess}.")
        

#Todo 4: If User guess an incorrect letter
    if guess in wrong_guess:
        print(f"You have already guessed {guess}, but this is wrong.")
    elif guess not in chosen_word:
        print(f"You guessed {guess}, that is not in the word. You lose a life.")
        lives -= 1
        wrong_guess.append(guess)
        print(stages[stage_counter])
        stage_counter += 1

#Todo 5: To show the remaining lives left
        print(f"{lives} out of 7 lives left")
        if lives == 0:
            print("💀 Game Over! The man is hanged. Better luck next time!")
            print(f"The correct word was: {chosen_word}")
            quit()
    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_letters.append(guess)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"
    
    if '_' not in display:
        game_over = True
        print("🏆 You win! Another victory for the word master!")

    print(display)
