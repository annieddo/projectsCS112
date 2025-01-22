import random

def main():
    instructions()
    userName1, userName2 = getUsersName()
    # initilize each player's win count
    userWin1 = 0
    userWin2 = 0
    # initialize each player's previous guesses list
    listPreviousGuessUser1 = []
    listPreviousGuessUser2 = []
    # make a loop to start a new round
    for round in range(3):
        print("Let's start a new round!")
        correctNumber, factor = getCorrectNumber()
        # set 6 chances maximum for 3 turns for each player each game
        chance = 6
        # set the first turn to be player 1
        userTurn = 1
        listPreviousGuessUser1 = []
        listPreviousGuessUser2 = []
        # condition if there are still chances to player
        while chance > 0:
            usersGuess = getUsersGuess(userTurn, userName1, userName2, factor,
                                       listPreviousGuessUser1, listPreviousGuessUser2)
            chance, userWin1, userWin2 = giveHint(usersGuess, correctNumber, chance, 
                                                  userTurn, userWin1, userWin2)
            # condition to let players alternately take turn
            if userTurn == 1:
                userTurn = 2
            else:
                userTurn = 1
    endGame(userWin1, userWin2, userName1, userName2)


def instructions():
    print("""
This is a guessing game tournament.
There are a total of 3 rounds. Two players will be playing against each other.
A number between 1 and 100 is selected, and it is also a multiple of a number between 4 and 10 selected in each round.
The factor will be announced at the beginning of each round. Factor can be the same for different rounds.
The winner is the one who wins most rounds within the tournament.
""")
    # receive any input to proceed
    input("Press enter if you understand the rules to start the game: ")
    print()   

# receive two players' names as inputs and return
def getUsersName():
    userName1 = input("Please enter Player 1's name: ")
    # condition if no name is given
    if userName1 == "":
        print("Please enter anything for your name. It would be easier to call you when it is your turn!")
        userName1 = input("Please enter Player 1's name: ")
    userName2 = input("Please enter Player 2's name: ")
    # condition if no name is given
    if userName2 == "":
        print("Please enter anything for your name. It would be easier to call you when it is your turn!")
        userName1 = input("Please enter Player 2's name: ")
    # condition if the same name is given
    elif userName2 == userName1:
        print("That name has already been picked. Please choose a new one. It would be easier to call you when it is your turn!")
        userName2 = input("Please enter Player 2's name: ")
    print()
    return userName1, userName2 


def getCorrectNumber():
    # select a random correct number between 1 and 100
    correctNumber = random.randint(1, 100)
    # select a random factor between 4 and 10
    factor = random.randint(4, 10)
    # keep randomly selecting a correct number until it is divided by the factor recently selected
    while correctNumber % factor != 0: 
        correctNumber = random.randint(1, 100)
    print(f"The factor this round is: {factor}.")
    print()
    return correctNumber, factor


def getUsersGuess(userTurn, userName1, userName2, factor, listGuesses1, listGuesses2):
    # set the username to be called as the name of the players received when they entered their names
    # set the list guesses to be the person guessing 's list guesses when it is their turn
    if userTurn == 1:
        userName = userName1
        listGuesses = listGuesses1
    else:
        userName = userName2
        listGuesses = listGuesses2
    if listGuesses != []:
        print(f"These are your previous guesses: {listGuesses}")
        usersGuess = int(input(f"{userName}, please enter your new guess: "))
    else:
        usersGuess = int(input(f"{userName}, please enter your guess: "))
    # keep asking for another guess if the current guess is in valid by calling the check valid function
    # the invalid guess is not counted as a turn
    while not checkValidInput(usersGuess, factor):
        print(f"The guess should be a number between 1 and 100 and multiple of {factor}.")
        usersGuess = int(input(f"{userName}, please re-enter your guess: "))
    listGuesses.append(usersGuess)
    return usersGuess


def checkValidInput(usersGuess, factor):
    # return False to the call to check validation if the guess is invalid
    # return True if it is valid
    if usersGuess not in range(1,101) or usersGuess % factor != 0:
        print("Your guess is not valid. You have to make another one.")
        return False
    else:
        return True
        

def giveHint(userGuess, correctNumber, chance, userTurn, userWin1, userWin2):
    # condition if a guess is right
    if userGuess == correctNumber:
        # tell the player in turn that their guess is right
        print("Your guess is right! You have won the game.")
        print()
        # take away any next turns of both players
        chance = 0
        # count 1 win for the player got it right after each game based on whose turn it is
        if userTurn == 1:
            userWin1 += 1
        else:
            userWin2 += 1
    # condition if the guess is wrong
    else:
        # tell them whether the guess is lower or higher than the correct number
        if userGuess < correctNumber:
            print("Your guess is too low.")
            print()
        else:
            print("Your guess is too high.")
            print()
        # take away one turn after one guess
        chance -= 1
    return chance, userWin1, userWin2


def endGame(userWin1, userWin2, userName1, userName2):
    # end game statement no matter the results
    print(f"This is the end of the game.")
    # condition if no one gets anything any game
    if userWin1 == userWin2 == 0:
        print(f"No one wins any rounds. Better luck next time!")
    # condition if both players have a draw or each wins one game
    elif userWin1 == userWin2 != 0:
        print(f"This is a draw! Congratulations both!")
    # condition if there is a winner
    else:
        # identify who the winner is for a congratulation
        if userWin1 > userWin2:
            winner = userName1
        else:
            winner = userName2
        # congratulate the winner 
        print(f"Congratulations {winner} on winning the tournament! You have more wins in total!")
    print()

main()

