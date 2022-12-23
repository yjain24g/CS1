'''
Created on Oct 27, 2020
Narrative: A rock paper scissors program that lets you play against the computer
Log: 10/28- Started
    11/1- Finished the Computer interface and user input
    11/2- Added a counter to check how many wins the player or computer had
    11/5- Added best of 3 and 5 modes
    11/6- FINISHED 
    
Bugs: Player would give an infinite loop (FIXED)
Bonuses:
Best of 3 and 5 modes,
Time taken 
@author: yjain24
'''
from random import randint 
import time
import webbrowser
#create a list of play options
t = ["Rock", "Paper", "Scissors"]
#base values to add on

#assign x to a value so we can store the win/loss data of the player
global m
m = 0
#assign y to a value so we can store the win/loss data of the computer
global l
l = 0
#assign a random play to the computer
computer = t[randint(0,2)]

#set player to False
player = False
e = int(input("do you want to play best of 3 or 5 : "))
while player == False:
#set player to True and go through all possible combinations
    player = input("Rock, Paper, Scissors?").lower()
    if player == computer:
        print("Tie!")
    elif player == "rock" or player == "r" and computer == "Paper":
        print("You lose!", computer, "covers", player)
        l = l + 1 
    else:
        print("You win!", player, "smashes", computer)
        m = m + 1
    if player == "paper" or player == "p" and computer == "Scissors":
        print("You lose!", computer, "cut", player)
        l = l + 1
    else:
        print("You win!", player, "covers", computer)
        m = m + 1
    if player == "scissors" or player == "s" and computer == "Rock":
        print("You lose...", computer, "smashes", player)
        l = l + 1
    else:
        print("You win!", player, "cut", computer)
        m = m + 1
else:
    print("That's not a valid play. Check your spelling!")
    #player was set to True, but we want it to be False so the loop continues
    player = False
    computer = t[randint(0,2)]
    print("Player", m,"Computer", l)
    #Best of 5 play, this checks if the computer has won or the player has won.
    #then displays time
    if l == 3 and e == 5:
        print("Computer wins")
        q = round(time.time(), 1)
        o = q / 100000000
        print("Time taken", o)
        webbrowser.open('https://www.youtube.com/watch?v=dQw4w9WgXcQ&ab_channel=RickAstleyVEVO')
        break
    elif m == 3 and e == 5:
        print("Player wins")
        q = round(time.time(), 1)
        o = q / 100000000
        print("Time taken",o)
        webbrowser.open('https://www.youtube.com/watch?v=dQw4w9WgXcQ&ab_channel=RickAstleyVEVO')
        break
    #This is for a best of 3 scenario, same thing as above
    elif l == 2 and e == 3:
        print("Player wins")
        q = round(time.time(), 1)
        o = q / 100000000
        print("Time taken",o)
        webbrowser.open('https://www.youtube.com/watch?v=dQw4w9WgXcQ&ab_channel=RickAstleyVEVO')
        break
    elif m == 2 and e == 3:
        print("Computer wins")
        q = round(time.time(), 1)
        o = q / 100000000
        print("time taken",o)
        webbrowser.open('https://www.youtube.com/watch?v=dQw4w9WgXcQ&ab_channel=RickAstleyVEVO')
        break

    