# DO NOT CHANGE "cs1robots2" MODULE NAME
from cs1robots2 import *

# You can change the size of world for testing your code
create_world(avenues=5, streets=9)

# You can change your Robot's name
hubo = Robot(beepers=100000)
hubo.set_trace('blue')
hubo.set_pause(0.1)
# Implement Here
num=1

def drop_beepers():
    global num
    for i in range(num):
        hubo.drop_beeper()
    num+=1

def drop_and_move():
    drop_beepers()
    hubo.move()
    
def turn_right():
    hubo.turn_left()
    hubo.turn_left()
    hubo.turn_left()

def left_up():
    drop_and_move()
    if hubo.left_is_clear():
        hubo.turn_left()
        hubo.move()
        turn_right()

def right_up():
    drop_and_move()
    if hubo.right_is_clear():
        turn_right()
        hubo.move()
        hubo.turn_left()
        
if hubo.front_is_clear():
    drop_and_move()
    hubo.turn_left()
    
while hubo.front_is_clear():
    while hubo.left_is_clear() and hubo.front_is_clear():
        left_up()
    if hubo.front_is_clear():
        drop_and_move()
    else:
        turn_right()
        drop_and_move()
        hubo.turn_left()
    turn_right()
    while hubo.right_is_clear() and hubo.front_is_clear():
        right_up()
    if hubo.front_is_clear():
        drop_and_move()
        hubo.turn_left()
    else:
        hubo.turn_left()
        if hubo.front_is_clear():
            drop_and_move()
drop_beepers()
