import pygame
from sprites import Player

yo = True
running = True
FPS = 30
BLACK = (0,0,0)
SWEDISH_BLUE = (62, 127, 232)
SWEDISH_YELLOW = (254, 204, 0)
WHITE = (255,255,255)
playerX = 150
playerY = 150

# Start up Pygame
pygame.init()
# Start up sound module for Pygame
pygame.mixer.init()
# Set up the screen for
screen = pygame.display.set_mode((400,400))
screen.fill(SWEDISH_BLUE)
# Keeps track of game clock
clock = pygame.time.Clock()

all_sprites = pygame.sprite.Group()
player = Player(screen)
all_sprites.add(player)

while running :
    # Set the game speed
    clock.tick(FPS)

    screen.fill(SWEDISH_BLUE)
    # Change background
    # if yo:
    #     screen.fill(WHITE)
    #     yo = False
    # else :
    #     screen.fill(BLACK)
    #     yo = True

    # Process Input
    for event in pygame.event.get():
        # Check for exiting out of window
        if event.type == pygame.QUIT :
            running = False

        # Process controls
        # if event.type == pygame.KEYDOWN:
        #     if event.key == pygame.K_LEFT:
        #         playerX = playerX - 10
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player.goLeft()

        if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT and player.change_x < 0:
                    player.stopMove()

    all_sprites.update()

    # Process controls continuously
    # keys = pygame.key.get_pressed()
    # if keys[pygame.K_RIGHT]:
    #     playerX = playerX + 10
    # if keys[pygame.K_LEFT]:
    #     playerX = playerX - 10
    # if keys[pygame.K_UP]:
    #     playerY = playerY - 10
    # if keys[pygame.K_DOWN]:
    #     playerY = playerY + 10

    # Drawing our player                      (x,y,width,height)
    pygame.draw.rect(screen, SWEDISH_YELLOW , ( playerX, playerY, 100, 100 ) )

    # Drawing a circle
    # pygame.draw.circle(screen, (255,0,0), (0,0) , 50)
    all_sprites.draw(screen)

    # Display new screen
    pygame.display.flip()

    # End of while loop

pygame.quit()
