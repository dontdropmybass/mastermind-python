import random
import os
import MastermindDBConn

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
print(code) # TODO: remove

while guess < 10 and game:
    clear()
    guess += 1
    game = doGuess(guess)
    
print("You won in "+str(guess)+" turns! Good job!")
