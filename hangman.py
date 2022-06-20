
import random
import string
import time

words = ["Kwantlen", "Rai", "Zimmerman", "apple", "hockey", "pear", "soccer", "basketball", "raptor", "James", "coding", "computer", "mouse", "phone", "turtle", "Lamelo", "chicken", "chair", "family", "vehicle", "grass", "center", "cucumber", "xylophone", "zebra", "queen"]
# the next three lines of code makes sure that the words kwantlen, rai, and zimmerman are not chosen for the hangman
words.remove("Kwantlen")
words.remove("Rai")
words.remove("Zimmerman")

correct_letter = ["That's in the word", "Good guess", "Lucky or skill?", "W mans you guessed right"]
# this line of code stores random messages that will be displayed whenever the user guesses correct
wrong_letter = ["Uh oh that wasn't a good guess", "Unlucky", "Your lives are running out", "L mans you guessed wrong"]
# this line of code stores random messages that will be displayed whenever the user guesses incorrect

# these are the drawings that are displayed whenever the user guesses a wrong number
lives_visual_dict = {
        0: """
                ___________
               | /        | 
               |/        ( )
               |        \ | /
               |         / \\
               |
           """,
        1: """
                ___________
               | /        | 
               |/        ( )
               |        \ |
               |         / \\
               |
            """,
        2: """
              ___________
               | /        | 
               |/        ( )
               |          |
               |         / \\
               |
            """,
        3: """
               ___________
               | /        | 
               |/        ( )
               |          |
               |         / 
               |
            """,
        4: """
               ___________
               | /        | 
               |/        ( )
               |          |
               |          
               |
            """,
        5: """
               ___________
               | /        | 
               |/        ( )
               |          
               |          
               |
            """,
        6: """
                ___________
               | /        | 
               |/        
               |          
               |          
               |
            """,
        7: "",
    }

def get_valid_word(words):
    word = random.choice(words)  # randomly chooses a word
    while "-" in word or ' ' in word:
        word = random.choice(words)

    return word.upper()

positivepoints = 0 #This stuff is going to be my modification
negativepoints = 0 #This stuff is going to be my modification

def hangman():
    word = get_valid_word(words)
    word_letters = set(word) 
    alphabet = set(string.ascii_uppercase)
    used_letters = set()  # what user guessed

    lives = 7

    # getting user input
    while len(word_letters) > 0 and lives > 0:
        print("You have " + str(lives) + " lives left and you have used these letters: ", " ".join(used_letters))

        # what current word is (ie W - R D)
        word_list = [letter if letter in used_letters else '-' for letter in word]
        print(lives_visual_dict[lives])
        print("Current word: " , " " .join(word_list))

        user_letter = input("Guess a letter: ").upper()
        time.sleep(1) #this line of code adds a 1 sec delay after a guess in order to add suspense
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
                print(random.choice(correct_letter)) #This prints a random phrase that was in the list, correct_letter, because the user guessed correctly
                global positivepoints
                positivepoints += 2 #if a user guesses a correct letter, their point total will increase by 2

            else:
                lives = lives - 1  # takes away a life if wrong
                print("Your letter, " + user_letter + " is not in the word. " + random.choice(wrong_letter)) 
                #The line of code above prints a random phrase that was in the list, wrong_letter, because the user guessed incorrectly
                global negativepoints
                negativepoints += -1 #if a user guesses an incorrect letter, their point total will decrease by 1

        elif user_letter in used_letters:
            print("You have already used that letter. Guess another letter.")

        else:
            print("That is not a valid letter.")

    # this code is run when the word is guessed or when you run out of lives
    if lives == 0:
        print(lives_visual_dict[lives])
        print("You lost. The word was", word)
        print("Points: " + str(positivepoints + negativepoints)) #The total number of points is printed if the user loses
    else:
        print("You guessed the right word. It was", word)
        print("Points: " + str(positivepoints + negativepoints)) #The total number of points is printed if the user wins

if __name__ == "__main__":
    print("""
                ___________
               | /        
               |/        
               |          
               |          
               |
            """) #this is the drawing displayed before the game even begins
    print("You get 2 points for a correct guess, and you lose a point for a wrong guess. Try achieving the highest score possible") # pre game instructions
    hangman()

play_again = input("Do you want to play again? (Y) or (N): ").lower() #This code asks the user if they want to play again after winning or losing the previous game

while play_again == "y":
    positivepoints = 0 #These two lines of code reset points to 0 so multiple game points aren't added up
    negativepoints = 0 
    print("""
                ___________
               | /        
               |/        
               |          
               |          
               |
            """) # this is the drawing dispalyed before the game begins
    print("You get 2 points for a correct guess, and you lose a point for a wrong guess. Try achieving the highest score possible") # pre game instrcutions
    hangman() #This code re runs the hangman game if the user decides to continue playing
    play_again = input("Do you want to play again? (Y) or (N): ").lower()
    if play_again == "n":
        print("You have succesfully quit") #this code ends the game because the user decided they did not want to continue playing