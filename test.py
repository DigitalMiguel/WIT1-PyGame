import pygame
import random
from sprites import Player
from sprites import Wall

running = True
FPS = 45
BLACK = (0,0,0)
SWEDISH_BLUE = (62, 127, 232)
SWEDISH_YELLOW = (254, 204, 0)
RED = (240,10,10)
WHITE = (255,255,255)
playerX = 150
playerY = 150

# Start up Pygame
pygame.init()
# Start up sound module for Pygame
pygame.mixer.init()
# Set up the screen for
screen = pygame.display.set_mode((640,640))
screen.fill(SWEDISH_BLUE)
# Keeps track of game clock
clock = pygame.time.Clock()
# Create player
player = Player(screen)
# Create a list to hold all sprites
all_sprites = pygame.sprite.Group()
# Add sprites to our list of sprites
all_sprites.add(player)
# Container for walls
#testList = ["A","B","C"]

walls = pygame.sprite.Group()

# Create a layout
layout = [  "                                                            ",
            "W                                                           ",
            "W                                                           ",
            "W                                                           ",
            "W                                                           ",
            "W                                                           ",
            "W                                                           ",
            "W                                                           ",
            "W                                                           ",
            "W                                                           ",
            "W                                                           ",
            "W                                                           ",
            "W                                                           ",
            "W                                          WWWWWWW          ",
            "W                                                           ",
            "W                                                           ",
            "W        RRRRR               WWWWWWW                        ",
            "W                                                           ",
            "W                                                           ",
            "WWWWWWWWWWWWWWWWWW       WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW"]

x = 0
y = 0
size = 32

for row in layout:
    for col in row:
        if col == "W":
            walls.add( Wall((WHITE),x,y,size) )
            x = x + size
        if col == "R":
            walls.add( Wall((RED),x,y,size) )
            x = x + size
        if col == " ":
            x = x + size
    y = y + size
    x = 0

player.localWalls = walls

while running :
    # Set the game speed
    clock.tick(FPS)

    # Wipe screen
    screen.fill(SWEDISH_BLUE)

    # Process Input
    for event in pygame.event.get():
        # Check for exiting out of window
        if event.type == pygame.QUIT :
            running = False

        # Process controls
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                # move the player left
                player.goLeft()
            if event.key == pygame.K_RIGHT:
                player.goRight()
            if event.key == pygame.K_UP:
                player.jump()

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                # stop moving left
                player.stop()
            if event.key == pygame.K_RIGHT:
                player.stop()

    all_sprites.update()

    all_sprites.draw(screen)
    # Draw all walls
    walls.draw(screen)

    # Display new screen
    pygame.display.flip()

    # End of while loop

pygame.quit()
