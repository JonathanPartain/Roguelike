import pygame
import sys
from Tilemap import Tilemap
from character import Character

# main loop variable
running = True


pygame.init()
pygame.font.init()

myfont = pygame.font.SysFont("monospace", 15)
# player position
p_row = 2
p_column = 2 

# create the level
level = Tilemap()

# set the player character in the level
level.setPlayer(p_row, p_column)

# create player, has no connection to MAP or level

player = Character(100, 10, p_row, p_column)

# get the level, set it to MAP
MAP = level.getMap()



TILESIZE = 30
MAPWIDTH = level.getWidth()
MAPHEIGHT = level.getHeight()


DISPLAYSURF = pygame.display.set_mode((MAPWIDTH*TILESIZE, (MAPHEIGHT*TILESIZE)+TILESIZE*2))




# colors
BLACK = (0,   0,   0  )
DIRT  = (140, 85,  67 )
GREEN = (0,   255, 0  )
BLUE  = (0,   0,   255)
GRAY  = (100, 100, 100)
WHITE = (255, 255, 255)


# tiles
WALL   = "#"
PLAYER = "@"
FLOOR  = "."
ITEM   = "X"
BLANK  = "_"


# Inventory string
invString = ""

# Link colors to tiles
colors = {
        PLAYER : GREEN,
        WALL   : GRAY,
        FLOOR  : DIRT,
        ITEM   : BLUE,
        BLANK  : WHITE
        }


level.placeItem(5)


while running == True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False



    for row in range(MAPHEIGHT):
        for column in range(MAPWIDTH):
            pygame.draw.rect(DISPLAYSURF, colors[MAP[row][column]], (column*TILESIZE, row*TILESIZE, TILESIZE, TILESIZE))

    pygame.draw.rect(DISPLAYSURF, WHITE, (0, MAPHEIGHT*TILESIZE, TILESIZE*MAPWIDTH, TILESIZE*2))


    events = pygame.event.get()
    for event in events:
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                # movement check
                if MAP[p_row][p_column-1] != "#":
                    # check pickup
                    if MAP[p_row][p_column-1] == "X":
                        player.inventory.append("item")
                    # set floor
                    level.setFloor(p_row, p_column)
                    p_column -= 1
                    level.setPlayer(p_row, p_column)
            if event.key == pygame.K_RIGHT:
                # movement check
                if MAP[p_row][p_column+1] != "#":
                    #movement check
                    if MAP[p_row][p_column+1] == "X":
                        player.inventory.append("item")
                    # set floor
                    level.setFloor(p_row, p_column)
                    p_column += 1
                    level.setPlayer(p_row, p_column)
            if event.key == pygame.K_UP:
                # movement check
                if MAP[p_row-1][p_column] != "#":
                    # check pickup
                    if MAP[p_row-1][p_column] == "X":
                        player.inventory.append("item")
                    # set floor
                    level.setFloor(p_row, p_column)
                    p_row -= 1
                    level.setPlayer(p_row, p_column)
            if event.key == pygame.K_DOWN:
                # movement check
                if MAP[p_row+1][p_column] != "#":
                    # check pickup
                    if MAP[p_row+1][p_column] == "X":
                        player.inventory.append("item")
                    # set floor
                    level.setFloor(p_row, p_column)
                    p_row += 1
                    level.setPlayer(p_row, p_column)

    itemLabel = myfont.render("Inventory: " + ", ".join(player.inventory) , 1, (BLACK))
    hpLabel   = myfont.render("HP: " + str(player.hp), 1, (BLACK))
    atkLabel  = myfont.render("Attack: " + str(player.attack), 1, (BLACK))

    DISPLAYSURF.blit(itemLabel, (30, MAPHEIGHT*TILESIZE))
    DISPLAYSURF.blit(hpLabel, (30, MAPHEIGHT*TILESIZE + 15))
    DISPLAYSURF.blit(atkLabel, (30, MAPHEIGHT*TILESIZE + 30))
    level.setPlayer(p_row, p_column)
    pygame.display.update()


# exit pygame
pygame.quit()
sys.exit()
