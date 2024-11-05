# global variables for rain, lightning and snow
rain_drops = []
num_drops = 100  # number of raindrops
rain_button = None
rain_active = False
lightning_button = None
lightning_active = False
lightning_bolts = []
num_lightning = 5  # number of lightning bolts
snow_flakes = []
num_flakes = 500 # number of snowflakes
snow_button = None
snow_active = False

def setup():
    global rain_button, lightning_button, snow_button
    size(1270, 630) #size of canvas
    
    # setups
    setup_rain()
    setup_lightning()
    setup_snow()
    
    # initialize custom buttons (x, y, width, height): of button. all placed on the left side of the screen
    rain_button = CustomButton(75, 130, 50, 50, "rain")  # rain button
    lightning_button = CustomButton(28, 85, 60, 60, "lightning")  # lightning button
    snow_button = CustomButton(90, 310, 55, 55, "snow") # snow button
    
    
def draw():
    if rain_active:
        background(98, 140, 180) 
    # if rain active, change the background to a gloomier colour
   
    elif lightning_active:
        background(0) 
    # if lightning is active, change the background to black
   
    elif snow_active:
        background(138, 203, 232)
    # if snow active, change the background to a light blue colour
   
    else:
        background(60, 175, 227) 
    # when no buttons are activated keep the normal sky colour
    
    # Draw all the static elements
    draw_static_elements()
    
    # Display the buttons
    rain_button.display()
    lightning_button.display()
    snow_button.display()
    
    # if rain is active, update and display rain
    if rain_button.pressed:
        update_and_display_rain()
    if snow_button.pressed:
        update_and_display_snow()
    
    # text above buttons on the left side of the screen
    s = "Click a button\nto change the weather!" 
    # \n puts the text in two seperate lines
    fill(0)
    textSize(16)
    textAlign(CENTER, TOP) # text is centered and placed at the top left of the page
    text(s, -45, 55, 280, 320)

def draw_static_elements():
# grass
    fill(85, 206, 106) # green colour
    stroke (85, 206, 106)
    strokeWeight(8)
    rect(0, 500, 1270, 130);

# for the house colours 
    stroke (178,163,142) # outline colour (darker beige)
    strokeWeight(8)
    fill(206,189,162) # fill colour (lighter beige)

# draw a square in the centre of the canvas
    square(550, 300, 220);

# windows
    square(570, 320, 40);
    line(570, 340, 610, 340)
    line(590, 320, 590, 360)

    square(710, 320, 40);
    line(710, 340, 750, 340)
    line(730, 320, 730, 360)

#for the door
    line(620, 520, 620, 380);
    line(700, 520, 700, 380);
    line(620, 380, 700, 380)
    circle(685, 446, 5);

#draw a triangle directly on top of the square for the roof
    triangle(554, 300, 660, 173, 765, 300);
    strokeWeight (8)
    fill (178,163,142)

#bushes
    fill(55, 170, 75)
    stroke (55, 170, 75)
    strokeWeight(8)
    circle(480, 510, 20);
    circle(500, 510, 20);
    circle(520, 510, 20);
    circle(510, 490, 20);
    circle(490, 490, 20);
    
    circle(780, 510, 20);
    circle(800, 510, 20);
    circle(820, 510, 20);
    circle(790, 490, 20);
    circle(810, 490, 20);
    
# tree branch
    fill(121, 69, 20)
    stroke (121, 69, 20)
    strokeWeight(8)
    rect(450, 290, 20, 230);
    
    #leaves
    fill(55, 170, 75)
    stroke (55, 170, 75)
    strokeWeight(8)
    circle(425, 305, 35);
    circle(450, 305, 35);
    circle(470, 305, 35);
    circle(500, 305, 35);
    circle(440, 280, 35);
    circle(460, 280, 35);
    circle(480, 280, 35);
    circle(430, 270, 35);
    circle(460, 270, 35);
    circle(490, 270, 35);
    circle(475, 255, 35);
    circle(445, 255, 35);
    circle(460, 245, 35);
    circle(425, 285, 35);
    circle(495, 285, 35);
    
# car
    car_x = 960 # x position of car
    car_y = 500 # y position of car
    
    # main car body
    fill(255, 0, 0)  # red 
    stroke (0)
    strokeWeight(2)
    arc(car_x, car_y, 200, 200, PI, TWO_PI, CHORD) # semi-circle

    # wheels
    fill(0)  # black
    stroke (0)
    strokeWeight(2)
    ellipse(car_x - 60, car_y, 50, 50)
    ellipse(car_x + 60, car_y, 50, 50)
    
    # insides of wheels
    fill(90, 90, 90)  # grey 
    stroke (90, 90, 90)
    ellipse(car_x - 60, car_y, 20, 20)
    ellipse(car_x + 60, car_y, 20, 20)
    
    # window
    fill(200, 200, 255)  # light blue
    stroke (0)
    arc(car_x, car_y, 180, 180, PI+QUARTER_PI/2, TWO_PI-QUARTER_PI/2, CHORD)
    

# snow setup
def setup_snow():
    global snow_flakes
    for i in range(num_flakes):
        snow_flakes.append(create_flake())

def create_flake(): # create random sized flakes at a random speed
    return {
        'x': random(width),
        'y': random(-50, -10),
        'size': random(2, 5),
        'speed': random(1, 3)
    }

def update_and_display_snow():
    for flake in snow_flakes:
        # update flake position
        flake['y'] += flake['speed']
        
        # horizontal movement
        flake['x'] += random(-0.5, 0.5)
        
        # reset flake if it's off-screen
        if flake['y'] > height:
            flake.update(create_flake())
        
        # display the snowflake
        fill(255)  # white color for snow
        noStroke()
        ellipse(flake['x'], flake['y'], flake['size'], flake['size'])
        
        
