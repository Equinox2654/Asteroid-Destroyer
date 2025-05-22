"""Contains the PowerUp Interface"""
import pygame
from constants import *
from random import randint

class PowerUp(pygame.sprite.Sprite):
    """Base class for all power-ups."""
    def __init__(self):
        pygame.sprite.Sprite.__init__(self, self.containers)
        self.radius = POWERUP_RADIUS
        self.spawn_timer = POWERUP_SPAWN_RATE
        self.powerups = []
        self.active_powerup = None
        self.is_spawned = False
        self.containers = None

    def draw(self, x, y):
        pygame.draw.circle(screen, self.colour, (x, y), self.radius)

    def spawn(self):
        pass
    
    def update(self, dt):
        pass