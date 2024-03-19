import pygame
import sys
import random
from tile import Tile

pygame.init()
clock = pygame.time.Clock()
WIDTH, HEIGHT = 600, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
images = []
counter = 1
DIM = 64
TILESIZE = WIDTH // DIM

def createArray():
    a = [[Tile() for _ in range(DIM)] for _ in range(DIM)]
    return a


array = createArray()

def getBlock():
    lowestEntropy = 6
    r, w = 0, 0
    for row in range(DIM):
        for col in range(DIM):
            if(array[row][col].collapsed == False):
                entropy = len(array[row][col].tiles)
                if(entropy < lowestEntropy):
                    lowestEntropy = entropy
                    r, w = row, col
    return r,w

def loadImages():
    images.append(pygame.image.load('assets/blank.png'))    #0
    images.append(pygame.image.load('assets/up.png'))    #1
    images.append(pygame.image.load('assets/down.png'))    #2
    images.append(pygame.image.load('assets/left.png'))    #3
    images.append(pygame.image.load('assets/right.png'))    #4

def getRemainingTiles(arrayT, tileID, dir):
    tile = []
    result = []


    if dir == "up":
        if tileID == 0:
            tile = [0,1]
        elif tileID == 1:
            tile = [2, 3, 4]
        elif tileID == 2:
            tile = [0, 1]
        elif tileID == 3:
            tile = [2, 3, 4]
        elif tileID == 4:
            tile = [2, 3, 4]
    elif dir == "down":
        if tileID == 0:
            tile = [0, 2]
        elif tileID == 1:
            tile = [0, 2]
        elif tileID == 2:
            tile = [1, 3, 4]
        elif tileID == 3:
            tile = [1, 3, 4]
        elif tileID == 4:
            tile = [1, 3, 4]
    elif dir == "left":
        if tileID == 0:
            tile = [0, 3]
        elif tileID == 1:
            tile = [1, 2, 4]
        elif tileID == 2:
            tile = [1, 2, 4]
        elif tileID == 3:
            tile = [1, 2, 4]
        elif tileID == 4:
            tile = [0, 3]
    elif dir == "right":
        if tileID == 0:
            tile = [0, 4]
        elif tileID == 1:
            tile = [1, 2, 3]
        elif tileID == 2:
            tile = [1, 2, 3]
        elif tileID == 3:
            tile = [0, 4]
        elif tileID == 4:
            tile = [1, 2, 3]

    for tl in arrayT:
        if tl in tile:
            result.append(tl)

    return result

def updateEntropy(row, col, tileID):
    if(row != 0):
        if(array[row-1][col].collapsed == False):
            array[row-1][col].tiles = getRemainingTiles(array[row-1][col].tiles, tileID[0], "up")
    if(col != DIM - 1):
        if(array[row][col+1].collapsed == False):
            array[row][col+1].tiles = getRemainingTiles(array[row][col+1].tiles, tileID[0], "right")
    if(row != DIM - 1):
        if(array[row+1][col].collapsed == False):
            array[row+1][col].tiles = getRemainingTiles(array[row+1][col].tiles, tileID[0], "down")
    if(col != 0):
        if(array[row][col-1].collapsed == False):
            array[row][col - 1].tiles = getRemainingTiles(array[row][col- 1].tiles, tileID[0], "left")
    
    
    

def init():
    # print("Processing: 0 0")
    array[0][0].collapsed = True
    randomTile = random.randint(0, 4)
    array[0][0].tiles = [randomTile]
    updateEntropy(0,0, array[0][0].tiles)
    counter = 1

def doAction(row, col):
    global counter
    counter = counter + 1
    array[row][col].collapsed = True
    if(len(array[row][col].tiles) == 0):
        print("error in ", row, col)
    else:
        randomTile = random.choice(array[row][col].tiles)
        array[row][col].tiles = [randomTile]
        updateEntropy(row, col, array[row][col].tiles)


def draw():
    for row in range(DIM):
        for col in range(DIM):
            if array[row][col].collapsed:
                
                image = pygame.transform.scale(images[array[row][col].tiles[0]], (TILESIZE, TILESIZE))
                screen.blit(image, ((col * TILESIZE), (row * TILESIZE)))
            else:
                pygame.draw.rect(screen, "white", pygame.Rect((col * TILESIZE), (row * TILESIZE), TILESIZE, TILESIZE), 1)

def update():
    row, col = getBlock()
    # print(array[row][col])
    doAction(row, col)
    pygame.display.update()

def main():
    loadImages()
    running = True
    init()
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        if(counter <= (DIM * DIM)):
            draw()
            update()

        clock.tick(DIM * 2)
        
        
        
    

if __name__ == '__main__':
    main()