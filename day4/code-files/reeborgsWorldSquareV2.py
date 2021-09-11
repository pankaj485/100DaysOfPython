
# football hurdle

def turn_right():
    turn_left()
    turn_left()
    turn_left()

def jump_forward():
    # move one step and go up
    move()
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
        jump_forward()
    


    
    
    
    
