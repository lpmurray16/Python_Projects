"""
Logan Murray
HangMan GUI
Nov 2020
Simple GUI for a simple Hangman Game
"""

import random, tkinter

# open text file containing all the words to choice from
with open('C:/Users/sk8in/Desktop/CodeStuff/Python/hangman_gui/word_list.txt', 'r') as word_file:
    word_list = word_file.read().splitlines()

# func to pick random word from list
def pickWord(x = word_list):
    return random.choice(x)

# func to print out blanks as string
def printBlanks(blankList):
    blanks = ""
    for ele in blankList:
        blanks+=ele
    print(blanks)


# func  to generate blanks 
def generateBlanks(word):
    blank = [char for char in word]
    for index in range(0, len(blank)):
        if blank[index] == ' ':
            continue
        else:
            blank[index] = "_ "
    return blank

# func to search for letter in word
def searchWord(word, letter):
    loc = []
    for index in range(0, len(word)):
        if(word[index] == letter):
            loc.append(index)
    return loc

# func to start the game
def playGame():
    
    #create number of wrong answers
    wrgAns = 6
    
    #create list of wrong guessed letters
    wrong = []
    
    #pick a word from the list and save it
    startWord = pickWord()
    
    #create underscores for blanks
    blanksList = generateBlanks(startWord)

    # print out blanks
    printBlanks(blanksList)

    print(startWord) #debugging purposes
    
    #begin guess loop
    while wrgAns != 0:
        
        #letters guessed wrong list
        print("Wrong letters-->", wrong) 
        
        #ask user for letter
        userGuess = input("Guess a letter: ")
        indexOfLetter = searchWord(startWord, userGuess)
        
        # check to see if it is correct
        if(len(indexOfLetter) > 0):
            #show correct guess on screen
            print('\ncorrect\n')
            print(indexOfLetter) #debugging purposes
        else:
            #add to wrong letter list and decrement
            print('\nwrong\n')
            wrong.append(userGuess)
            wrgAns-=1


playGame()