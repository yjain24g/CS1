'''
Created on March 14, 2021


@author: yjain24
'''


import os
import pprint
import matplotlib.pyplot as plt
import PIL 
import pygame
import time


def main():
    print("Welcome to the GCDS Directory")
    first_name = input("\nWhats the first name of the person you are looking for?: ")
    last_name = input("\nWhats the last name of the person you are looking for?: ")
    while True:
        print("If you would like to search for info on somebody by their first name, enter 'search first'.")
        print("If you would like to search for info on somebody by their last name, enter 'search last'.")
        print("If you would like to search for info on somebody by their city, enter 'search city'.")
        print("If you would like to add to the directory, enter 'modify'.")
        print("If you would like to delete an entry, enter 'delete'.")
        print("If you would like to count the frequencies of the cities enter 'city'.")
        print("If you would like to count the amount of people assigned to each advisor, enter 'advisors'.")
        print("If you would like to count genders on the list, enter 'gender'.\n")
        
        
        goto = input("Enter Here: ")
        goto == goto.lower()
        first_name = first_name.lower()                     #This isolates the first and last name for functions
        last_name = last_name.lower()
        if goto == "search first":
            hold = searchF(first_name, last_name)
            print(hold)
            tighten = input("Would you like to tighten your parameters? (y/n): ")
            if tighten == "y":
                hold = tightenParameters(hold, first_name, last_name)
                print(hold)
            else:
                print('No results')
        elif goto == "search last":
            hold = searchL(last_name, first_name)
            print(hold)
            tighten = input("Would you like to tighten your parameters? (y/n): ")
            if tighten == "y":
                hold = tightenParameters(hold, first_name, last_name)
                print(hold)
            else:
                print('No results')
        elif goto == "search city":
            city = input("What city are you looking for?: ")
            city = city.lower()
            hold = searchCity(city, first_name, last_name)
            print(hold)
            tighten = input("Would you like to tighten your parameters? (y/n): ")
            if tighten == "y":
                hold = tightenParameters(hold, first_name, last_name)
                print(hold)
            else:
                print('No results')
            print(searchCity(city, first_name, last_name))
        elif goto == "search advisor":
            advisor = input("What is the advisor's last name?: ")
            
            advisor =  '"' + advisor 
            #because the way the data is stored with a ' " ' in front of
            #the last name of the desired advisor, this adds it to allow
            #it to continue to search 
            advisor = advisor.lower()
            hold = searchAdvisor(advisor, first_name, last_name)
            print(hold)
            tighten = input("Would you like to tighten your parameters? (y/n): ")
            if tighten == "y":
                hold = tightenParameters(hold, first_name, last_name)
                print(hold)
            else:
                print('No results')

        elif goto == "search grade":
            grade = input("What grade are you looking for? (N, PK, K, 1-12): ") 
            hold = searchGrade(grade, first_name, last_name)
            print(hold)
            tighten = input("Would you like to tighten your parameters? (y/n): ")
            if tighten == "y":
                hold = tightenParameters(hold, first_name, last_name)
                print(hold)
            else:
                print('No results')
        elif goto == "modify":
            addition()
        elif goto == "delete":
            delete()
        elif goto == "gender":
            d = genderC()
            pprint.pprint(d)
            graph = input("Would you liked this graphed?")
            if graph == "y":
                plt = graphing(d)
                plt.show()
                #this sends the directory to a function I wrote
                #that turns a directory to a graph
            else: continue
        elif goto == "city":
            d = cityFreq()
            pprint.pprint(d)
            #pprint is a imported print function to make a dictionary
            #look more pleasing to the user
            graph = input("Would you liked this graphed? (y/n): ")
            if graph == "y":
                plt = graphing(d)
                plt.show()
            else: continue
        elif goto == "grade":
            d = gradeFreq()
            pprint.pprint(d)
            #pprint is a imported print function to make a dictionary
            #look more pleasing to the user
            graph = input("Would you liked this graphed? (y/n): ")
            if graph == "y":
                plt = graphing(d)
                plt.show()
            else: continue
        elif goto == "advisors":
            d = advisorFreq()
            pprint.pprint(d)
            graph = input("Would you liked this graphed? (y/n): ")
            if graph == "y":
                plt = graphing(d)
                plt.show()
            else: continue
        else:
            print("Sorry! Thats not an option. Please try again.")
            main()

def searchF(first_name, last_name):
    file_in = open("Breh.csv.csv")
    count = 0
    hold =""
    almost = ""
    for line in file_in: #read a line or record of info  ROW!!!
        
        line = line.lower()
        
        list_of_words = line.split(",")  #split into unique element using the delimeter ","
        #print(list_of_words)
        if list_of_words[0] == first_name:
            hold = hold + line
            count = count + 1
    if count == 0:                          #if there are no 
        return "No Found Person"    
    else:
        return hold
    file_in.close()

