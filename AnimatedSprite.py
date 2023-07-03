from Sprite import Sprite

class AnimatedSprite(Sprite):
    NEUTRAL_FACING = 0
    RIGHT_FACING = 1
    LEFT_FACING = 2
    def __init__(self, img, scaling, x = 0, y = 0, dx = 0, dy = 0):
        Sprite.__init__(self, img, scaling, x, y, dx, dy)
        self.direction = self.NEUTRAL_FACING
        self.index = 0
        self.frame = 0
        self.currentImages = []
        self.standNeutral = []
        self.moveLeft = []
        self.moveRight = []
    

    
    def selectDirection(self):
        if self.changeX > 0:
            self.direction = self.RIGHT_FACING;
        elif self.changeX < 0:
            self.direction = self.LEFT_FACING
        else:
            self.direction = self.NEUTRAL_FACING
            
            
    def selectCurrentImages(self):
        if self.direction == self.RIGHT_FACING:
            self.currentImages = self.moveRight
        elif self.direction == self.LEFT_FACING:
            self.currentImages = self.moveLeft
        else:
            self.currentImages = self.standNeutral
            
    def advanceToNextImage(self):
        if self.index >= len(self.currentImages):
            self.index = 0
        self.img = self.currentImages[self.index]
        self.index += 1
        
    def updateAnimation(self):
        self.frame += 1
        if self.frame % 5 == 0:
            self.selectDirection()
            self.selectCurrentImages()
            self.advanceToNextImage()
  
        
