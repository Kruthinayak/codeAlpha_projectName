import random

# Step 1: Define a list of 5 words
word_list = ["apple", "tiger", "chair", "house", "robot"]

# Step 2: Randomly select a word
chosen_word = random.choice(word_list)
guessed_letters = []
tries = 6

# Step 3: Game loop
print("Welcome to Hangman!")

while tries > 0:
    # Display current state of the word
    display_word = ""
    for letter in chosen_word:
        if letter in guessed_letters:
            display_word += letter
        else:
            display_word += "_"
    
    print("Word:", display_word)

    # Check if the player has won
    if "_" not in display_word:
        print("Congratulations! You guessed the word:", chosen_word)
        break

    # Take a guess
    guess = input("Guess a letter: ").lower()

    if guess in guessed_letters:
        print("You already guessed that letter.")
    elif guess in chosen_word:
        print("Good guess!")
        guessed_letters.append(guess)
    else:
        print("Wrong guess.")
        guessed_letters.append(guess)
        tries -= 1
        print("Tries left:", tries)

# Step 4: Game over
if tries == 0:
    print("Sorry, you lost. The word was:", chosen_word)
