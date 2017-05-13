# implementation of card game - Memory
# State logic is wrong, see mini_proj5_OOP for correct state logic

import simplegui
import random

exposed = [False, False, False, False, False, False, False, False, False, False,
          False, False, False, False, False, False]
cards = range(0,8)
cards.extend(range(0,8))
num_tracker = []
matched_nums = []
counter = 0



# helper function to initialize globals
def new_game():
    global cards, state, counter, exposed
    state = 0
    random.shuffle(cards)
    counter = 0
    exposed = [False, False, False, False, False, False, False, False, False, False,
          False, False, False, False, False, False]
    label.set_text("Turns = " +str(counter))
     
# define event handlers
def mouseclick(pos):
    # add game state logic here
    global cards, exposed, state, num_tracker, matched_nums, counter
    for i in range(0, len(cards)):
        a = 0+i*50
        c = 50+i*50
        if (a < pos[0] and c > pos[0]) and state == 0 and exposed[i] == False:
            exposed[i] = True
            state = 1
            num_tracker.append(cards[i])
        elif (a < pos[0] and c > pos[0]) and (state == 1 and exposed[i] == False):
            exposed[i] = True
            state = 2
            num_tracker.append(cards[i])
        elif (a < pos[0] and c > pos[0]) and state == 2 and exposed[i] == False:  
            #print matched_nums, num_tracker
            if num_tracker[0] == num_tracker[1]:
                matched_nums.append(num_tracker[0])
                for j in range(0, len(cards)):
                        if cards[j] in matched_nums:
                            exposed[j] = True
                        else:
                            exposed[j] = False
                exposed[i] = True
                state = 1
                num_tracker[:] = []
                num_tracker.append(cards[i])
            else:
                if len(matched_nums) == 0:
                    for j in range(0, len(cards)):
                        exposed[j] = False
                else:
                    for j in range(0, len(cards)):
                        if cards[j] in matched_nums:
                            exposed[j] = True
                        else:
                            exposed[j] = False
                exposed[i] = True
                counter = counter + 1
                label.set_text("Turns = " +str(counter))
                state = 1
                num_tracker[:] = []
                num_tracker.append(cards[i])

                        
# cards are logically 50x100 pixels in size    
def draw(canvas):
    global cards, exposed, counter
    
    
    #Draw Green rectangular cards   
    for i in range(0, len(cards)):
        if exposed[i] == False:
            a = 0+i*50
            b = 0
            c = 50+i*50
            d = 100
            canvas.draw_polygon([(a, b), (a, d), (c, d), (c, b)], 2, "Green", "Green")
            canvas.draw_line([c,b], [c,d], 5, 'Black')
        elif exposed[i] == True:
            canvas.draw_text(str(cards[i]), [23+(i*50), 50], 16, "White")


# create frame and add a button and labels
frame = simplegui.create_frame("Memory", 800, 100)
frame.add_button("Reset", new_game)
label = frame.add_label("Turns = 0")


# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

# get things rolling
new_game()
frame.start()


# Always remember to review the grading rubric