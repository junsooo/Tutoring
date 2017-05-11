function turn_right() {
	turn_left()
	turn_left()
	turn_left()
}

function move_one_stair() {
	pick_beeper()
	turn_right()
	move()
	turn_left()
	move()
}

function one_turn(n){
	for(i=0;i<4;i++)
	{	
	for(j=0;j<n;j++)
		move_one_stair()
	turn_left()
	}
	move()
	move()	
}
//Code starts
for(i=0;i<5;i++)
	move()
turn_left()
move()
	
one_turn(5)
one_turn(3)
one_turn(1)
