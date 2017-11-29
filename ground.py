'''
Dylan Rice
10-21-16
rock and grass
'''
import pygame, random
from pygame.locals import *

# draw the grass and rocks
def draw(screen):
    # Load grass.gif and rock.gif into variables
    img = pygame.image.load("rock.gif")
    grass = pygame.image.load("grass.gif")
    # Create variables to keep track of where to
    # draw the grass
    x = 0
    y = 0
    
    # Outer loop runs as long as x is 
    # not past the right edge of the screen
    while (x <= 800):
        # Inner loop runs as long as y is 
        # not past the bottom edge of the screen
        while (y <= 600):
            # Draws the grass and increases the y
            screen.blit(grass,(x,y))
            y = (y + 50)

        # Increase the x and reset the y
        y = 0
        x = (x + 50)
        
        
    # Draw 30 rocks in random x and y positions
    '''
    for x in range (0, 30):
        A = random.randint (0, 800)
        B = random.randint (0, 600)
        screen.blit(img,(A,B))
    '''
