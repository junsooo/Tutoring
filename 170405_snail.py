# DO NOT CHANGE "cs1robots2" MODULE NAME
from cs1robots2 import *

# You can change the size of world for testing your code
create_world(avenues=6, streets=6)

# You can change your Robot's name
hubo = Robot(beepers=100000)
hubo.set_trace('blue')
j=1

num=1

def drop_beepers():
    global num
    for i in range(num):
        hubo.drop_beeper()
    num+=1
    
def drop_and_move():
    drop_beepers()
    hubo.move()

def home():
    while not hubo.facing_north():
        hubo.turn_left()
    hubo.turn_left()
    while hubo.front_is_clear():
        hubo.move()
    hubo.turn_left()
    while hubo.front_is_clear():
        hubo.move()
    hubo.turn_left()
    
def map_check():
    row1 = 0
    column1 = 0
    while hubo.front_is_clear():
        hubo.move()
        row1+=1
    hubo.turn_left()
    while hubo.front_is_clear():
        hubo.move()
        column1+=1
    home()
    return row1,column1
    
#row -> garo 
row, column  = map_check()

beeper_num=1
#avenue=5
#street=5
drop_beepers()
for i in range(row):
    drop_and_move()
hubo.turn_left()
for i in range(column):
    drop_and_move()
hubo.turn_left()
for i in range(row):
    drop_and_move()
hubo.turn_left()

while not hubo.on_beeper():
    if column-j==0:
        break
    for i in range(column-j):
        drop_and_move()
    hubo.turn_left()
    for i in range(row-j):
        drop_and_move()
    hubo.turn_left()
    j+=1
drop_beepers()
"""
avenue_flag = 0 #Check avenue == 1
street_flag = 0 #Check street == 1

def drop_beepers(n):
    global num
    for i in range(n):
        hubo.drop_beeper()
    num+=1
def turn_right():
    hubo.turn_left()
    hubo.turn_left()
    hubo.turn_left()

def turn_around():
    hubo.turn_left()
    hubo.turn_left()
    
def move_one_line_and_turn():
    while hubo.front_is_clear() and (not hubo.on_beeper()):
        drop_beepers(num)
        hubo.move()
    turn_around()
    hubo.move()
    turn_right()
    hubo.move()

def first_one_line_and_turn():    
    while hubo.front_is_clear() and (not hubo.on_beeper()):
        drop_beepers(num)
        hubo.move()
    hubo.turn_left()
# Implement Here

if not hubo.front_is_clear():
    hubo.turn_left()
    while hubo.front_is_clear():
        drop_beepers(num)
        hubo.move()
    avenue_flag = 1

if not hubo.left_is_clear():    #Street == 1
    while hubo.front_is_clear():
        drop_beepers(num)
        hubo.move()
    street_flag = 1

if avenue_flag == 0 and street_flag == 0 :    
    
    for i in range(3):
        first_one_line_and_turn()

    while not hubo.on_beeper():
        move_one_line_and_turn()

if avenue_flag == 1 and street_flag == 1 :  #Map -> 1*1
    hubo.drop_beeper()
"""
