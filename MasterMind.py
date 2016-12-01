import random
import os
import time
import MastermindDBConn as db

def clear():
    # this works on windows
    try:
        return os.system("cls") + os.system("clear")
    except:
        return 1
# code as an array
code = []
# guess counter
guess = 0
# whether or not the game is still being played
game = True

def genCode():
    # generated a random code
    code = [random.randrange(10),random.randrange(10),random.randrange(10),random.randrange(10)]
    return code

def doGuess(guess):
    inCode = 0
    correctPos = 0
    # user makes a guess
    currentGuess = input("Enter your guess #"+str(guess)+": ")
    currentGuess.strip()
    b = True
    # check if the guess is in the correct format
    if len(currentGuess) != 4:
        b = False
    for i in range(len(currentGuess)):
        if not currentGuess[i].isdigit():
            b = False
    if not b:
        # show them they're wrong and try again
        input("Guesses must be 4 numbers in length. Press enter to continue...")
        currentGuess = ""
        # clear()
        doGuess(guess)
    for i in range(len(currentGuess)):
        # check the code and show them how many
        # numbers they guessed correctly
        if int(currentGuess[i]) == code[i]:
            correctPos += 1
        if int(currentGuess[i]) in code:
            inCode += 1
    print("You guessed "+str(inCode)+" numbers in the code, and "+str(correctPos)+" in the correct position.")
    if correctPos == 4:
        # if they guess the code correctly,
        # end the game
        return False
    else:
        return True

##### Main Game Code
# ask for their name
name = input("Welcome to mastermind, please enter your name to start: ")
# generate the code
code = genCode()
# find out what time it is right now
start = time.time()
clear()
# for ten guesses,
while guess < 10 and game:
    guess += 1
    # do the guess
    game = doGuess(guess)

if not game:
    # if they win, put their score in the database
    print("You won in "+str(guess)+" turns! Good job!\n\n")
    print("--------------------------------------------------\n\n")
    db.Insert(name,str(guess),str(time.time()-start))
    db.Select()
else:
    # if they don't win, tell them the code
    # and how bad they are
    print("Sorry, you fail.")
    print("The correct combo is: ")
    print(code)
    print("\n\n--------------------------------------------------\n\n")
    db.Select()
input("\n\nPress enter to quit")
db.Close()
