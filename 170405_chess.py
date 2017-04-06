# DO NOT CHANGE "cs1robots2" MODULE NAME
from cs1robots2 import *

# You can change the size of world for testing your code
create_world(avenues=1, streets=7)

# You can change your Robot's name
hubo = Robot(beepers=100000)

# Implement Here
hubo.set_trace('blue')

check = 0

def turn_right():
    hubo.turn_left()
    hubo.turn_left()
    hubo.turn_left()

def move_and_drop():
    global check
    hubo.move()
    check+=1
    if check%2==1:
        hubo.drop_beeper()

if not hubo.front_is_clear():
    hubo.turn_left()


while hubo.front_is_clear():
    
    while hubo.front_is_clear():
        move_and_drop()
    if hubo.left_is_clear():
        hubo.turn_left()
        move_and_drop()
        hubo.turn_left()
        while hubo.front_is_clear():
            move_and_drop()
        if hubo.right_is_clear():
            turn_right()
            move_and_drop()
            turn_right()
