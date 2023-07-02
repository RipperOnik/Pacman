from AnimatedSprite import AnimatedSprite

class Coin(AnimatedSprite):
     def __init__(self, img, scaling, x = 0, y = 0, dx = 0, dy = 0):
        AnimatedSprite.__init__(self, img, scaling, x, y, dx, dy)
        for i in range(4):
            imgPath = "coin/gold{}.png".format(i+1)
            self.standNeutral.append(loadImage(imgPath))
        self.currentImages = self.standNeutral
        
