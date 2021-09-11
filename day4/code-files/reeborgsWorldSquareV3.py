
# football hurdle

def turn_right():
    turn_left()
    turn_left()
    turn_left()

def jump_forward():
    # move one step and go up
    turn_left()
    move()
    # move one step right
    turn_right()
    move()
    # go down 
    turn_right()
    move()
    # turn to initial position    
    turn_left()    
    
while not at_goal():
    if front_is_clear():
        move()
    if wall_in_front(): 
        jump_forward()
    

# front_is_clear()
# wall_in_front()
# at_goal()
    
    
    
    
