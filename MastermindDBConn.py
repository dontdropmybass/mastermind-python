#!/usr/bin/python
import sqlite3

conn= sqlite3.connect('HighScores.sqlite')

def Select():
    #Select Statement
    cursor = conn.execute("SELECT * from Scores ORDER BY Stage, Time LIMIT 0,10")
    for row in cursor:
        print("Name: " , row[1], " Stage: " , row[2], " Time: " , row[3])
        
def Insert():
    #Gather values
    name = input("Enter Name: ")
    Stage = input("Stage: ")
    Time = input("Time: ")
    #Insert into Statement
    conn.execute("INSERT INTO Scores (Name,Stage,Time) VALUES('{name}','{stage}','{time}')".\
            format(name=name, stage = Stage, time = Time))
    conn.commit()

def Insert(Name, Stage, Time):
    conn.execute("INSERT INTO Scores (Name,Stage,Time) VALUES('{name}','{stage}','{time}')".\
                 format(name=Name, stage = Stage, time = Time))
    conn.commit()
   
def Close():
    #Close Statement
    conn.close()
    
#//Sample Run (slashes because ben forgot python)
#conn= sqlite3.connect('HighScores.sqlite')
#Select()
#Insert()
#Close()
