# Michael Somkuti 
# Source:  https://www.youtube.com/watch?v=KkyIDI6rQJI
# Fading: https://forum.processing.org/two/discussion/13189/a-better-way-to-fade

# CHANGE COLORS
# EDIT WINDOW PANE COLOR

import time 
from Drop import Drop  # Import our class
# from night_sky import drawGradient

def setup():
    global bg_color, drops, flash, flash_count, foreground, old_time, start_time
    size(1920, 1080)  # Window size
    
    # IMPLEMENTATION OF CANVAS IN PROGRESS
    # canvas  = createGraphics(width, height)  # LEARN MORE
    
    drops = [None] * 1000  # Preallocate array of rain drops
    for i in range(len(drops)):
        drops[i] = Drop()  # Create array of rain drops
    
    start_time = time.time()  # Acquire time, will control frequency of thunder clap
    old_time = 0  # Track every time step for thunder animation

    flash = 0  # Keep track on whether thunder animation is in progress
    flash_count = 0  # Track num frames passed during animation

    foreground = loadImage("foreground.png")  # Set foreground image
    foreground.resize(1920,1080)
    
    bg_color = color(17, 35, 41)  # Background color
    
    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # GRADIENT STUFF SETUP
    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    global num_frames
    num_frames = int(60*20)


def draw():
    global thun_old, flash_count, flash, old_time, num_frames
    background(bg_color)  # Draw our background
    
    
    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # GRADIENT STUFF COMING SOON^TM
    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    
    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # Rain falling
    for i in range(len(drops)):  # Makes our drops start falling and draws them to the canvas
        drops[i].fall()
        drops[i].show()
    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # Thunder flashes every x amount of seconds
    pos_thun = time.time()
    new_time = int(pos_thun - start_time)
    
    # RAINDROPS SLOW DOWN DURING THUNDER
    
    # Check how much time has passed
    if ( new_time % 14 == 0 and old_time != new_time):  # This thunders every 5 seconds # MAKE THIS FLASH CORRECTLY
        flash = 1  # Thunderclap has begun
        old_time = new_time  # Increment our time step
    #print(flash_count)
    # If thunder has begun
    if (flash == 1):
        flash_count += 1  # Count num frames drawn during thunder
        fade_in =  50 + flash_count  # Initial flash of lightning is always brighter than second
        fade_out = 60 - int(flash_count * 1.12) # * 1.03) # Second flash of lightning leads to fade out  # Change opacity, MAKE THIS SMOOTHER
    
        if flash_count < 10:
            fill(255, 250, 205, fade_in)
        else:
            fill(255, 250, 205, fade_out)
            #stroke(230, 230, 250)   
        
        rect(0,0, width, height)
                    
        if (fade_out < 0 ):
            flash_count = 0
            flash = 0
            fade_in = 0
            fade_out = 0
    
    image(foreground, 0,0)
     
    #if frameCount <= num_frames:
    #    saveFrame('image-%s.gif' %frameCount)
    
    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

           
# # FUNCTION CREATION IN PROGRESS    
# def fadeGraphics(PGraphics c, int fadeAmount):
#     c.beginDraw()  # LEARN WHAT HAPPENS IN THIS FUNCTION
#     c.loadPixels()
    
#     for i in range(0, c.pixels.length):  # GET ALPHA VALUE
#         alpha = (c.pixels[i] >> 24) & 0xFF  # WHAT THIS
        
#         alpha = max(0, alpha - fadeAmount)
#         c.pixels[i] = (alpha << 24 or c.pixels[i]) & 0xFFFFFF 
        
#     canvas.updatePixels()
#     canvas.endDraw()        
        
