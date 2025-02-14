import random

# Hangman Logo with ASCII Art
hangman_logo = """
  _______
 |/      |
 |      (_)
 |      \|/
 |       |
 |      / \\
 |      
 |______
"""

print(hangman_logo)
print("Welcome to Hangman! Let's play! 🎮")

# Initial game setup
lives = 5
words_list = ["java", "virat", "championstrophy", "india", "coding", "python", "hangman", "cinema", "music", "gaming", "cricket",
              "football", "technology", "education", "science", "travel", "books", "artificialintelligence",
              "machinelearning", "sports", "innovation", "fitness", "nature", "exploration", "programming", "development",
              "hacking", "chess", "movies", "photography", "food", "astronomy", "space", "history", "language", "culture"]
random_choice = random.choice(words_list)
word_len = len(random_choice)
fill = "_" * word_len
print(f"It's a {word_len}-letter word! 🤔")

correct_letters = []

# Game loop
game_over = False
while not game_over:
    print(f"*********************** {lives}/5 lives left 😱 ******************")
    print("Word to guess:", fill)

    # Get user input
    guess = input("Guess a letter: 🔤\n").lower()

    # Check if the letter has been guessed already
    if guess in correct_letters:
        print(f"⚠️ You've already guessed the letter '{guess}'. Try a different one.")
        continue  # Skip the rest of the loop if the guess is repeated

    # Adding the letter to the list of correct guesses
    correct_letters.append(guess)

    word = ""
    for letter in random_choice:
        if letter in correct_letters:
            word += letter
        else:
            word += "_"

    # If the guess is not in the word, player will lose a life
    if guess not in random_choice:
        lives -= 1
        print(f"❌ '{guess}' is not in the word. You lose a life.")
        if lives == 0:
            game_over = True
            print(f"***************************** 😞 It was '{random_choice}'. You lose! 😞 *****************************")

    # Update the fill with the current word
    fill = word

    # Checking if the player has guessed all letters correctly
    if "_" not in word:
        game_over = True
        print(f"🎉 Congratulations, you win! 🎉 The word was '{random_choice}'. 🎊")

