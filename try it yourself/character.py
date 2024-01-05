import pygame
import sys

class Character:
    def __init__(self, ai_game, width, height):
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        self.settings = ai_game.settings
        self.original_image = pygame.image.load('/Users/tsrk04/Desktop/-_-/SSN/2ND SEM/alien invasion/try it yourself/rocket.png')
        self.original_rect = self.original_image.get_rect()
        self.rect = pygame.Rect(0, 0, width, height)
        self.rect.center = self.screen_rect.center
        self.image = pygame.transform.scale(self.original_image, (width, height))

        self.x = float(self.rect.x)

        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

    def update(self):
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.character_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.character_speed
        if self.moving_up and self.rect.right > 0:
            self.y += self.settings.character_speed
        if self.moving_down and self.rect.left > self.screen_rect.bottom:
            self.y -= self.settings.character_speed


    def blitme(self):
        self.screen.blit(self.image, self.rect)
