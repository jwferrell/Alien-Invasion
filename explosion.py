import pygame

class Explosion(pygame.sprite.Sprite):
    def __init__(self, ai_game, position):
        super().__init__()
        self.screen = ai_game.screen
        self.image = pygame.image.load("images/explosion.png")
        self.rect = self.image.get_rect()
        self.rect.center = position
        self.timer = 15  # frames to show explosion (~0.25s at 60fps)

    def update(self):
        self.timer -= 1
        if self.timer <= 0:
            self.kill()  # remove from group after timer ends

    def draw(self):
        self.screen.blit(self.image, self.rect)
