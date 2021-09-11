# football hurdle

def turn_right():
    turn_left()
    turn_left()
    turn_left()

def jump():
    turn_left()         
    if not at_goal():
        while  wall_on_right() :
            if wall_in_front():
                turn_left()
            else:
                move()    
        
    while right_is_clear():
        turn_right()
        move()    

while not at_goal():
    while wall_in_front():
        jump()
        
    move()
    
    

