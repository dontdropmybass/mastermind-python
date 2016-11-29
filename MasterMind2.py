import random
import os
import time
import MastermindDBConn as db

def clear():
    try:
        return os.system("cls") + os.system("clear")
    except:
        return 1

code = []
guess = 0
game = True

def genCode():
    code = [random.randrange(10),random.randrange(10),random.randrange(10),random.randrange(10)]
    return code

def doGuess(guess):
    inCode = 0
    correctPos = 0
    currentGuess = input("Enter your guess #"+str(guess)+": ")
    currentGuess.strip()
    b = True
    if len(currentGuess) != 4:
        b = False
    for i in range(len(currentGuess)):
        if not currentGuess[i].isdigit():
            b = False
    if not b:
        input("Guesses must be 4 numbers in length. Press enter to continue...")
        currentGuess = ""
        clear()
        doGuess(guess)
    for i in range(len(currentGuess)):
        if int(currentGuess[i]) == code[i]:
            correctPos += 1
        if int(currentGuess[i]) in code:
            inCode += 1
    print("You guessed "+str(inCode)+" numbers in the code, and "+str(correctPos)+" in the correct position.")
    if correctPos == 4:
        return False
    else:
        return True

# this is the game you dick
name = input("Welcome to mastermind, please enter your name to start: ")
code = genCode()
start = time.time()
while guess < 10 and game:
    clear()
    guess += 1
    game = doGuess(guess)

if not game:
    print("You won in "+str(guess)+" turns! Good job!\n\n")
    print("--------------------------------------------------\n\n")
    db.Insert(name,str(guess),str(time.time()-start))
    db.Select()
else:
    print("Sorry, you fail.")
    print("The correct combo is: ")
    print(code)
    print("\n\n--------------------------------------------------\n\n")
    db.Select()
input("\n\nPress enter to quit")
db.Close()
