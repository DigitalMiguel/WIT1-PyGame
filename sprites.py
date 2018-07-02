import pygame
import math
vec = pygame.math.Vector2

class Player(pygame.sprite.Sprite):

    # Set speed vector of player
    change_x = 0
    change_y = 0

    def __init__(self,screen):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((100,100))

        pygame.draw.rect(screen, (0,255,0) , ( 0, 0, 100, 100 ) )

        self.image.fill((0,255,0))
        self.rect = self.image.get_rect()
        self.rect.center = (100,100)

    def update(self):

        self.rect.y += self.change_y
        self.rect.x += self.change_x

    # Player-controlled movement:
    def goLeft(self):
        """ Called when the user hits the left arrow. """
        self.change_x = -6

    def stopMove(self):
        self.change_x = 0
