# Add your Python code here. E.g.
import microbit, random
from random import randint

FALLING_INTERVAL = 1000
OBJ_SPAWNS_PER = 1
PLAYER_BRIGHTNESS = 8
OBJ_BRIGHTNESS = 4

#player position x,y. y is constant
p_position = [2,4]

#set timers
#nextSpawnTime = microbit.running_time()+1000
nextMoveTime = microbit.running_time()+FALLING_INTERVAL

f_objects = []

while True:
    updateDisplay = False
    
    #player movements
    if microbit.button_a.was_pressed() and p_position[0] != 0:
        p_position[0]-=1
        updateDisplay = True
        
    elif microbit.button_b.was_pressed() and p_position[0] != 4:
        p_position[0]+=1
        updateDisplay = True

    #object falling
    if microbit.running_time() >= nextMoveTime:
        
        objs_to_remove = []
        for f_obj in f_objects:
            if f_obj[1] < 4:
                f_obj[1]+=1
            else:
                #f_objects.remove(f_obj)
                objs_to_remove.append(f_obj)
        
        for f_obj in objs_to_remove:
            f_objects.remove(f_obj)
        
        #object spawning
        for i in range(0, OBJ_SPAWNS_PER):
            f_objects.append([randint(0,4),0])
        updateDisplay = True
        nextMoveTime = microbit.running_time()+FALLING_INTERVAL
    
    #collision detection
    
    
    #update display
    if updateDisplay:
        microbit.display.clear()
        
        #object positions
        for f_obj in f_objects:
            microbit.display.set_pixel(f_obj[0], f_obj[1], OBJ_BRIGHTNESS)
        #player position
        microbit.display.set_pixel(p_position[0], p_position[1], PLAYER_BRIGHTNESS)
