'''
Created on Jan 13, 2021
Narrative: A string iteration program that allows you to check for things in a string and much more
@author: yjain24
Log: 1/14- Started
1/15- Brain dumped code
1/17- Created vowelcount, consonantcount, and palindrome
1/19- Created Enumerat
1/21- Created a Menu and hyphen
1/25- Added First, last and initials
1/28- Changed consonant count and vowel count  

Bugs: 1/17 Vowelcount and consonantcount give infinite recursion
1/28- FIXED
Bonuses:
Enumerate
self inputed list
Menu
Initials
Play again
'''       

 
while True:
    #Creating a menu here for all of the functions
    def option():
        while True:
            op = int(input("Enter option(1-Reversal, 2-Upperlower, 3-Vowel count, 4- Consonantcount, 5- Lists and finding letters, 6- Palindrome, 7- Hyphen, 8- First, last and Initals) : "))
            if op == 1:
                reversal()
                break
            elif op == 2:
                UpLow()
                break
            elif op == 3:
                vowelcount(inp)
                break
            elif op == 4:
                consonantcount(inp)
                break
            elif op == 5:
                enumerat()
                break
            elif op == 6:
                palindrome()
                break
            elif op == 7:
                hyphen()
                break
            elif op == 8:
                Outside()
                break
            else:
                print(" Invalid.... ")
    global inp
    inp = input("What is your name? ")
    def reversal():
        ''' REVERSAL FUNCTION
        Input: Your name (from above)
        Output: A reversed version of that name '''
        global txt
        txt = inp[::-1]
        print(txt)
    
    def UpLow():
        u_or_l = input("Would you like it in upper case (1) or lower case (2)?: ")
        ''' UPPERCASE AND LOWERCASE FUNCTION
        Input: int and str
        int- 1 or 2 for uppercase or not
        str- your name
        output: str- uppercase version of that name '''
        #VARIABLES
        letter_num=0
        output = ""
        
        if u_or_l == "1":
            for index in range(len(inp)):                  #Loop that runs the length of the input
                letter = inp[index]                        #gets letter from word
                letter_num = ord(letter)                    #converts to decimal from a ASCII table
                if letter_num >= 97 and letter_num <= 122:  #checks to see if the decimal is between 97 and 122 (lower case)
                    letter_num = letter_num - 32            #switches it to upper case
                letter = chr(letter_num)                    #switches letter into the new format
                output = output + str(letter)               #appends the output by adding the letter
            print(output)
                  
        elif u_or_l == "2":
            for index in range(len(inp)):                  #see above documentation
                letter = inp[index]
                letter_num = ord(letter)
                if letter_num >= 65 and letter_num <= 90:   #difference here is that it now checks to see if it is between 65 and 90 (upper case
                    letter_num = letter_num + 32            
                letter = chr(letter_num)
                output = output + str(letter)
            print(output)
        else:
            print("Please input letters")
    #counting the Vowels
    def vowelcount(inp):
        '''VOWEL COUNT
        Input: str- your name 
        Output: array- of the frequency of each vowel'''
        vowels = 'aeiou' or 'AEIOU'
        count = {}.fromkeys(vowels,0)
        for char in inp: #Checking for charecter is in the input
            if char in count: #Then making sure if that charecter is in the "count"
                count[char] += 1
        print(count)
        
    def consonantcount(inp):
        '''CONSONANT COUNT 
        Same exact thing as above with consonants'''
        consonants = 'bcdfghjklmnpqrstvwxyz' or 'BCDFGHJKLMNPQRSTVWXYZ'
        count = {}.fromkeys(consonants,0)
        for char in inp:
            if char in count:
                count[char] += 1
        print(count)
    def enumerat():
        '''ENUMERATE
        Here we ask for a user inputted list and how many friends you want
        Input: Str and int and lst 
        int for how many friends and str for the friends names
        Output: Str
        str because we are finding if _ letter is in the list and it returns a string if tripped'''
        lst = []
           
        n = int(input("how many friends? "))
           
        for i in range(0, n):
            ele = input()
               
            lst.append(ele)
        print(lst)
    #Bonus 2 and 3, if the name is a palindrome and if letter is in list
        for char in enumerate(lst): #listing all strings in the list, then checking if that charecter is the letter B
            if char=='Y':
                print('the letter' + char + 'has been located in this list')
            elif char=='y':
                print('The letter' + char + 'has been located in this list')
    #PALINDROMS
    def palindrome():
        '''PALINDROME
        Here we check if the name is a palindrome 
        Input: str (your name)
        Output:str ( e p i c or no palindrome detected)'''
        if inp == inp[::-1]:
            print(" e p i c")
        else:
            print("No palindrome detected")
    #Checks if hyphen
    def hyphen():
        '''HYPHEN
        Here we check if the name has a hyphen
        input: str (your name)
        output: str ( OH NO ITS A HYPHEN or Crisis Averted, no hyphen)'''
        if '-' in inp:
            print('OH NO ITS A HYPHEN')
        else:
            print('Crisis Averted, no hyphen')
    def Outside():
        '''PARSE NAME
        Here we print the first name, first initial and last name'
        input: str (your name)
        output: lst (first name, First initial and last name)'''
        def parse_name(inp):
            fl = inp.split() #splits the str into cohesive words
            first_name = fl[0] # first letter in the name
            last_name1 = fl[len(fl)-1] # For any last name, non-inclusive
            if "." in first_name:
                first_initial = first_name
            else:
                first_initial = first_name[0]+"."
    
                return {'FirstName':first_name, 'FirstInitial':first_initial, 'LastName':last_name1}        print(parse_name(inp))
    option()
    again = input("\n" + "Do you want to play again: ")
    if again == "yes":
        continue
    else:
        break