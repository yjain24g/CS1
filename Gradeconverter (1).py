'''
Created on Oct 19, 2020

@author: yjain24
'''
def score():
    while True:
        try:
            z = float(input("Enter Score : "))
            if (1 >= z >= 0.9):
                print("Your Grade is an A")
            if (0.9 > z >= 0.8):
                print("Your Grade is a B")
            if (0.8 > z >= 0.7):
                print("Your Grade is a C")
            if (0.7 > z >= 0.6):
                print("Your grade is a D")
            if (z < 0.6):
                print("Your grade is a F")
        except:
            print("Bad score")       
score()
    
