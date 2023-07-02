from Sprite import Sprite
from Coin import Coin
from AnimatedSprite import AnimatedSprite

SPRITE_SCALE = 50.0/128.0
SPRITE_SIZE = 50.0
MOVESPEED = 5


def setup():
    size(800,600)
    imageMode(CENTER)
    playerImg = loadImage("player/player_stand_right.png")
    global redBrick, brownBrick, crate, player, objects, gold, coins
    player = Sprite(playerImg, 55.0/96.0, 100, 100)
    objects = []
    coins = []
    
    redBrick = loadImage("red_brick.png")
    brownBrick = loadImage("brown_brick.png")
    crate = loadImage("crate.png")
    gold = loadImage("coin/gold1.png")
    
    createObjects("map.csv")
    # coin = Coin(gold, SPRITE_SCALE, 100.0, 100.0)
  
  
def draw():
    background(0, 255, 0);
    player.display()
    resolveObjectCollisions(objects)
    for obj in objects:
        obj.display()
        
    for coin in coins:
        coin.display()
        coin.updateAnimation()


def keyPressed():
    if(keyCode == RIGHT):
        player.changeX = MOVESPEED
    elif (keyCode == LEFT):
        player.changeX = -MOVESPEED
    elif (keyCode == UP):
        player.changeY = -MOVESPEED
    elif (keyCode == DOWN):
        player.changeY = MOVESPEED
        

def keyReleased():
    if(keyCode == RIGHT):
        player.changeX = 0
    elif (keyCode == LEFT):
        player.changeX = 0
    elif (keyCode == UP):
        player.changeY = 0
    elif (keyCode == DOWN):
        player.changeY = 0
        

def createObjects(filename):
    lines = loadStrings(filename)
    for row in range(len(lines)):
        values = split(lines[row], ";")
        for col in range(len(values)):
            if values[col] == "1":
                sprite = Sprite(redBrick, SPRITE_SCALE)
                sprite.centerX = SPRITE_SIZE/2 + col * SPRITE_SIZE
                sprite.centerY = SPRITE_SIZE/2 + row * SPRITE_SIZE
                objects.append(sprite)
            if values[col] == "2":
                sprite = Sprite(crate, SPRITE_SCALE)
                sprite.centerX = SPRITE_SIZE/2 + col * SPRITE_SIZE
                sprite.centerY = SPRITE_SIZE/2 + row * SPRITE_SIZE
                objects.append(sprite)
            if values[col] == "3":
                sprite = Sprite(brownBrick, SPRITE_SCALE)
                sprite.centerX = SPRITE_SIZE/2 + col * SPRITE_SIZE
                sprite.centerY = SPRITE_SIZE/2 + row * SPRITE_SIZE
                objects.append(sprite)
            if values[col] == "4":
                coin = Coin(gold, SPRITE_SCALE)
                coin.centerX = SPRITE_SIZE/2 + col * SPRITE_SIZE
                coin.centerY = SPRITE_SIZE/2 + row * SPRITE_SIZE
                coins.append(coin)
                
                
                
def checkCollisionList(spriteList):
    collisionList = []
    for s in spriteList:
        if player.hasCollidedWith(s):
            collisionList.append(s)
    return collisionList

def resolveObjectCollisions(spriteList):
    player.centerX += player.changeX
    
    collisionList = checkCollisionList(spriteList)
    if len(collisionList) > 0:
        collidedSprite = collisionList[0]
        if player.changeX > 0:
            player.setRight(collidedSprite.getLeft())
        elif player.changeX < 0:
            player.setLeft(collidedSprite.getRight())
    
        
    player.centerY += player.changeY
    collisionList = checkCollisionList(spriteList)
    if len(collisionList) > 0:
        collidedSprite = collisionList[0]
        if player.changeY > 0:
            player.setBottom(collidedSprite.getTop())
        elif player.changeY < 0:
            player.setTop(collidedSprite.getBottom())
    
    
    
    
