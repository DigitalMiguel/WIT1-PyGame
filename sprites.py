import pygame

class Player(pygame.sprite.Sprite):

    # Set movement variables
    change_x = 0
    change_y = 0

    walls = []

    def __init__(self, screen):
        # Lets us use sprites
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((100,100))
        pygame.draw.rect(screen, (255,255,255), (150,150,100,100) )
        self.image.fill((0,255,255))
        self.rect = self.image.get_rect()
        self.rect.center = (100,100)

    def calc_grav(self):
        """ Calculate effect of gravity. """
        if self.change_y == 0:
            self.change_y = 1
        else:
            self.change_y += .35

        # See if we are on the ground.
        if self.rect.y >= 400 - self.rect.height and self.change_y >= 0:
            self.change_y = 0
            self.rect.y = 400 - self.rect.height

    def update(self):
        # Gravity
        self.calc_grav()

        # Move left and right
        self.rect.x = self.rect.x + self.change_x
        # Move up and down
        self.rect.y = self.rect.y + self.change_y

        # If you collide with a wall, move out based on velocity
        for wall in self.walls:
            if self.rect.colliderect(wall.rect):
                print("mhm")
            else :
                print("OHHH")



    def jump(self):
        """ Called when user hits 'jump' button. """

        # move down a bit and see if there is a platform below us.
        # Move down 2 pixels because it doesn't work well if we only move down 1
        # when working with a platform moving down.
        self.rect.y += 2
        platform_hit_list = pygame.sprite.spritecollide(self, self.level.platform_list, False)
        self.rect.y -= 2

        # If it is ok to jump, set our speed upwards
        if len(platform_hit_list) > 0 or self.rect.bottom >= 400:
            self.change_y = -10

    def goLeft(self):
        self.change_x = -10

    def goRight(self):
        self.change_x = 5

    def stop(self):
        self.change_x = 0

class Platform(pygame.sprite.Sprite):
    """ Platform the user can jump on """

    def __init__(self,screen):
        """ Platform constructor. Assumes constructed with user passing in
            an array of 4 numbers like what's defined at the top of this
            code. """
        # pygame.sprite.Sprite.__init__(self)
        # #self.image = pygame.Surface((400,50))
        # pygame.draw.rect(screen, (255,255,255), (0,350,400,50) )
        # #self.image.fill((255,255,255))
        # self.rect = self.image.get_rect()
        # self.rect.topleft = (0,350)

        pygame.sprite.Sprite.__init__(self)
        self.rect = pygame.Rect((0,350,400,50) )
        self.image = pygame.Surface(self.rect.size).convert()
        self.image.fill((255,255,255))
        self.type = "normal"

# Nice class to hold a wall rect
class Wall(object):

    def __init__(self, pos, walls,size):
        walls.append(self)
        self.rect = pygame.Rect(pos[0], pos[1], size, size)
