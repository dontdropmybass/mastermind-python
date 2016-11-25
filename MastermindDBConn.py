#!/usr/bin/python
import sqlite3
conn= sqlite3.connect('HighScores.sqlite')



#Statement
cursor = conn.execute("SELECT * from Scores ORDER BY Stage, Time")
for row in cursor:
    print("Name: " , row[1], " Stage: " , row[2], " Time: " , row[3])
conn.close()
