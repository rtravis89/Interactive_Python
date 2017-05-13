# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console

import simplegui
import random
import math

range_num = 100
# helper function to start and restart the game
def new_game():
    # initialize global variables used in your code here
    global secret_number
    global range_num 
    global counter
    secret_number = random.randrange(0,range_num - 1,1)
    counter = 1
    print 'New game. Range is 1 to ' + str(range_num)

# define event handlers for control panel
def range100():
    # button that changes the range to [0,100) and starts a new game 
    global range_num
    range_num = 100
    new_game()
    

def range1000():
    # button that changes the range to [0,1000) and starts a new game     
    global range_num
    range_num = 1000
    new_game()
    
    
def input_guess(guess):
    # main game logic goes here	
    global secret_number
    global counter
    global range_num
    
    guess_int = int(guess)
    
    print "Guess was " + guess
    if (range_num == 100 and counter < 8):
        print str(7 - counter) + ' guesses left.'
        if guess_int == secret_number:
            print 'Correct'  
            new_game()
        elif guess_int < secret_number:
            counter = counter + 1
            if counter != 8:
                print 'Higher'
            else:
                print 'Out of guesses!'
                new_game()
        elif guess_int > secret_number:
            counter = counter + 1
            if counter != 8:
                print 'Lower'
            else:
                print 'Out of guesses!'
                new_game()
        else:
            print 'Something is wrong'
    elif (range_num == 1000 and counter < 11):
        print str(10 - counter) + ' guesses left.'
        if guess_int == secret_number:
            print 'Correct'    
            new_game()
        elif guess_int < secret_number:
            counter = counter + 1
            if counter != 11:
                print 'Higher'
            else:
                print 'Out of guesses!'
                new_game()
        elif guess_int > secret_number:
            counter = counter + 1
            if counter != 11:
                print 'Lower'
            else:
                print 'Out of guesses!'
                new_game()    
        else:
            print 'Something is wrong'
    else:
        print 'Something went wrong'
# create frame
frame = simplegui.create_frame('Guess the number',200,200)
frame.add_input("Enter guess", input_guess, 200)
frame.add_button('Range is [0, 100) range',range100, 200)
frame.add_button('Range is [0, 1000) range',range1000, 200)
frame.add_button('Reset', new_game, 200)
# register event handlers for control elements and start frame


# call new_game 
new_game()

