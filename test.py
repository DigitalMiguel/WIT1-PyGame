import pygame
from sprites import Player
from sprites import Wall

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
screen = pygame.display.set_mode((800,600))
screen.fill(SWEDISH_BLUE)
# Keeps track of game clock
clock = pygame.time.Clock()
# Create player
player = Player(screen)
# Create a list to hold all sprites
all_sprites = pygame.sprite.Group()
# Add sprites to our list of sprites
all_sprites.add(player)

walls = [] # List to hold the walls

# Holds the level layout in a list of strings.
level = [
"WWWWWWWWWWWWWWWWWWWWWWWW",
"W                      W",
"W                      W",
"W             W        W",
"W                      W",
"W                      W",
"W                      W",
"W                      W",
"W                      W",
"W                      W",
"W                      W",
"W                      W",
"WWWWWWWWWWWWWWWWWWWWWWWW",
]

# Parse the level string above. W = wall, E = exit
x = y = 0
size = 2
for row in level:
    for col in row:
        if col == "W":
            Wall((x, y), walls, size)
        if col == "E":
            end_rect = pygame.Rect(x, y, size, size)
        x += size
    y += size
    x = 0

player.walls = walls

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
                # move the player right
                player.goRight()
            if event.key == pygame.K_UP:
                player.jump()

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                # stop moving left
                player.stop()
            if event.key == pygame.K_RIGHT:
                # stop moving right
                player.stop()

    all_sprites.update()

    all_sprites.draw(screen)
    for wall in walls:
        pygame.draw.rect(screen, (255, 255, 255), wall.rect)
    # Display new screen
    pygame.display.flip()

    # End of while loop

pygame.quit()
