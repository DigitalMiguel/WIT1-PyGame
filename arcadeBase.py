import pygame

FPS = 45

# Starts up Pygame
pygame.init()
# Set up the screen for
screen = pygame.display.set_mode((640,640))
# Color the background blue
screen.fill((62, 127, 232))
# Keeps track of game clock
clock = pygame.time.Clock()
running = True

xMove = 32

while running == True:

    # Set the game speed
    clock.tick(FPS)

    # Color the background blue / wipes the screen
    screen.fill((62, 127, 232))

    for event in pygame.event.get():
        # Check for exiting out of window
        if event.type == pygame.QUIT :
            running = False

    box = pygame.draw.rect(screen, (255,255,255), (xMove,150,32,32) )
    xMove = xMove + 1
    
    pygame.display.flip()


pygame.quit()