def searchGrade(grade, first_name, last_name):
    file_in = open("Breh.csv.csv")
    count = 0
    hold = ""
    names = []
    
    for line in file_in:                                                                                    #a loop for every line in the text file
        
        line = line.lower()
        
        list_of_words = line.split(",")                                                              #splits the line into a list at every ","
        if list_of_words[2] == grade:                                                      #checks to see if words match with input
            hold = hold + line
            count = count + 1
    if count == 0:                          #if there are no 
        return "No Found Person"    
    else:
        return hold
    file_in.close()
    
def searchL(first_name, last_name):
    file_in = open("Breh.csv.csv")
    count = 0
    hold = ""
    names = []
    for line in file_in:                                                                                    #a loop for every line in the text file
        
        line = line.lower()
        
        list_of_words = line.split(",")                                                              #splits the line into a list at every ","
        if list_of_words[3] == last_name:                                                      #checks to see if words match with input
            hold = hold + line
            count = count + 1
    
        
    if count == 0:                          #if there are no 
        return "No Found Person"    
    else:
        return hold
    file_in.close()


        

def searchCity(city, first_name, last_name):
    file_in = open("Breh.csv.csv")
    count = 0
    hold = ""
    names = []
    for line in file_in:                                                                                    #a loop for every line in the text file
        
        line = line.lower()
        
        list_of_words = line.split(",")                                                              #splits the line into a list at every ","
        if list_of_words[7] == city:                                                      #checks to see if words match with input
            hold = hold + line
            count = count + 1
    
        
    if count == 0:                          #if there are no 
        return "No Found Person"    
    else:
        return hold
    file_in.close()

def searchAdvisor(advisor, first_name, last_name):
    file_in = open("Breh.csv.csv")
    print(advisor)
    count = 0
    hold = ""
    names = []
    for line in file_in:                                                                                    #a loop for every line in the text file
        
        line = line.lower()
        
        list_of_words = line.split(",")                                                              #splits the line into a list at every ","
        if list_of_words[5] == advisor:                                                      #checks to see if words match with input
            hold = hold + line
            count = count + 1
    
        
    if count == 0:                          #if there are no 
        return "No Found Person"    
    else:
        return hold
    file_in.close()
    
def tightenParameters(hold, first_name, last_name):
    print("Here are your search functions to tighten parameters.\nSearch First name (SF)\nSearch Last name (SL)\nSearch Grade (SG)\nSearch City (SC)\nSearch Advisor(SA)")
    tighten = input("Input here:")
    tighten = tighten.upper()
    hold1 = hold
    final = ""
    if tighten == "SF":
        print("\n")
        hold2 = searchF(first_name, last_name)
        hold1list = hold1.split("\n")
        hold2list = hold2.split("\n")
        #this is a temporary hardcode problem 
        #to remove the empty piece of data made 
        #in the lists above
        
        for i in hold1list:
            for j in hold2list:
                if i == j:
                #if there is a match in the list,
                    final = final + i + "\n"
                    #add it to the return string
        if final == "":
            return "Sorry, no found matches!\n"
        else:
            return final
            
    elif tighten == "SL":
        print("\n")
        hold2 = searchL(last_name, first_name)
        hold1list = hold1.split("\n")
        hold2list = hold2.split("\n")
        #this is a temporary hardcode problem 
        #to remove the empty piece of data made 
        #in the lists above
        
        for i in hold1list:
            for j in hold2list:
                if i == j:
                #if there is a match in the list,
                    final = final + i + "\n"
                    #add it to the return string
        if final == "":
            return "Sorry, no found matches!\n"
        else:
            return final
    elif tighten == "SG":
        grade = input("What grade are you looking for?: ")
        print("\n")
        hold2 = searchGrade(grade, first_name, last_name)
        hold1list = hold1.split("\n")
        hold2list = hold2.split("\n")
        #this is a temporary hardcode problem 
        #to remove the empty piece of data made 
        #in the lists above
        
        for i in hold1list:
            for j in hold2list:
                if i == j:
                #if there is a match in the list,
                    final = final + i + "\n"
                    #add it to the return string
        if final == "":
            return "Sorry, no found matches!\n"
        else:
            return final
    elif tighten == "SC":
        city = input("What city are you looking for?: ")
        print("\n")
        hold2 = searchCity(city, first_name, last_name)
        hold1list = hold1.split("\n")
        hold2list = hold2.split("\n")
        #this is a temporary hardcode problem 
        #to remove the empty piece of data made 
        #in the lists above
        
        for i in hold1list:
            for j in hold2list:
                if i == j:
                #if there is a match in the list,
                    final = final + i + "\n"
                    #add it to the return string
        if final == "":
            return "Sorry, no found matches!\n"
        else:
            return final
    elif tighten == "SA":
        advisor = input("What advisor are you looking for?: ")
        print("\n")
        hold2 = searchAdvisor(advisor, first_name, last_name)
        hold1list = hold1.split("\n")
        hold2list = hold2.split("\n")
        #this is a temporary hardcode problem 
        #to remove the empty piece of data made 
        #in the lists above
        
        for i in hold1list:
            for j in hold2list:
                if i == j:
                #if there is a match in the list,
                    final = final + i + "\n"
                    #add it to the return string
        if final == "":
            return "Sorry, no found matches!\n"
        else:
            return final
    else:
        print("Please input the shortened version of a menu item.")
        
