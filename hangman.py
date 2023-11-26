import random

def hangman():
    word_list = ["apple", "banana", "cherry", "durian", "elderberry"]  # List of words to choose from
    chosen_word = random.choice(word_list).lower()  # Randomly select a word from the list
    guessed_letters = []  # List to store the guessed letters
    attempts = 6  # Number of attempts allowed
    
    while True:
        print("\n")
        print(" ".join([letter if letter in guessed_letters else "_" for letter in chosen_word]))
        
        if set(chosen_word) == set(guessed_letters):
            print("Congratulations! You guessed the word correctly!")
            break
        
        if attempts == 0:
            print("Game Over! You ran out of attempts.")
            print("The word was:", chosen_word)
            break
        
        guess = input("Guess a letter: ").lower()
        
        if guess.isalpha() and len(guess) == 1:
            if guess in guessed_letters:
                print("You already guessed that letter. Try again.")
            elif guess in chosen_word:
                print("Correct guess!")
                guessed_letters.append(guess)
            else:
                print("Wrong guess!")
                attempts -= 1
                print("Attempts remaining:", attempts)
                guessed_letters.append(guess)
        else:
            print("Invalid input. Please enter a single letter.")
            
hangman()

