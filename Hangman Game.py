import random

def display_intro():
    print("===================================")
    print("       Welcome to Hangman Game     ")
    print("===================================")
    print("Guess the word one letter at a time.")
    print("You only have 6 incorrect guesses.")
    print("Good luck!\n")

def get_random_word():
    # Predefined word list
    word_list = ["python", "coding", "hangman", "simple", "random"]
    return random.choice(word_list)

def display_word_progress(word, guessed_letters):
    # Display the current state of the guessed word
    display = ''
    for letter in word:
        if letter in guessed_letters:
            display += letter + " "
        else:
            display += "_ "
    return display.strip()

def hangman():
    display_intro()
    
    word_to_guess = get_random_word()
    guessed_letters = []           # To store the correct letters guessed
    incorrect_guesses = 0
    max_guesses = 6
    game_over = False

    while not game_over:
        print("\nWord: ", display_word_progress(word_to_guess, guessed_letters))
        print(f"Incorrect guesses left: {max_guesses - incorrect_guesses}")
        print(f"Guessed letters so far: {', '.join(guessed_letters) if guessed_letters else 'None'}")

        user_input = input("Enter a letter: ").lower()

        # Input validations
        if len(user_input) != 1 or not user_input.isalpha():
            print("❌ Please enter a single alphabet letter.")
            continue
        if user_input in guessed_letters:
            print("🔁 You already guessed that letter.")
            continue

        # Add letter to guessed list
        guessed_letters.append(user_input)

        if user_input in word_to_guess:
            print("✅ Good guess!")
        else:
            incorrect_guesses += 1
            print("❌ Wrong guess!")

        # Check for win condition
        if all(letter in guessed_letters for letter in word_to_guess):
            print("\n🎉 Congratulations! You guessed the word:", word_to_guess)
            game_over = True

        # Check for lose condition
        if incorrect_guesses >= max_guesses:
            print("\n💀 Game Over! You've been hanged.")
            print("The word was:", word_to_guess)
            game_over = True

    print("Thanks for playing Hangman!")

# Run the game
if __name__ == "__main__":
    hangman()
