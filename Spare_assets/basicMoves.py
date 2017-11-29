'''
Dylan Rice
10-7-16
if lab 4
'''
import pygame
from pygame.locals import *

class Person:
    # set all class variables in the constructor
    def __init__(self, newX, newY):
        self.x = newY
        self.y = newY
        self.img = pygame.image.load("elric.gif")
        
    # draw your image
    def draw(self, screen):
        screen.blit(self.img, (self.x, self.y))
        
    # move left unless you hit the edge
    def moveLeft(self):
        self.x = (self.x - 12)
        if self.x < 0:
            self.x = 0
        else:
            pass
    
    # move right unless you hit the edge
    def moveRight(self):
        myRec= self.getRec()
        width = myRec[2]
        self.x = (self.x + 12)
        if self.x + width > 803:
            self.x = 803 - width
        else:
            pass
        
    # move up unless you hit the edge
    def moveUp(self):
        self.y = (self.y - 12)
        if self.y < 0:
            self.y = 0
        else:
            pass
        
    # move down unless you hit the edge
    def moveDown(self):
        myRec= self.getRec()
        height = myRec[3]
        self.y = (self.y + 12)
        if self.y + height > 600:
            self.y = 600 - height
        else:
            pass
    
    # This will be filled out in 2.ifs_collide_lab. 
    # It will return True if your person has 
    # collided with another object
    def collide(self, other):
        # Get other's x, y, width and height
        otherRec = other.getRec()
        otherWidth = otherRec[2]
        otherHeight = otherRec[3]
        otherX = otherRec[0]
        otherY = otherRec[1]
        
        # Get person's width and height
        myRec = self.getRec()
        width = myRec[2]
        height = myRec[3]
        X = myRec[0]
        Y = myRec[1]
        
        # check if person is to the right of the object
        # if self.x greater than (otherX + otherWidth)
            # person and object do not intersect
        if X > (otherX + otherWidth):
            return False
        
        # else check if the person is to the left of the object
        # elif(self.x + width) less than otherX
            # person and object do not intersect
        elif otherX > (self.x + width):
            return False
        
        # elif person is above the object
            # person and object do not intersect
        elif otherY > (self.y + height):
            return False
        
        # elif person is below the object
            # person and object do not intersect
        elif Y > (otherY + otherHeight):
            return False
        
        # else
            # person and object do intersect
        else:
            return True
        

    
    # DO NOT CHANGE THIS
    # This method returns a rectangle - (x, y, width, height) - that represents
    # the object
    def getRec(self):
        myRec = self.img.get_rect()
        return (self.x, self.y, myRec[2], myRec[3])
