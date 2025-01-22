# Diepanh (!! MY NAME !!)

# This program automatically sets up a different secret word for each round.
# It is a two player game. Players are allowed to guess one letter in the word at a time.
# Player 1 gets to guess first. Players take turn when the other guesses incorrectly.
# Both should guess the word before a snowman is completely drawn.
# The player who guesses the all the letters in the secret word first is the winner.

import random

def main():
    # Introduce the rules
    gameEntrance = introduction()

    # Starts the game if players input "y" (continue)
    if gameEntrance == "y":

        player1Name = input("Player 1, please enter your name: ") 
        player2Name = input("Pleyer 2, please enter your name: ")
        print()

        # Store the secret word as a string so that it cannot be modified
        secretWord = chooseSecretWord()

        # Automatically set the first turn to be player one. Turn only changes when player guess wrong.
        playerName = player1Name

        listIncorrectGuesses = []
        # Store player's incorrect guesses count as step recognition to draw the snowman
        incorrectGuessesCount = 0
        # Display to player a blank represents the number of letters in the secret word
        blank = []
        blank = initialBlank(secretWord, blank)

        # Initial a grid to draw the snowman
        grid = [["[ ]", "[ ]", "[ ]"], ["[ ]", "[ ]", "[ ]"], 
                ["[ ]", "[ ]", "[ ]"], ["[ ]", "[ ]", "[ ]"]]

         # Print the blank (with guessed and unguessed letters) at the beginning of every guesses
        printBlank(blank)

        # Print the grid with that might holds the snowman inside
        printGrid(grid)


        while "_" in blank and grid[1][2] == "[ ]":

            # Ask for user's guess as one letter
            guess = getGuess(playerName) 

            # Recheck guess until it has met all the rules. Rules are written inside checkValidGuess().
            while not checkValidGuess(guess, listIncorrectGuesses, blank):
                print("Please make another guess.")
                guess = getGuess(playerName)

            if guess not in secretWord:
                listIncorrectGuesses.append(guess)

                incorrectGuessesCount += 1
                # Draw one more piece of the snowman
                drawSnowman(incorrectGuessesCount, grid)

                if playerName == player1Name:
                    playerName = player2Name
                elif playerName == player2Name:
                    playerName = player1Name

            else:
                # Replace a blank with the letter player just guessed
                blank[secretWord.index(guess)] = guess
                addLettersToBlank(blank, guess, secretWord)
            
            print(f"Incorrect Guesses: " + " ".join(listIncorrectGuesses))
            print()

            # Print the blank (with guessed and unguessed letters) at the beginning of every guesses
            printBlank(blank)

            # Print the grid with that might holds the snowman inside
            printGrid(grid)
                    
            
        gameEntrance = "n"
        report(blank, grid, playerName, secretWord)

    elif gameEntrance == "n":
        endGame()

def introduction():
    print()
    print("""This is a two player game called The Snowman Game (originally Hangman).
When entering the game, you have the chances to guess the secret word.
For each time, you are only allowed to guess one letter.
Player who guesses correctly continue to have the chance to guess. 
Player who guesses all the correct letters first wins.
Both loses when the snowman picture is completely drawn.
""")
    
    # Allow players to continue or exit the game
    gameEntrance = input("Press 'y' to enter the game and 'n' to get out of the game: ")
    print()

    # All inputs must be written in or converted to lower case for consistency
    gameEntrance = gameEntrance.lower()

    return gameEntrance


def endGame():
    # Greet players before ending the program
    print("This is the end of The Snowman Game. Thank you for entering!")

# Randomly choose a secret word from a file with 10 different words separated by new lines.
# Future improvements are expected to detect unexpected file contents (e.g.: special characters).

def chooseSecretWord():
    files = open("words.txt", "r")
    listWords = files.readlines()
    files.close()

    # All words in the file are stored in a list
    for n in range(len(listWords)):
        listWords[n] = listWords[n].rstrip("\n").lstrip("\n")

    # Use random function to select a random index (a random word in the list)
    randomNumber = random.randint(0, len(listWords) - 1)

    secretWord = listWords[randomNumber]

    secretWord = secretWord.lower()

    return secretWord

def initialBlank(secretWord, blank):
    # Create a list of blanks that represent each letter of the word
    for letter in secretWord:
        if letter != " ":
            blank.append("_")
        else:
            blank.append(" ") 

    return blank

# Display the guessing progress to the player
def printBlank(blank):
    print("(A Christmas Sweet Treat)")
    print()

    # Display blanks (not succesfully guessed) and letters (successfully guessed) 
    # stored in the program (as list) to the player
    print(" ".join(blank))
    print()

def printGrid(grid):
    print()
    for row in grid:
        print("".join(row))
    print()
    

def getGuess(player):
    # Ask for user's guess
    guess = input(f"{player}, enter your guess: ")
    print()

    return guess

def checkValidGuess(guess, listIncorrectGuesses, blank):
    # Rule 1: The guess has not previously been incorrect.
    if guess in listIncorrectGuesses:
        print("This letter has already been incorrect.")
        print()
        return False
    
    # Rule 2: The guess has not previously been correct.
    elif guess in blank:
        print("This letter has already been guessed correctly.")
        print()
        return False

    # Rule 3: The guess can only be a LETTER.
    elif not guess.isalpha():
        print("You should enter a leter.")
        print()
        return False
    
    # Rule 4: The guess can only be A letter.
    elif len(guess) > 1:
        print("You can only guess one letter at a time.")
        print()
        return False

    # Skip the statements below the function call if all of the above rules are followed
    return True

def drawSnowman(incorrectGuessesCount, grid):
    match incorrectGuessesCount:
        case 1 | 2 | 3:
            grid[3][incorrectGuessesCount - 1] = "[~]"
        case 4 | 5 | 6:
            grid[incorrectGuessesCount - 4][1] = "[O]"
        case 7:
            grid[1][0] = "[\\]"
        case 8:
            grid[1][2] = "[/]"


def addLettersToBlank(blank, guess, secretWord):
    copySecretWord = list(secretWord) 

    # Count the number the letter appears within the secret word to prevent missing duplicate letters
    for n in range(copySecretWord.count(guess)):
        blank[copySecretWord.index(guess)] = guess
        copySecretWord[copySecretWord.index(guess)] = "*"

def report(blank, grid, playerName, secretWord):

    print(f"The word is: {secretWord}")

    if grid[1][2] != "[ ]":
        print("The snowman has been completed.")
        print(f"{playerName} has lost the game!")

    elif "_" not in blank:
        print("Every letters have been guessed.")
        print(f"Congrats {playerName} on winning the game!")

    print()

main()