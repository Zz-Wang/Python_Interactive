# "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console
# Zhizheng Wang


import simplegui
import math
import random

low = 0
high = 100
max_guess = 0

# helper function to start and restart the game
def new_game(low, high):
    # initialize global variables 
    global secret_number, max_guess
    secret_number = random.randrange(low, high)
    print "New game. Range is from", low, "to", high
    max_guess = int(math.ceil(math.log(high,2)))
    
# define event handlers for control panel
def range100():
    # button that changes the range to [0,100) and starts a new game 
    new_game(0, 100)

def range1000():
    # button that changes the range to [0,1000) and starts a new game     
    new_game(0, 1000)
    
def input_guess(guess):
    # main game logic goes here	
    global your_guess, max_guess
    your_guess = int(guess)
    print "Guess was", your_guess
    #compare the guess with secret
    max_guess = max_guess - 1
    if(max_guess == 0) :
        print "Sorry, you have no more guesses!!"
        new_game(low, high)
    if your_guess > secret_number:
        print "Lower!"
        print "You have " , max_guess , " guesses remaining"
    elif your_guess < secret_number:
        print "Higher!"
        print "You have " , max_guess , " guesses remaining"
    else:
        print "Correct!"
        new_game(low, high)
    print ""
    
    
# create frame
f = simplegui.create_frame("Guess the number", 200, 200)

# register event handlers for control elements and start frame
f.add_button("Range is [0, 100)", range100, 200)
f.add_button("Range is [0, 1000)", range1000, 200)
f.add_input("Enter a guess", input_guess, 200)

# call new_game 
new_game(low, high)


# always remember to check your completed program against the grading rubric
