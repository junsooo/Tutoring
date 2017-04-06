change_speed(0)
//알고리즘의 핵심: left_up()과 right_up()을 정의해서 벽에 닿을때까지 이 친구들을 반복함
//1 * n, n * 1 맵을 제외하고 모든 맵에서 가능
num=1

function drop_beepers(){
    for(i=0;i<num;i++)
        put_beeper()
    num+=1
}
function drop_and_move(){
    drop_beepers()
    move()
}
function turn_right(){
    turn_left()
    turn_left()
    turn_left()
}
function left_up(){
    drop_and_move()
    if(left_is_clear())
    {   
	turn_left()
        move()
        turn_right()
    }
}
function right_up(){
    drop_and_move()
    if(right_is_clear())
    {	
	turn_right()
        move()
        turn_left()
    }
}

if(front_is_clear())
{
    drop_and_move()
    turn_left()
}
    
while(front_is_clear())
{    
    while(left_is_clear()&&front_is_clear())
        left_up()
    if(front_is_clear())
        drop_and_move()
    else
    {   
	turn_right()
        drop_and_move()
        turn_left()
    }
    turn_right()
    while(right_is_clear()&&front_is_clear())
	right_up()
    if(front_is_clear())
    {
	drop_and_move()
        turn_left()
    }
    else
    {
        turn_left()
        if(front_is_clear())
            drop_and_move()
    }
}
drop_beepers()