def addition():
    file = open("Breh.csv.csv" , "a")                                                                     #opens the file for appending      
    first = input("first name: ")
    middle = input("middle name: ")
    last = input("last name: ")
    grade = input("grade, K for kindergarden; PK for Pre-K; and N for nursery: ")
    sex = input("M for male and F for female: ")
    teacher = input("Lastname, Firstname of the teacher (REMEMBER THE COMMA): ")
    town = input("enter town: ")
    state = input("State in two letter I.E. Connecticut = CT: ")
    zips = input("Zipcode: ")
    file.write("\n" + first + "," + middle + "," + last + "," + grade + "," + sex + "," + teacher + "," + town + "," + state + "," + zips) 
    #writes in the line to the file as a new one
    file.close()
    return "Added!"
    
def delete():
    input_file = open("Breh.csv.csv", "r")
    output_file = open("temp.txt", "w")
    first = input("\nWhat is the first name of the person you are trying to delete?: \n")
    last = input("What is the last name of the person you are trying to delete?: ")
    first = first.lower()
    last = last.lower()
    #This fixes the problem of miscapitalization.
    count = 0
    for line in input_file:
        line = line.lower()
        data = line.split(",")
        #this splits the line at the comma, making a list
        if data[0] == first and data[2] == last:
        #if the first item in the line matches with the first name and the 3rd item in the line matches with the last name,
            count = count + 1
            continue
        else:
            output_file.write(line)
            #writes the lines not containing the deleted party
    if count > 0:
               
        input_file.close()
        output_file.close()
        os.remove("Breh.csv.csv")
        os.rename("temp.txt", "Breh.csv.csv")
        output_file.close()
        print("Done!")
    else:
        print("Sorry, no results found.")
def genderC():
    file_input = open("Breh.csv.csv")
    d = dict() 
    #this creates a dictonary under variable name 'd'
    #this makes organizing the freqency significantly easier.
    linelist =[]
    for line in file_input:
        line.lower()
        linelist = line.split(',')
        #This converts the line to a list and makes a new item 
        #at every ','
        if linelist[4] not in d:
        #if the fifth (items in lists start at a 0) item in the menu
         #isnt in the directory
             d[linelist[4]] = 0
        else:
             d[linelist[4]] = d[linelist[4]] + 1       
    return d

def cityFreq():
    file_input = open("Breh.csv.csv")
    d = dict()
    #this creates a dictonary under variable name 'd'
    #this makes organizing the freqency significantly easier.
    linelist =[]
    for line in file_input:
        line.lower()
        linelist = line.split(",")
        #This converts the line to a list and makes a new item 
        #at every ','
        if linelist[7] not in d:
        #if the eight  (items in lists start at a 0) item in the menu
         #isnt in the directory    
             d[linelist[7]] = 1
        else:
             d[linelist[7]] = d[linelist[7]] + 1       
    return d
        
def advisorFreq():
    file_input = open("Breh.csv.csv")
    d = dict() 
    #this creates a dictonary under variable name 'd'
    #this makes organizing the freqency significantly easier.
    linelist =[]
    for line in file_input:
        line.lower()
        linelist = line.split(',')
        if linelist[5] not in d:
        #if the sixth (items in lists start at a 0) item in the menu
        #isnt in the directory
             d[linelist[5]] = 1
        else:
             d[linelist[5]] = d[linelist[5]] + 1       
    return d

def gradeFreq():
    file_input = open("Breh.csv.csv")
    d = dict() 
    #this creates a dictonary under variable name 'd'
    #this makes organizing the freqency significantly easier.
    linelist =[]
    for line in file_input:
        line.lower()
        linelist = line.split(',')
        if linelist[3] not in d:
         #if the fourth (items in lists start at a 0) item in the menu
         #isnt in the directory   
             d[linelist[3]] = 1
        else:
             d[linelist[3]] = d[linelist[3]] + 1       
    return d

def graphing(d):
    try:
        keys = d.keys()     
        values = d.values()
        #this separates the matching keys and values to its own 
        #variables, making it easier to work with
        
        
        x = input("What is your X-Axis?: ")
        y = input("What is your Y-Axis?: ")
    
        chart = input("Which chart would you like to use? (line, bar, or pie): ")
        if chart == "line":
            plt.plot(keys, values)
            plt.ylabel(x)
            plt.xlabel(y)
            return plt
        elif chart == "bar":
            plt.bar(keys, values)
            plt.ylabel(x)
            plt.xlabel(y)
            return plt
        elif chart == "pie":
            plt.pie(values, labels = keys, shadow=True, autopct='%1.1f%%',radius=1.3)  
            #To be honest, im not sure what all these mean, but I do know that this 
            #customizes the pie chart.
            return plt
        else:
            print("Sorry! Thats not an option.")
    except:
        print("Error, missing data.")
 

if __name__ == '__main__':
    main()

