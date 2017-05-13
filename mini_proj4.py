# Implementation of classic arcade game Pong

import simplegui
import random

# initialize globals - pos and vel encode vertical info for paddles
WIDTH = 600
HEIGHT = 400       
BALL_RADIUS = 20
PAD_WIDTH = 8
PAD_HEIGHT = 80
HALF_PAD_WIDTH = PAD_WIDTH / 2
HALF_PAD_HEIGHT = PAD_HEIGHT / 2
LEFT = False
RIGHT = True
paddle1_pos = [(HEIGHT / 2) + HALF_PAD_HEIGHT, (HEIGHT / 2) - HALF_PAD_HEIGHT]
paddle2_pos = [(HEIGHT / 2) + HALF_PAD_HEIGHT, (HEIGHT / 2) - HALF_PAD_HEIGHT]
paddle1_vel = 0
paddle2_vel = 0
score1 = 0
score2 = 0


# initialize ball_pos and ball_vel for new bal in middle of table
# if direction is RIGHT, the ball's velocity is upper right, else upper left
def spawn_ball(direction):
    global ball_pos, ball_vel # these are vectors stored as lists
    ball_pos = [WIDTH / 2, HEIGHT / 2]
    ball_vel = [0, 0]
    if direction == RIGHT:
        ball_vel[0] = random.randrange(120, 240)
        ball_vel[1] = -random.randrange(60, 180)
    elif direction == LEFT:
        ball_vel[0] = -random.randrange(120, 240)
        ball_vel[1] = -random.randrange(60, 180)
# define event handlers
def new_game():
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel  # these are numbers
    global score1, score2  # these are ints
    score1 = 0
    score2 = 0
    spawn_ball(RIGHT)
    
def draw(canvas):
    global score1, score2, paddle1_pos, paddle2_pos, ball_pos, ball_vel
    global paddle1_vel, paddle2_vel

      
    # draw mid line and gutters
    canvas.draw_line([WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 1, "White")
    canvas.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1, "White")
    canvas.draw_line([WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1, "White")
        
    # update ball
    # verticle collision
    if HEIGHT - BALL_RADIUS <= ball_pos[1]:
        ball_vel[1] = -ball_vel[1]
    elif BALL_RADIUS >= ball_pos[1]:
        ball_vel[1] = -ball_vel[1]
        
    #horizontal collision
    #if ball vert position between paddle end points and horiz touching gutter 
    #reflect ball
    in_gutter_left = PAD_WIDTH + BALL_RADIUS >= ball_pos[0]
    in_gutter_right = WIDTH - PAD_WIDTH - BALL_RADIUS <= ball_pos[0]
    touch_left_paddle = ball_pos[1] >= paddle1_pos[1] and ball_pos[1] <= paddle1_pos[0]
    touch_right_paddle = ball_pos[1] >= paddle2_pos[1] and ball_pos[1] <= paddle2_pos[0]
    if (in_gutter_left and touch_left_paddle) or (in_gutter_right and touch_right_paddle):
        ball_vel[0] = -(ball_vel[0] + .1*ball_vel[0])
        ball_vel[1] = ball_vel[1] + .1*ball_vel[1]
    elif WIDTH - PAD_WIDTH - BALL_RADIUS < ball_pos[0]:
        score1 = score1 + 1
        spawn_ball(LEFT)
    elif PAD_WIDTH + BALL_RADIUS > ball_pos[0]:
        score2 = score2 + 1
        spawn_ball(RIGHT)     
    
    
    ball_pos[0] = ball_pos[0] + (ball_vel[0]/100.0)
    ball_pos[1] = ball_pos[1] + (ball_vel[1]/100.0)
    # draw ball
    canvas.draw_circle(ball_pos, BALL_RADIUS, 1, "White", "White")
    # update paddle's vertical position, keep paddle on the screen
    if paddle1_pos[1] == 0 and paddle1_vel == 2:
        paddle1_pos[0] = paddle1_pos[0]
        paddle1_pos[1] == paddle1_pos[1]
    elif paddle1_pos[0] == HEIGHT and paddle1_vel == -2:
        paddle1_pos[0] = paddle1_pos[0]
        paddle1_pos[1] == paddle1_pos[1]
    else:    
        paddle1_pos[0] = paddle1_pos[0] - paddle1_vel        
        paddle1_pos[1] = paddle1_pos[1] - paddle1_vel 
    if paddle2_pos[1] == 0 and paddle2_vel == 2:
        paddle2_pos[0] = paddle2_pos[0]
        paddle2_pos[1] = paddle2_pos[1]
    elif paddle2_pos[0] == HEIGHT and paddle2_vel == -2: 
        paddle2_pos[0] = paddle2_pos[0]
        paddle2_pos[1] = paddle2_pos[1]
    else:    
        paddle2_pos[0] = paddle2_pos[0] - paddle2_vel
        paddle2_pos[1] = paddle2_pos[1] - paddle2_vel
    # draw paddles
    canvas.draw_line([PAD_WIDTH / 2, paddle1_pos[0]], 
                     [PAD_WIDTH / 2, paddle1_pos[1]], 
                     PAD_WIDTH,'White')
    canvas.draw_line([WIDTH - (PAD_WIDTH /2),paddle2_pos[0]], 
                     [WIDTH - (PAD_WIDTH /2),paddle2_pos[1]], 
                     PAD_WIDTH,'White')  
    
    # draw scores
    canvas.draw_text(str(score1) + ' | ' + str(score2),[275, 30], 30, 'White')    
def keydown(key):
    global paddle1_vel, paddle2_vel
    if key == simplegui.KEY_MAP["up"]:
        paddle2_vel =  2
    elif key == simplegui.KEY_MAP["down"]:
        paddle2_vel =  -2    
    elif key == simplegui.KEY_MAP["w"]:
        paddle1_vel = 2
    elif key == simplegui.KEY_MAP["s"]:
        paddle1_vel = -2
        
def keyup(key):
    global paddle1_vel, paddle2_vel
    if key == simplegui.KEY_MAP["up"]:
        paddle2_vel =  0
    elif key == simplegui.KEY_MAP["down"]:
        paddle2_vel =  0
    elif key == simplegui.KEY_MAP["w"]:
        paddle1_vel = 0
    elif key == simplegui.KEY_MAP["s"]:
        paddle1_vel = 0

# create frame
frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)
frame.add_button('reset', new_game)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)


# start frame
new_game()
frame.start()
