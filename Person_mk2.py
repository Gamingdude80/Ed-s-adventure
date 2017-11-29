import pygame
from pygame.locals import *

class Person:
    # set all class variables in the constructor
    def __init__(self, newX, newY):
        self.x = newX
        self.y = newY
        
        """  Add images to the list of images  """
        self.images = [pygame.image.load("Moving down.gif"), pygame.image.load("Moving left.gif"), pygame.image.load("Moving right.gif"), pygame.image.load("Moving up.gif"), pygame.image.load("Looking down.gif")]
        
        """  Use this to keep track of which image to use """ 
        self.cos = 0
    
    """  draw your person with the correct image  """ 
    def draw(self, screen):
        screen.blit(self.images[self.cos], (self.x, self.y))
        
    """  move person left and set the costume facing left. """ 
    def moveLeft(self):
        self.cos = 1
        self.x = (self.x - 15)
        if self.x < 0:
            self.x = 0
    
    """  move person right and set the costume facing right   """ 
    def moveRight(self):
        self.cos = 2
        myRec= self.getRec()
        width = myRec[2]
        self.x = (self.x + 15)
        if self.x + width > 803:
            self.x = 803 - width
        
    """  move person up and set the costume facing up   """ 
    def moveUp(self):
        self.cos = 3
        self.y = (self.y - 15)
        if self.y < 0:
            self.y = 0

        
    """  move person down and set the costume facing down   """ 
    def moveDown(self):
        self.cos = 0
        myRec= self.getRec()
        height = myRec[3]
        self.y = (self.y + 15)
        if self.y + height > 600:
            self.y = 600 - height

    def standStill(self):
        self.cos = 4
    
    """
    This will return True if your person has collided with other
    """
    def collide(self, other):
        myRec = self.getRec()
        otherRec = other.getRec()
        oRight  = otherRec[0] + otherRec[2]
        oBottom  = otherRec[1] + otherRec[3]
    
        right = myRec[0] + myRec[2]
        bottom = myRec[1] + myRec[3]
        
        
        if (otherRec[0] <= right) and (oRight >= self.x) and (otherRec[1] <= bottom) and (oBottom >= self.y):
            return True
        return False

    """
    This method returns a rectangle - (x, y, width, height) - that represents
    the object
    """
    def getRec(self):
        myRec = self.images[self.cos].get_rect()
        return (self.x, self.y, myRec[2], myRec[3])
