class Sprite(object):
    def __init__(self, img, scaling, x = 0, y = 0, dx = 0, dy = 0):
        self.img = img
        self.scaling = scaling
        self.centerX = x
        self.centerY = y
        self.changeX = dx
        self.changeY = dy
        self.w = img.width * scaling
        self.h = img.height * scaling
    
    def display(self):
        image(self.img, self.centerX, self.centerY, self.w, self.h)
    
    def update(self):
        self.centerX += self.changeX
        self.centerY += self.changeY
        
    def getLeft(self):
        return self.centerX - self.w/2
    def setLeft(self, left):
        self.centerX = left + self.w/2
    
    def getRight(self):
        return self.centerX + self.w/2
    def setRight(self, right):
        self.centerX = right - self.w/2
        
    def getTop(self):
        return self.centerY - self.h/2
    def setTop(self, top):
        self.centerY = top + self.h/2
        
    def getBottom(self):
        return self.centerY + self.h/2
    def setBottom(self, bottom):
        self.centerY = bottom - self.h/2
        
    def hasCollidedWith(self, sprite):
        noXOverlap = self.getRight() <= sprite.getLeft() or self.getLeft() >= sprite.getRight()
        noYOverlap = self.getBottom() <= sprite.getTop() or self.getTop() >= sprite.getBottom()
        if noXOverlap or noYOverlap:
            return False
        else:
            return True
        
        
