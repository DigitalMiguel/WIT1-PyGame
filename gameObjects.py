import pygame

class Player(pygame.sprite.Sprite):

    # Set movement variables
    change_x = 0
    change_y = 0

    def __init__(self, screen):
        # Lets us use sprites
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.Surface((100,100))
        pygame.draw.rect(screen, (255,255,255), (150,150,100,100) )
        self.image.fill((0,255,255))
        self.rect = self.image.get_rect()
        self.rect.center = (100,100)

    def update(self):
        # Move left and right
        self.rect.x = self.rect.x + self.change_x


    def goLeft(self):
        self.change_x = -5

    def goRight(self):
        self.change_x = 5

    def stop(self):
        self.change_x = 0
