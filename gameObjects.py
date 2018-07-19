import pygame
### DBCONN ###
from dbconn import *

class Player(pygame.sprite.Sprite):

    ### DBCONN ###
    dbconn = DBCONN()

    # Set movement variables
    change_x = 0
    change_y = 0

    # Starting positions
    start_x = 100
    start_y = 100

    # Positions of death
    die_x = 0

    # track timer
    timer = 0

    localWalls = pygame.sprite.Group()

    def __init__(self, screen):
        # Lets us use sprites
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((32,32))
        pygame.draw.rect(screen, (255,255,255), (150,150,32,32) )
        self.image.fill((0,255,255))
        self.rect = self.image.get_rect()

        self.rect.center = (self.start_x,self.start_y)

    def update(self):
        # Move left and right
        self.rect.x = self.rect.x + self.change_x

        # Determine the change along the y
        self.calcGrav()

        # Applies gravity
        self.rect.y = self.rect.y + self.change_y

        # Check for platform collision
        for wall in self.localWalls:
            if self.rect.colliderect(wall.rect) and wall.__class__.__name__ != "TrickWall" :
                # Check if VictoryWall
                if wall.victory == 1:
                    self.dbconn.insertTime(self.timer)
                # Collide with walls
                if self.change_y > 0 and self.rect.bottom < wall.rect.bottom :
                    self.rect.bottom = wall.rect.top
                    self.change_y = 0
                elif self.change_y < 0 and self.rect.top > wall.rect.top:
                    self.rect.top = wall.rect.bottom
                    self.change_y = 0
                elif self.rect.bottom > wall.rect.top and self.rect.x < wall.rect.x:
                    self.rect.right = wall.rect.left
                elif self.rect.bottom > wall.rect.top and self.rect.x > wall.rect.x:
                    self.rect.left = wall.rect.right



        # Check how far right player is in screen
        if self.rect.x > 300 :
            for wall in self.localWalls:
                wall.rect.x -= self.change_x
                self.rect.x = 299

        # Don't move past left threshold
        if self.rect.x <= 0:
            self.rect.x = 0

        if self.rect.y > 640 :
            # Save position of death
            self.die_x = self.rect.x


            # Respawn / Reset
            self.rect.center = (self.start_x,self.start_y)
            # Reset the position of all the walls
            for wall in self.localWalls:
                wall.reset()

    def calcGrav(self):

        if self.change_y == 0:
            self.change_y = 2
        else :
            self.change_y = self.change_y + .9

    def goLeft(self):
        self.change_x = -7

    def goRight(self):
        self.change_x = 7

    def jump(self):
        # Test if there's anything below us
        self.rect.y += 2
        wallHitList = pygame.sprite.spritecollide(self, self.localWalls, False)
        self.rect.y -= 2
        # Jump flag
        canJump = 0

        # Check for trickwalls
        for wall in wallHitList:
            if wall.__class__.__name__ != "TrickWall":
                canJump = 1

        # if something is below us, then jump
        if canJump == 1:
            self.change_y = -20

    def stop(self):
        self.change_x = 0

class Wall(pygame.sprite.Sprite):

    # Starting positions
    start_x = 0
    start_y = 0
    victory = 0

    def __init__(self,c,x,y,s):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((s,s))
        self.rect = pygame.Rect(x,y,s,s) # (x,y,width,heights)
        self.image.fill(c)
        self.start_x = x
        self.start_y = y

    def reset(self):
        self.rect.x = self.start_x
        self.rect.y = self.start_y

class VictoryWall(pygame.sprite.Sprite):

    # Starting positions
    start_x = 0
    start_y = 0
    victory = 1


    def __init__(self,c,x,y,s):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((s,s))
        self.rect = pygame.Rect(x,y,s,s) # (x,y,width,heights)
        self.image.fill(c)
        self.color = c
        self.start_x = x
        self.start_y = y

    def reset(self):
        self.rect.x = self.start_x
        self.rect.y = self.start_y

class InvisibleWall(pygame.sprite.Sprite):

    # Starting positions
    start_x = 0
    start_y = 0
    victory = 0

    def __init__(self,c,x,y,s):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((s,s))
        self.rect = pygame.Rect(x,y,s,s) # (x,y,width,heights)
        self.image.fill(c)
        self.start_x = x
        self.start_y = y

    def reset(self):
        self.rect.x = self.start_x
        self.rect.y = self.start_y


class TrickWall(pygame.sprite.Sprite):

    # Starting positions
    start_x = 0
    start_y = 0
    victory = 0

    def __init__(self,c,x,y,s):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((s,s))
        self.rect = pygame.Rect(x,y,s,s) # (x,y,width,heights)
        self.image.fill(c)
        self.start_x = x
        self.start_y = y

    def reset(self):
        self.rect.x = self.start_x
        self.rect.y = self.start_y
