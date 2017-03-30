// 새로운 명령어를 만드는 공간
num=0
size_check=1

change_speed(0)
// 명령어를 실행하는 공간


function drop_beepers(){
    repeat('put_beeper()',num)
    num+=1
}
    
function drop_and_move(){
    drop_beepers()
    move()
}
function home(){
    while(!direction_is_north())
        turn_left()
    turn_left()
    while(front_is_clear())
        move()
    turn_left()
    while(front_is_clear())
        move()
    turn_left()
    }
    
function row_check(){
    row1 = 0
    while(front_is_clear())
    {
        move()
        row1+=1
    }
    home()
    return row1
    }

function column_check(){
    column1=0
    turn_left()
    while(front_is_clear())
    {
        move()
        column1+=1
    }
    home()
    return column1
    }

function first_turn(row,column){
    drop_beepers()
    repeat('drop_and_move()',row)
    turn_left()
    repeat('drop_and_move()',column)
    turn_left()
    repeat('drop_and_move()',row)
    turn_left()
}
function half_turn(row,column){
    repeat('drop_and_move()',column-size_check)
    turn_left()
    repeat('drop_and_move()',row-size_check)
    turn_left()
    size_check+=1
}
    
//check size of map
row = row_check()
column = column_check()


first_turn(row,column)

while(!on_beeper())
{
    if(column==size_check)
        break
    half_turn(row,column)
}
drop_beepers()