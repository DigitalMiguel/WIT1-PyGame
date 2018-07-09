import pygame

class Player(pygame.sprite.Sprite):

    # Set movement variables
    change_x = 0
    change_y = 0

    # Set starting variables
    start_x = 150
    start_y = 150

    localWalls = pygame.sprite.Group()

    def __init__(self, screen):
        # Lets us use sprites
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.Surface((32,32))
        pygame.draw.rect(screen, (255,255,255), (self.start_x,self.start_y,32,32) )
        self.image.fill((0,255,255))
        self.rect = self.image.get_rect()
        self.rect.center = (self.start_x,self.start_y)


    def update(self):
        # Move left and right
        self.rect.x = self.rect.x + self.change_x

        # Determine the change along the y
        self.calcGrav()

        # Sets position
        self.rect.y = self.rect.y + self.change_y
        # Check for platform collision
        for wall in self.localWalls:
            if self.rect.colliderect(wall.rect):
                ### NEW COLLISION ###
                if self.rect.bottom < wall.rect.bottom and self.change_y > 0:
                    self.rect.bottom = wall.rect.top
                    self.change_y = 0

                if self.rect.bottom > wall.rect.top and self.rect.x < wall.rect.x:
                    self.rect.right = wall.rect.left
                elif self.rect.bottom > wall.rect.top and self.rect.x > wall.rect.x:
                    self.rect.left = wall.rect.right

        # Check how far right player is in screen
        if self.rect.x > 300 :
            for wall in self.localWalls:
                wall.rect.x -= self.change_x
                self.rect.x = 299

        if self.rect.y > 640 :
            self.reset()

    def calcGrav(self):

        if self.change_y == 0:
            self.change_y = 3
        else :
            self.change_y = self.change_y + .8

    def goLeft(self):
        self.change_x = -7

    def goRight(self):
        self.change_x = 7

    def jump(self):
        # Test if there's anything below us
        self.rect.y += 2
        wallHitList = pygame.sprite.spritecollide(self, self.localWalls, False)
        self.rect.y -= 2
        # if something is below us, then jump
        if len(wallHitList) > 0:
            self.change_y = -20

    def stop(self):
        self.change_x = 0

    def reset(self):
        self.rect.x = self.start_x
        self.rect.y = self.start_y
        for wall in self.localWalls:
            wall.reset()

class Wall(pygame.sprite.Sprite):

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
