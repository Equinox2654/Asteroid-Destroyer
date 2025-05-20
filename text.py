"""Contains text class for pygame window."""
import pygame

class Text():
    def __init__(self, text, font_size=20, color=(255, 255, 255)):
        self.font = pygame.font.Font(None , font_size)
        self.color = color
        self.text = text
        self.rendered_text = self.font.render(self.text, True, self.color)
        self.rect = self.rendered_text.get_rect()
    
    def draw(self, screen, x, y):
        self.rect.topleft = (x, y)
        screen.blit(self.rendered_text, self.rect)