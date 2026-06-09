import random

# list and strings A small list of some predefined strings words
pro_languages = ["object", "hacker", "coder", "syntax", "python"]

# Random: select a random word from our list
secret_word = random.choice(pro_languages)

# setup our initial game state
guessed_letters = []
incorrect_guess_left = 6
print("Welcome to Hungman!")

# while loop: keep the game going as long as they have guesses left
while incorrect_guess_left > 0:
    # create a string to display the current (e.g., "pyt _ _ n")
    display_word = ""
    for letter in secret_word:
        if letter in guessed_letters:
            display_word += " "
        else :
            display_word += "_ "
    print(f"\nWord: {display_word}")
    print(F"Incorrect guesses remaining: {incorrect_guess_left}")
    print(f"Guessed letters: {', '.join(guessed_letters)}")

    # check for a win condition 
    if "_" not in display_word:
        print(f"\nCongratulations! You guessed the word: {secret_word}")
        break # exit the while loop
    # get user input
    guess = input("Guess the letter: ").lower()
    # if-else logic: handle the different scenerios for the user's guess
    if len(guess) != 1 or not guess.isalpha():
        print("Invalid input. Please enter a single letter.")
    elif guess in guessed_letters:
        print("You already guessed that letter! Try different one.")
    elif guess in secret_word:
        print("Good guess!")
        guessed_letters.append(guess)
    else :
        print("Wrong guess!")
        guessed_letters.append(guess)
        incorrect_guess_left -= 1

# if the loop ends and they have o guesses , they lost
if incorrect_guess_left == 0:
    print("Game Over! You've run out of guesses.")
    print(f"The secret word was: {secret_word}")
