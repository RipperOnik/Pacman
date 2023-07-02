from AnimatedSprite import AnimatedSprite

class Player(AnimatedSprite):
    def __init__(self, img, scaling, x = 0, y = 0, dx = 0, dy = 0):
        AnimatedSprite.__init__(self, img, scaling, x, y, dx, dy)
        self.inPlace = True
        self.standLeft = [loadImage("player/player_stand_left.png")]
        self.standRight = [loadImage("player/player_stand_right.png")]
        
        for i in range(3):
            imgPath = "player/player_walk_left{}.png".format(i+1)
            self.moveLeft.append(loadImage(imgPath))
        for i in range(3):
            imgPath = "player/player_walk_right{}.png".format(i+1)
            self.moveRight.append(loadImage(imgPath))
            
        self.currentImages = self.standRight
        
    def updateAnimation(self):
        self.inPlace = self.changeX == 0 and self.changeY == 0
        AnimatedSprite.updateAnimation(self)
    
    def selectDirection(self):
        if self.changeX > 0:
            self.direction = self.RIGHT_FACING
        elif self.changeX < 0:
            self.direction = self.LEFT_FACING
    def selectCurrentImages(self):
        if self.direction == self.RIGHT_FACING:
            if self.inPlace:
                self.currentImages = self.standRight
            else:
                self.currentImages = self.moveRight
        elif self.direction == self.LEFT_FACING:
            if self.inPlace:
                self.currentImages = self.standLeft
            else:
                self.currentImages = self.moveLeft
                
