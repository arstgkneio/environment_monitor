import turtle
import random
import time
import math


class Habitat:
    '''
        Class Habitat:
        Create the main window with a title. Draw a rectangular border
    '''

    screen_tracing = 0
    border_pen = ''
    wn = ''

    def __init__(self, title, side, bg_colour='black', line_colour='white', line_width=3):
        self.title = title
        self.side_length = side     #lenght of habitat's side
        self.bg_colour = bg_colour
        self.line_colour = line_colour
        self.line_width = line_width

    def create(self):
        self.wn = turtle.Screen()
        self.wn.title(self.title)
        self.wn.bgcolor(self.bg_colour)
        self.wn.tracer(self.screen_tracing)

        border_pen = Pen(self.line_colour, self.line_width, pendown=True, hidden=True)

        bp = border_pen.create()


        bp.penup()
        bp.goto(-(self.side_length/2), -(self.side_length/2))
        bp.pendown()
        
        for side in range(4):
            bp.fd(self.side_length)
            bp.lt(90)
        
    def update_scrn(self):
            self.wn.update()


class PersonalSpace:
    '''
        Class PersonalSpace:
        Determine parameters of the personal sqare space for each individual
    '''

    line_width = 0
    border_colour='green'

    def __init__(self, habitat, side):
        self.habitat = habitat
        self.side_length = side

        #Create random x and y for the personal space centre
        self.cntr_x = random.randint(-((habitat.side_length/2)-self.side_length/2),((habitat.side_length/2)-self.side_length/2))
        self.cntr_y = random.randint(-((habitat.side_length/2)-self.side_length/2),((habitat.side_length/2)-self.side_length/2))

    def draw(self):
        '''Function to draw border of the personal space'''
        border_pen = Pen(self.border_colour, self.line_width, pendown=True, hidden=True)
        bp = border_pen.create()

        bp.penup()
        bp.goto((self.cntr_x - self.side_length/2), (self.cntr_y - self.side_length/2))

        bp.pendown()

        for side in range(4):
            bp.fd(self.side_length)
            bp.lt(90)
            


class Individual:
    '''
        Class Individual:
        Create an individual according with the specified parameters
    '''

    size = 0.3
    line_width = 1
    max_delta = 4
    steps_before_changing_direction = 0
    step_count = 0
    straight_steps_min = 10
    min_safe_distance = 10
    shape='circle'
    colour='white'
    tracking=False


    def __init__(self, habitat, space_width, show_border=False, infected=False):
        self.habitat = habitat
        self.is_infected = infected
        self.space_width = space_width
        self.show_border = show_border
        self.straight_steps_max = space_width/3

        if(self.straight_steps_max <= self.straight_steps_min):
            self.straight_steps_max = self.straight_steps_min

        self.p_space = PersonalSpace(self.habitat, self.space_width)
        
        if(self.show_border):
            self.p_space.draw()

        individual_pen = Pen(self.colour, self.line_width, pendown=self.tracking, hidden=False)
        self.ip = individual_pen.create()

        self.ip.shape(self.shape)
        self.ip.shapesize(self.size)

        self.x = random.randint((self.p_space.cntr_x - self.space_width/2),(self.p_space.cntr_x + self.space_width/2))
        self.y = random.randint((self.p_space.cntr_y - self.space_width/2),(self.p_space.cntr_y + self.space_width/2))
        self.ip.penup()
        self.ip.goto(self.x, self.y)

    def move(self):
        '''Function to update position of an individual.
        Also set the individual's colour accourding to the individual's health status'''
        
        if(self.step_count > self.steps_before_changing_direction or self.step_count == 0):
            self.steps_before_changing_direction = random.randint(self.straight_steps_min,int(self.straight_steps_max))

            self.reset_step_count()
            self.set_speed_vector()

        self.new_x = self.x + self.delta_x
        self.new_y = self.y + self.delta_y


        if((self.new_x > self.p_space.cntr_x + self.space_width/2) or (self.new_x < self.p_space.cntr_x - self.space_width/2)):
            self.new_x = self.x
            self.set_speed_vector()

        if((self.new_y > self.p_space.cntr_y + self.space_width/2) or (self.new_y < self.p_space.cntr_y - self.space_width/2)):
            self.new_y = self.y
            self.set_speed_vector()

        if(self.is_infected):
            self.ip.color('red')
        else:
            self.ip.color('white')

        if(self.tracking):
            self.ip.pendown()
        else:
            self.ip.penup()

        self.ip.goto(self.new_x, self.new_y)
        self.x = self.new_x
        self.y = self.new_y

        self.increment_step_count()

    def increment_step_count(self):
        self.step_count = self.step_count + 1 

    def reset_step_count(self):
        self.step_count = 0

    def set_speed_vector(self):
        '''Function to generate random values for delta_x and delta_y'''
        
        self.delta_x = random.randint(-self.max_delta, self.max_delta)
        self.delta_y = random.randint(-self.max_delta, self.max_delta)

    def is_too_close(self, someone):
        '''Function to check if the individual is close enough to another individual to catch virus'''
        
        distance = math.sqrt((self.x - someone.x)**2 + (self.y - someone.y)**2)
        if(distance < self.min_safe_distance):
            return True

    def check_if_avoided(self, potential_virus_carriers):
        '''Function to check if the individual caught the virus when comming too close to another individual'''
        for another_individual in potential_virus_carriers:
            
            if(self.is_too_close(another_individual)):
               self.is_infected = another_individual.is_infected
               break

class Pen:
    '''
        Class Pen:
        Set parameters for a pen (turtle) used to render items that use the pen,
        e.g Habitat and Individual.
    '''

    speed = 0

    def __init__(self, colour, size, pendown=False, hidden=False):
        self.colour = colour
        self.size = size
        self.is_down = pendown
        self.is_hidden = hidden
        

    def create(self):
        '''Function to create a pen (turtle) with specified parameters'''
        pen = turtle.Turtle()
        pen.pensize(self.size)
        pen.color(self.colour)
        pen.speed(self.speed)

        if(self.is_down):
            pen.pendown()
        else:
            pen.penup()
        
        if(self.is_hidden):
            pen.hideturtle()
        else:
            pen.showturtle()

        return pen
    



'''
    Main:
    Instatiate Habitat and list of individuals.
    Run a loop to upate location and infected status of individuals.
'''


#Create Habitat
habitat = Habitat('Virus Simulator', 600)
habitat.create()


#Create populate habitat with individuals

tracking = False #whether or not to plot individuals' tracks


individuals = []


#Create the first infected individual
infected_individual = Individual(habitat, space_width=100, show_border=False, infected=True)
infected_individual.tracking = tracking
individuals.append(infected_individual)

#Create initially uninfected individuals
for i in range(50): #number of individuals
    individual = Individual(habitat, space_width=100, show_border=False)
    individual.tracking=tracking
    
    individuals.append(individual)


#Set simulator in motion
for step in range(1000):    #number of total update cycles

    infections_detected=0
        
    for i in range(len(individuals)):
        ind = individuals[i]
        ind.move()

        if(not ind.is_infected):

            rest_inds = individuals[:]
            del(rest_inds[i])
            ind.check_if_avoided(rest_inds)

        else:
            infections_detected+=1

    print(infections_detected)

    habitat.update_scrn()
    time.sleep(0.001) #use this sleep to control the screen update rate






