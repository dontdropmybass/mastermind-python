__author__ = 'benvc'
import random
Turn = 1
CorrectArray = ["","","",""]
Array0 = ['#',"#","#","#",""]
Array1 = ["x","x","x","x",""]
Array2 = ["x","x","x","x",""]
Array3 = ["x","x","x","x",""]
Array4 = ["x","x","x","x",""]
Array5 = ["x","x","x","x",""]
Array6 = ["x","x","x","x",""]
Array7 = ["x","x","x","x",""]
Array8 = ["x","x","x","x",""]
ArrayList = [Array0,Array1,Array2,Array3,Array4,Array5,Array6,Array7,Array8]
##Print List Method
def printList():
    for i in range(9):
        print(ArrayList[i][0], ArrayList[i][1],ArrayList[i][2],ArrayList[i][3],ArrayList[i][4])
def CheckCorrect():
    rand = 0
#Random Number for Correct list
for i in range(4):
    rand = random.randrange(10)
    CorrectArray[i] = (rand)

print("Welcome to MasterMind, try to crack the within 8 tries to win.")
printList()

