import random

# Predefined list of words
words = ["apple", "tiger", "chair", "river", "smile"]

# Randomly select a word
secret_word = random.choice(words)
guessed_letters = []
attempts_left = 6

print("🎯 Welcome to Hangman!")
print("_ " * len(secret_word))

# Game loop
while attempts_left > 0:
    guess = input("\nGuess a letter: ").lower()

    # Check for valid input
    if len(guess) != 1 or not guess.isalpha():
        print("❌ Please enter a single alphabet letter.")
        continue

    # If guessed before
    if guess in guessed_letters:
        print(f"⚠ You already guessed '{guess}'. Try another.")
        continue

    guessed_letters.append(guess)

    # Correct guess
    if guess in secret_word:
        print("✅ Good guess!")
    else:
        attempts_left -= 1
        print(f"❌ Wrong guess! Attempts left: {attempts_left}")

    # Display current progress
    display_word = ""
    for letter in secret_word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "
    print(display_word.strip())

    # Win check
    if all(letter in guessed_letters for letter in secret_word):
        print("\n🎉 Congratulations! You guessed the word:", secret_word)
        break
else:
    print("\n💀 Game Over! The word was:", secret_word)