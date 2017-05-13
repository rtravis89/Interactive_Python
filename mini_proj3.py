# template for "Stopwatch: The Game"

# define global variables
import simplegui

counter = 0
correct_stop = 0
total_stop = 0
watch_running = False
# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(t):

    a = counter // 600
    b = ((counter // 10) % 60) // 10
    c = ((counter // 10) % 60) % 10
    d = counter % 10
    return str(a) + ':' + str(b) + str(c) + '.' + str(d)
    
# define event handlers for buttons; "Start", "Stop", "Reset"
def start():
    global watch_running
    watch_running = True
    timer.start()
    
def stop():
    global correct_stop
    global total_stop
    global counter
    global watch_running
    timer.stop()
    if watch_running == True and (counter % 10 == 0):
        correct_stop = correct_stop + 1
        total_stop = total_stop + 1
        watch_running = False
    elif watch_running == True and (counter % 10 != 0):
        total_stop = total_stop + 1
        watch_running = False
    else:
        pass
def reset():
    global counter
    global correct_stop
    global total_stop
    counter = 0
    correct_stop = 0
    total_stop = 0
    timer.stop()

# define event handler for timer with 0.1 sec interval
def tick():
    global counter
    counter = counter + 1

# define draw handler

def draw_handler(canvas):
    """Draw timer as text."""
    canvas.draw_text(format(counter), [150, 200], 50, "Red")
    canvas.draw_text(str(correct_stop) + '/' + str(total_stop), [350, 50], 20, 'Red')
    
# create frame

frame = simplegui.create_frame("Start", 400, 400)
timer = simplegui.create_timer(100, tick)

frame.add_button('Start', start, 100)
frame.add_button('Stop', stop, 100)
frame.add_button('Reset', reset, 100)

# register event handlers
frame.set_draw_handler(draw_handler)

# start frame
frame.start()


# Please remember to review the grading rubric
