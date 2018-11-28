# Michael Somkuti 
# Source:  https://www.youtube.com/watch?v=KkyIDI6rQJI
# Fading: https://forum.processing.org/two/discussion/13189/a-better-way-to-fade

import time 
from Drop import Drop  # Import our class

flash_count = 0

def setup():
    size(2000, 1500)  # Window size
    
    # IMPLEMENTATION OF CANVAS IN PROGRESS
    canvas  = createGraphics(width, height)  # LEARN MORE
    
    global drops  
    drops = [None] * 1000  # Preallocate the array of rain drops
    for i in range(len(drops)):
        drops[i] = Drop()  # Create an array of drops
    
    global start_time
    start_time = time.time()
    
    global thun_old  # Keep track of what second the thunder occurs
    thun_old = 0
    
    global flash
    flash = 0
    
    global old_time
    old_time = 0
        
    
def draw():
    global thun_old, flash_count, flash, old_time
    
    background(230, 230, 250)  # Draw our background
    
    for i in range(len(drops)):  # Makes our drops start falling and draws them to the canvas
        drops[i].fall()
        drops[i].show()
    
    
    # WORK IN THE THUNDER!!!
    pos_thun = time.time()
    new_time = int(pos_thun - start_time)
    #print(new_time)
    #print('thun_old')
    #print(thun_old)
    
    # RAINDROPS SLOW DOWN DURING THUNDER
    if ( new_time % 11 == 0 and old_time != new_time):  # This thunders every 5 seconds # MAKE THIS FLASH CORRECTLY
        flash = 1
        old_time = new_time

       
    if (flash == 1):
        flash_count += 1
        #thun_old = 1
        fade_out = 200 - (flash_count * 4) * 1.25  # Change opacity, MAKE THIS SMOOTHER
        #if (flash_count == 8):  # MAKE DOUBLE FLASH BETTER
        #    fade_out = 200
        fill(255, 250, 205, fade_out)
            #stroke(230, 230, 250)   
        rect(0,0, 2000, 1500)
        #print(fade_out)
       # print(flash_count)
            
        if (fade_out < 0):
            #thun_old = 0
            flash_count = 0
            flash = 0
           # print('reset')
       
           
# FUNCTION CREATION IN PROGRESS    
def fadeGraphics(PGraphics c, int fadeAmount):
    c.beginDraw()  # LEARN WHAT HAPPENS IN THIS FUNCTION
    c.loadPixels()
    
    for i in range(0, c.pixels.length):  # GET ALPHA VALUE
        alpha = (c.pixels[i] >> 24) & 0xFF  # WHAT THIS
        
        alpha = max(0, alpha - fadeAmount)
        c.pixels[i] = (alpha << 24 or c.pixels[i]) & 0xFFFFFF 
        
    canvas.updatePixels()
    canvas.endDraw()        
        
