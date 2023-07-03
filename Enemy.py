from AnimatedSprite import AnimatedSprite

class Enemy(AnimatedSprite):
    def __init__(self, img, scaling, bLeft, bRight, x = 0, y = 0, dx = 0, dy = 0):
        AnimatedSprite.__init__(self, img, scaling, x, y, dx, dy)
        self.bLeft = bLeft
        self.bRight = bRight
        for i in range(3):
            imgPath = "enemy/spider_walk_left{}.png".format(i+1)
            self.moveLeft.append(loadImage(imgPath))
        for i in range(3):
            imgPath = "enemy/spider_walk_right{}.png".format(i+1)
            self.moveRight.append(loadImage(imgPath))
            
        self.currentImages = self.moveRight
        self.direction = self.RIGHT_FACING
        self.changeX = 1
        
    def update(self):
        AnimatedSprite.update(self)
        if self.getLeft() <= self.bLeft:
            self.setLeft(self.bLeft)
            self.changeX *= -1
        elif self.getRight() >= self.bRight:
            self.setRight(self.bRight)
            self.changeX *= -1
        
