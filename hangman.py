import random

word_list = ['apple', 'bannana', 'lemon', 'fruit']


'''get_word: function to return a random word from word_list'''
def get_word():
    word = random.choice(word_list)
    return word.upper()

'''
    print_letters_guessed: function to display the letters that have been guessed and the blank spaces for the letters missing
    word: a random word
    guesses: a list of user's guesses
'''
def print_letters_guessed(word, guesses):
    for letter in word:
        if letter.upper() in guesses:
            print(letter, end=" ")
        else:
            print("_", end=" ")
    print()

'''play: function that will run the Hangman game from start to finish'''
def play():
    word = get_word()
    guesses = []
    done = False
    lives = 7

    while not done:
        print_letters_guessed(word, guesses)
        print("You have", lives, "allowed errors left")
        guess = input("Guess a letter: ")
        guesses.append(guess.upper())
        if guess.upper() not in word.upper() or len(guess) > 1 and guess.upper() != word.upper():
            lives -= 1
            if lives == 0:
                break
        elif guess.upper() == word.upper():
            done = True
            break

        done = True
        for letter in word:
            if letter.upper() not in guesses:
                done = False

    print()
    if done:
        print("You guessed the word! It was", word)
    else:
        print("Game Over! The word was", word)

play()