# rain set-up
def setup_rain():
    global rain_drops
    rain_drops = []
    for i in range(num_drops):
        rain_drops.append(create_drop())

def create_drop(): # create random sized raindrops at a random speed
    return {
        'x': random(width),
        'y': random(-500, -50),
        'z': random(0, 20),
        'length': map(random(0, 20), 0, 20, 10, 20),
        'speed': map(random(0, 20), 0, 20, 4, 10)
    }

def update_and_display_rain():
    for drop in rain_drops:
        # update drop position
        drop['y'] += drop['speed']
        
        # reset drop if it's off-screen
        if drop['y'] > height:
            drop.update(create_drop())
        
        # display the raindrop
        stroke(120, 208, 247)  # color of rain
        strokeWeight(map(drop['z'], 0, 20, 1, 3))
        line(drop['x'], drop['y'], drop['x'], drop['y'] + drop['length'])

class CustomButton:
    def __init__(self, x, y, w, h, button_type):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.pressed = False
        self.button_type = button_type
    
    def display(self):
        pushMatrix()
        translate(self.x, self.y)
        
        if self.button_type == "rain":
            # rain button display code
            fill(120, 208, 247)
            stroke(120, 208, 247)
            strokeWeight(5)
            circle(0, 20, 5)
            triangle(-0.5, 15, 0.5, 12, 1, 15)
            circle(30, 20, 5)
            triangle(29.5, 15, 30.5, 12, 31, 15)
            circle(15, 0, 5)
            triangle(14.5, -5, 15.5, -8, 16, -5)
       
        elif self.button_type == "lightning":
            # lightning button display code
            if self.pressed:
                fill(255, 165, 0) # darker yellow when button is pressed
                stroke(255, 165, 0)
            else:
                fill(242, 207, 29) # normal yellow when button is not pressed
                stroke(242, 207, 29)
            strokeWeight(5)
            scale(0.7)  # scale of lightning bolt
            beginShape()
            vertex(80, 170)
            vertex(110, 170)
            vertex(90, 190)
            vertex(110, 190)
            vertex(80, 230)
            vertex(85, 205)
            vertex(70, 205)
            vertex(80, 170)
            endShape(CLOSE)
            
        elif self.button_type == "snow":
            # snow button display
            if self.pressed:
                fill(60, 175, 227)  # light blue when pressed
                stroke(60, 175, 227)
            else:
                fill(255, 255, 255)  # white when not pressed
                stroke(255, 255, 255)
            strokeWeight(2)
            scale(1.3)  # scale of snowflake
            for i in range(8):
                pushMatrix()
                rotate(TWO_PI * i / 8)
                self.draw_branch()
                popMatrix()
        
        popMatrix()
    
    def draw_branch(self): # snowflake shape
        branch_length = 15
        line(0, 0, branch_length, 0)
      
        for i in range(2):
            pushMatrix()
            translate(branch_length * (0.4 + i * 0.3), 0)
            rotate(PI / 4)
            line(0, 0, branch_length * 0.3, 0)
            rotate(-PI / 2)
            line(0, 0, branch_length * 0.3, 0)
            popMatrix()
    
    def check_click(self, mx, my):
        if (mx > self.x and mx < self.x + self.w and 
            my > self.y and my < self.y + self.h):
            self.pressed = not self.pressed
            return True
        return False

# lightning set-up
def setup_lightning():
    global lightning_bolts
    lightning_bolts = []
    for _ in range(num_lightning):
        lightning_bolts.append(create_lightning_bolt())

def create_lightning_bolt(): # create random lengths and branches of lightning
    return {
        'x': random(width),
        'y': 0,
        'length': random(50, 150),
        'branch': random(1, 3)  # number of branches
    }


def setup_lightning():
    global lightning_bolts
    lightning_bolts = []

def update_and_display_lightning():
    # clear old bolts that have gone off-screen
    lightning_bolts[:] = [bolt for bolt in lightning_bolts if bolt['y'] < height]
    
    # add new bolts when lightning is active
    if random(1) < 0.05:  # probability for how often lightning strikes
        lightning_bolts.append(create_lightning_bolt())
    
    for bolt in lightning_bolts:
        bolt['y'] += random(5, 15)  # lightning bolts fall over time
        draw_lightning_bolt(bolt)

def draw_lightning_bolt(bolt):
    stroke(255, 255, 0)
    strokeWeight(3)
    
    # create a jagged lines for the lightning bolt
    x = bolt['x']
    y = bolt['y']
    length = bolt['length']
    
    # randomise the x positions to create a jagged effect
    for i in range(int(length / 10)):
        next_x = x + random(-10, 10)  # randomise for jagged effect
        next_y = y + (length / (length / 10)) * i
        line(x, next_y, next_x, next_y)
        x = next_x

def mousePressed(): # what is printed when buttons are active and not active 
    global rain_active, lightning_active, snow_active
    if rain_button.check_click(mouseX, mouseY):
        rain_active = not rain_active
        print("Rain:", "On" if rain_active else "Off")
    elif lightning_button.check_click(mouseX, mouseY):
        lightning_button.pressed = not lightning_button.pressed
        lightning_active = lightning_button.pressed
        print("Lightning:", "On" if lightning_active else "Off")
    elif snow_button.check_click(mouseX, mouseY):
        snow_active = not snow_active
        print("Snow:", "On" if snow_active else "Off")
