import random
import os

def clear():
    try:
        return os.system("cls")
    except:
        return os.system("clear")

code = []
guess = 0
game = True

def genCode():
    code = []
    code += random.randint(0,9)
    code += random.randint(0,9)
    code += random.randint(0,9)
    code += random.randint(0,9)
    return code

def doGuess():
    inCode = 0
    correctPos = 0
    currentGuess = input("Enter your guess #"+guess+": ")
    currentGuess.strip()
    b = True
    if len(currentGuess) != 4:
        b = False
    for i in range(4):
        if not currentGuess[i].isDigit():
            b = False
    if not b:
        input("Guesses must be 4 numbers in length. Press enter to continue...")
        clear()
        doGuess()
    for i in range(4):
        if int(currentGuess[i]) == code[i]:
            correctPos += 1
        if int(currentGuess[i]) in code:
            inCode += 1
    print("You guessed "+inCode+" numbers in the code, and "+correctPos+" in the correct position.")
    if correctPos == 4:
        return False
    else:
        return True

# this is the game you dick
name = input("Welcome to mastermind, please enter your name to start: ")

while guess < 10 and game:
    clear()
    guess += 1
    code = genCode()
    game = doGuess()
    
print("You won in "+guess+" turns! Good job!")
