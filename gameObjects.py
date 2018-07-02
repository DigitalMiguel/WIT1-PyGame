import pygame

class Player(pygame.sprite.Sprite):

    def __init__(self, screen):
        # Lets us use sprites
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.Surface((100,100))
        pygame.draw.rect(screen, (255,255,255), (150,150,100,100) )
        self.image.fill((255,255,255))
        self.rect = self.image.get_rect()
        self.rect.center = (100,100)
