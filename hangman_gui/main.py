"""
Logan Murray
HangMan GUI
Nov 2020
Simple GUI for a simple Hangman Game
"""

import random, tkinter, os, time

# open text file containing all the words to choice from
with open('C:/Users/sk8in/Desktop/CodeStuff/Python/hangman_gui/word_list.txt', 'r') as word_file:
    word_list = word_file.read().splitlines()

# func to pick random word from list
def pickWord(x = word_list):
    return random.choice(x)

    
# takes list returns string
def to_String(wordList):
    rtnStr = ""
    for ele in wordList:
        rtnStr+=ele
    return rtnStr

# func to generate blanks 
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

# takes the word, the list of blanks for the word, and the guessed letter
# and uses the index of where the letter would be and changes it if correct 
def makeChange(word, word_blank, lttr):
    wordAsList = [char for char in word]
    for index in range(0, len(wordAsList)):
        if wordAsList[index] == lttr:
            word_blank[index] = lttr

# func if you win the game
def youWin(word):
    os.system('cls' if os.name == 'nt' else 'clear')
    print("""  \n\t\t~~ CONGRADULATIONS! ~~ 
    You just WON the game of Harry Potter Hangman :) 
    \t\tYour word: """ + word)

#func if you lose the game
def youLose(word):
    os.system('cls' if os.name == 'nt' else 'clear')
    print("""\n\t\t** You lost the game ** 
                   too many guesses :/
                 Your word was: """ + word)   
    

# func to start the game
def playGame():
    
    #create number of allowed wrong answers
    wrgAns = 6
    
    #create list of wrong guessed letters
    wrong = []

    #determines if they won or not to break loop
    win = "n"
    
    #pick a word from the list and save it
    startWord = pickWord().lower()
    
    #create underscores for blanks
    blanksList = generateBlanks(startWord)

    # print out blanks
    print(to_String(blanksList))

    print(startWord) #debugging purposes, remove later
    
    #begin guess loop
    while wrgAns != 0 or win == "y":
        
        #letters guessed wrong list
        print("\nWrong letters-->", wrong)
        print("Guesses left--> ", wrgAns) 
        
        #ask user for letter
        userGuess = input("Guess a letter: ").lower()
        
        os.system('cls' if os.name == 'nt' else 'clear')
        
        if startWord.count(userGuess) > 0:
            print("\n~~~ correct! ~~~\n")
            makeChange(startWord, blanksList, userGuess)
        else:
            print("\n*** wrong. ***\n")
            wrgAns-=1
            wrong.append(userGuess)
        
        print(to_String(blanksList))
        if to_String(blanksList).count("_ ") == 0:
            win = "y"
            break
    
    
    # end of while loop if guesses are out or won

    if win == "y":
        youWin(startWord.title())
    else:
        youLose(startWord.title())
        wrgAns = 6  


# the play variable is by default y as in yes, let's play
play = "y"
while play != "n" or play != "N":
    playGame()
    ans = input("\nPlay Again? --> ")
    play = ans
print("Thanks for playing! BuhBye.")
time.sleep(3)