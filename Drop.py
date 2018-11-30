from random import randint
import time

# Look into what map does, I think it changes the value in the second range based upon where 
# z falls in the first range

# Expand upon this by making drops splash at the bottom, adding thunder effects (ALMOST DONE!), 
# Improve 3d effects by more drops in back than front
# Smaller drops should fall slower
# Rain drops are at terminal velocity (DONE)
# Add gusts of wind


class Drop:
    x=0
    y=0
    yspeed=0
    drop_color = color(98, 98, 130)
    
    def __init__(self):
        self.x = random(width)
        y = random(-500, 0)  # Starts beyond screen randomly
        self.y = y
        self.z = random(0, 20)
        self.len = map(self.z, 0, 30, 10, 20)  # Mapping speed between 0,20 and len 10,20
        # longer if closer, shorter if further
        
        self.yspeed = map(self.z, 0, 20, 2, 40)  # falling speed of drop, faster when closer, originally: map(self.z, 0, 20, 10, 20)
        self.len = random(10, 20)
        
        # ADD DRIP MECHANIC
   
    def fall(self):
        self.y = self.y + self.yspeed  # Make the rain fall
        # self.grav = map(self.z, 0, 20, 0, 0.2)
        # self.yspeed = self.yspeed # + self.grav  # Add the sense of gravity by increasing speed
        
        if (self.y > height):  # reset our drops when they go out of frame
            self.y = random(-500, 0)
            # self.yspeed = map(self.z, 0, 20, 10, 20) # Reset our speed
            
    def show(self):
        thick = map(self.z, 0, 20, 1, 3)  # Closer it is, thicker drop is
        strokeWeight(thick)  # Set thickness of drop
        stroke(self.drop_color)
        line(self.x, self.y, self.x, self.y + self.len)  # Rain drop starts at a point (x,y) and ends at (x,y+10)
    
       
