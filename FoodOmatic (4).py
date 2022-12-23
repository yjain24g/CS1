'''
Created on Nov 30, 2020
Description- A food geneartor that gives you food and how many of it
Bugs- Try... Except gives an infinite loop (FIXED)
Log:  12/1- Started
    12/3- Created bare minimum
    12/6- Added Price an how many meals
    12/7- Created the while loop
    12/9- Added what food do you not like and spell check
        FINISHED
Bonuses: 
Added pricing
Spell check
Shuffle for more randomness
Foods you dont like
@author: yjain24
'''
#For the Random.randint function
import random
#Shuffle for adding extra randomness
from random import shuffle
#Spellcheck
from textblob import TextBlob
def main():
    n = int(input("How many meals do you want : "))
    pr = str(input("What food do you not like : "))
    prC = TextBlob(pr)
    print("corrected text: "+str(prC.correct()))
    prCC = prC.correct()
    #Our first food set
    food1 = ['local' , 'roasted' , 'grilled' , 'garlic mashed' , 'oven dried' , 'spiced' , 'stewed' , 'assorted' , 'iced' , 'sliced' , 'braised' , 'free-range' , 'baby' , 'teriyaki glazed' , 'steamed']
    price1 = [ 1.50 , 2.00 , 2.50 , 3.00 , 2.50 , 4.00 , 5.00 , 3.75 , 4.00 , 2.00 , 1.00 , 2.75 , 3.00 , 4.50 , 9.00]
    #Second food set
    food2 = ['cauliflower' , 'tilapia fillet' , 'pork loin' , 'green beans' , 'basmati rice' , 'rainbow carrots' , 'fingerling potatoes' , 'three color squash' , 'potatoes' , 'eggplant' , 'drumstick' , 'short rib' , 'duck breast' , 'eye round of beef' , 'baguette']
    price2 = [ 0.75 , 1.00 , 2.00 , 1.45 , 2.99 , 3.45 , 4.50 , 5.25 , 6.00 , 5.00 , 4.99 , 5.50 , 0.50 , 0.99 , 9.50]
    #Third food set
    food3 = ['with fennel' , 'gratin' , 'bengali style' , 'with peas' , 'pizza' , 'with balsamico' , 'with garlic and olive oil' , 'with pigeon peas' , 'with minted yogurt' , 'soup' , 'cutney' , 'salad' , 'with tropical friut salsa' , 'over sticky rice' , 'au jus']
    price3 = [ 0.95 , 3.00 , 4.00 , 2.60 , 5 , 1.99 , 4 , 2.50 , 6.50 , 2.00 , 3.99 , 2.50 , 3.50 , 4.99 , 10.50]
    #We are shuffling the lists for an extra element of randomness
    shuffle(food1)
    shuffle(price1)
    shuffle(food2)
    shuffle(price2)
    shuffle(food3)
    shuffle(price3)
    #Simple loop
    i = 0
    while i < n:
        #We use -1 to indicate that the rand int isnt inclusive
        randomnum = random.randint(0, len(food1)-1) 

        randomnum1 = random.randint(0, len(food2)-1) 

        randomnum2 = random.randint(0, len(food3)-1)
        
        price = price1[randomnum] + price2[randomnum1] + price3[randomnum2]
        #Price is measured to hundreths
        r = round(price, 3)
            
        r = int(r)
            #exclude any foods that have things we didnt like
        if food1[randomnum] == prCC:
            print('We encountered a food you didnt like')
        elif food2[randomnum1] == prCC:
            print('We encountered a food you didnt like')
        elif food3[randomnum2] == prCC:
            print('We encountered a food you didnt like')
        else:
            print(food1[randomnum] , food2[randomnum1], food3[randomnum2],', Your total will come out to be', r, '$' )
  
        i += 1 
         
if __name__ == '__main__':
    main()
 
