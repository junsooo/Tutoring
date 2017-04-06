change_speed(0)

//알고리즘의 핵심: 끝까지 가서 왼쪽이 비어있는지 확인하고, 비어있으면 돌아서 한줄 쭉 간다음에 다시 오른쪽 비어있는지 확인하는 과정을 반복
//그래서 가로 10 * 세로 홀수 맵도 가능함
check = 0

function turn_right(){
    turn_left()
    turn_left()
    turn_left()
	}

function move_and_drop(){
    move()
    check+=1
    if(check%2==1)
        put_beeper()
}

if(!front_is_clear())
    turn_left()


while(front_is_clear()){
    
    while(front_is_clear())
        move_and_drop()
    if(left_is_clear())
    {	turn_left()
        move_and_drop()
        turn_left()
        while(front_is_clear())
            move_and_drop()
        if(right_is_clear())
        {    turn_right()
            move_and_drop()
            turn_right()
		}
	}
}
