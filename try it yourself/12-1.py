import sys
import pygame
from character import Character
from settings import Settings
class Test:
    def __init__(self):
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((1000,1000))
        pygame.display.set_caption("TRY IT YOURSELF")
        self.bg_color = (0,0,255)
        self.character = Character(self,50,100)
    
    def run_game(self):
        while True:
            self._check_events()
            self.character.update()
            self._update_screen()
    
    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)
    
    def _check_keydown_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.character.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.character.moving_left = True
        if event.key == pygame.K_UP:
            self.character.moving_right = True
        elif event.key == pygame.K_DOWN:
            self.character.moving_left = True
    
    def _check_keyup_events(self,event):
        if event.key == pygame.K_RIGHT:
            self.character.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.character.moving_left = False
        if event.key == pygame.K_UP:
            self.character.moving_right = False
        elif event.key == pygame.K_DOWN:
            self.character.moving_left = False
    
    def _update_screen(self):
        self.screen.fill(self.bg_color)
        self.character.blitme()
        pygame.display.flip()
    
t = Test()
t.run_game()