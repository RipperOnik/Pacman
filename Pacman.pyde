from Sprite import Sprite
from Coin import Coin
from Enemy import Enemy
from Player import Player

SPRITE_SCALE = 50.0/128.0
SPRITE_SIZE = 50.0
MOVESPEED = 5
RIGHT_MARGIN = 400;
LEFT_MARGIN = 60;
VERTICAL_MARGIN = 40;



def setup():
    size(800,600)
    imageMode(CENTER)
    playerImg = loadImage("player/player_stand_right.png")
    global redBrick, brownBrick, crate, player, objects, gold, coins, score, enemies, enemyImage, viewX, viewY
    player = Player(playerImg, 55.0/96.0, 100, 100)
    objects = []
    coins = []
    enemies = []
    score = 0
    viewX = 0
    viewY = 0
    
    redBrick = loadImage("red_brick.png")
    brownBrick = loadImage("brown_brick.png")
    crate = loadImage("crate.png")
    gold = loadImage("coin/gold1.png")
    enemyImage = loadImage("enemy/spider_walk_right1.png")
    
    createObjects("map.csv")

  
  
def draw():
    background(0, 255, 0);
    scroll()
    player.display()
    player.updateAnimation()
    resolveObjectCollisions(objects)
    resolveCoinCollection()
    
    for obj in objects:
        obj.display()
        
    for coin in coins:
        coin.display()
        coin.updateAnimation()
        
    for enemy in enemies:
        enemy.display()
        enemy.update()
        enemy.updateAnimation()
    

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
            if values[col] == "5":
                bLeft = col * SPRITE_SIZE
                bRight = bLeft + 4*SPRITE_SIZE 
                enemy = Enemy(enemyImage, 60.0/72.0, bLeft, bRight)
                enemy.centerX = SPRITE_SIZE/2 + col * SPRITE_SIZE
                enemy.centerY = SPRITE_SIZE/2 + row * SPRITE_SIZE
                enemies.append(enemy)
            
    
                
                
                
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
    
def resolveCoinCollection():
    global score
    player.centerX += player.changeX
    player.centerY += player.changeY
    collisionList = checkCollisionList(coins)
    for coin in collisionList:
        score += 1
        coins.remove(coin)
    player.centerX -= player.changeX
    player.centerY -= player.changeY
    
    
def scroll():
    global viewX, viewY
    
    rightBoundary = viewX + width - RIGHT_MARGIN
    if player.getRight() > rightBoundary:
        viewX += player.getRight() - rightBoundary
        
    leftBoundary = viewX + LEFT_MARGIN
    if player.getLeft() < leftBoundary:
        viewX -= leftBoundary - player.getLeft()
    
    bottomBoundary = viewY + height - VERTICAL_MARGIN
    if player.getBottom() > bottomBoundary:
        viewY += player.getBottom() - bottomBoundary
        
    topBoundary = viewY + VERTICAL_MARGIN
    if player.getTop() < topBoundary:
        viewY -= topBoundary - player.getTop()
        
    translate(-viewX, -viewY)
    
    
