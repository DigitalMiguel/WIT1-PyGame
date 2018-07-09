import pygame

class Player(pygame.sprite.Sprite):

    # Set movement variables
    change_x = 0
    change_y = 0

    # Starting positions
    start_x = 100
    start_y = 100

    localWalls = pygame.sprite.Group()

    def __init__(self, screen):
        # Lets us use sprites
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((100,100))
        pygame.draw.rect(screen, (255,255,255), (150,150,100,100) )
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
            if self.rect.colliderect(wall.rect):
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

        if self.rect.y > 640 :
            # Respawn / Reset
            self.rect.center = (self.start_x,self.start_y)
            # Reset the position of all the walls
            for wall in self.localWalls:
                wall.reset()


    def calcGrav(self):

        if self.change_y == 0:
            self.change_y = 2
        else :
            self.change_y = self.change_y + .8

    def goLeft(self):
        self.change_x = -10

    def goRight(self):
        self.change_x = 10

    def jump(self):
        # Test if there's anything below us
        self.rect.y += 2
        wallHitList = pygame.sprite.spritecollide(self, self.localWalls, False)
        self.rect.y -= 2
        # if something is below us, then jump
        if len(wallHitList) > 0:
            self.change_y = -25

    def stop(self):
        self.change_x = 0

class Wall(pygame.sprite.Sprite):

    # Starting positions
    start_x = 0
    start_y = 0

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
