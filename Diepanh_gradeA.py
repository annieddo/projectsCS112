import random
import time
import playerClass as pc
import cardClass as cc

def main():

    # INPUT: none
    # PROCESS: run the game including calling all functions
    # OUTPUT: none

    game = instructions()
    if game == "y":
        print()
        numberPlayers = int(input("How many players (not including dealer) in this game? "))
        totalPlayersObject = [] # Currently unneccesary
        for num in range(numberPlayers):
            print()
            usernameEntered = input(f"Please enter player {num+1}'s username: ")
            for player in totalPlayersObject:
                if usernameEntered == player.username:
                    usernameEntered = input("Username taken. Please enter another: ")

            if len(usernameEntered) > 10:
                usernameEntered = input("Username is too long. Please enter another: ")
            totalPlayersObject.append(pc.Player(usernameEntered))
        totalPlayersObject.append(pc.Player("dealer"))


        deck = createDeck()

        round = 0
        numPlayersLeft = len(totalPlayersObject)


    while numPlayersLeft != 0:
        round += 1
        print()
        print(f"Round {round}")
        for object in totalPlayersObject:
            if object.stand == False and object.out == False:
                
                print()
                print(f"{object.username}'s turn")
                print()


                if round >= 3:

                    if object.username != "dealer":

                        decisionHitOrStand = hitOrStand(object.username)

                    else:

                        decisionHitOrStand = dealerHitOrStand(object.handVal)

                    if decisionHitOrStand == "stand":
                        object.stand = True
                        numPlayersLeft -= 1


                cardDealtObject = deal(deck)

                if cardDealtObject.rank == "Ace":
                    aceVal = int(input("Please enter the value of your Ace (1 or 11): "))
                    if aceVal == 11:
                        cardDealtObject.val == 11  

                print(cardDealtObject.getCardDealt())               

                print(object.displayHand(cardDealtObject))
                
                object.updateHandVal(cardDealtObject.val)
                
                print(object)

                if object.handVal > 21:
                    print("You've busted.")
                    object.out = True
                    if object.username != "dealer":
                        numPlayersLeft -= 1
                    else:
                        numPlayersLeft = 0

                elif object.handVal == 21:
                    print("You've won.")
                    object.out = True
                    if object.username != "dealer":
                        numPlayersLeft -= 1
                    else:
                        numPlayersLeft = 0

        dealerFinalHandVal = totalPlayersObject[-1].handVal



    for object in totalPlayersObject:
        if object.out == False:
            if dealerFinalHandVal > 21:
                print(f"{object.username} wins.")
            elif dealerFinalHandVal == 21:
                print(f"{object.username} lost.")
            else:
                if object.handVal > dealerFinalHandVal:
                    print(f"{object.username} wins.")
                elif object.handVal < dealerFinalHandVal:
                    print(f"{object.username} lost.")
                else:
                    print("It's a tie.")


    endGame()


def instructions():

    # INPUT: none
    # PROCESS: print out instructions
    # OUTPUT: none

    print()
    print("""This game is called Blackjack.
Each player plays against the dealer of the game.
Player(s) and dealer take turn dealing a card. Dealer deals last, and then new round begins.
From round 3, all player(s) get asked if they want to hit or stand, meaning continue or stop.
""")
    game = input("Press Y if you want to enter the game: ").lower()
    return game

def endGame():
    print("""Thank you for playing this game.
Hopefully you've gotten an enjoyable experience.
Let's come back another time!""")
    
def createDeck():
    cardList = []
    suits = ["Spades", "Hearts", "Clubs", "Diamonds"]
    specialVals = {"Ace": 1, "King": 10, "Queen":  10, "Jack": 10}

    for rank in range(2, 11):
        for suit in suits:
            cardList.append(cc.Card(str(rank), suit, rank))
    
    for specialVal in specialVals:
        for suit in suits:
            cardList.append(cc.Card(specialVal, suit, specialVals[specialVal]))

    return cardList

def deal(deck):

    # INPUT: deck
    # PROCESS: deal a card randomly from deck
    # OUTPUT: cardDealt

    random.shuffle(deck)
    cardDealt = deck[0]
    time.sleep(2)

    return cardDealt


def hitOrStand(currentPlayer):

    # INPUT: current player or object.username
    # PROCESS: take in user's input as decision to hit or stand
    # OUTPUT: decision

    decisionHitOrStand = input(f"{currentPlayer}, hit or stand? ('hit' / 'stand'): ").lower()

    return decisionHitOrStand

def dealerHitOrStand(dealerHandVal):

    # INPUT: dealer's hand value
    # PROCESS: decide hit or stand for dealer based on their hand value
    # OUTPUT: decision

    if dealerHandVal <= 16:
        decisionHitOrStand = "hit"
    else:
        decisionHitOrStand = "stand"

    return decisionHitOrStand

    
if __name__ == "__main__":
    main()
