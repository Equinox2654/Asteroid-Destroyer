"""Contains the shoot speed buff PowerUp"""
import pygame
from constants import *
from power_ups import PowerUp
from random import randint

class ShootSpeedBuff(PowerUp):
    """Power-up that increases the player's shot speed."""
    def __init__(self):
        super().__init__()
        self.colour = (0, 0, 255)  # Red color for the shoot speed buff

    def spawn(self):
        """Spawn the power-up at a random position."""
        self.position = pygame.math.Vector2((randint(0, SCREEN_WIDTH)), (randint(0, SCREEN_HEIGHT)))
        self.draw(self.position.x, self.position.y)
        
    
    def activate(self, player):
        """Activate the power-up effect on the player."""
        PLAYER_SHOOT_SPEED_MAX += 100

    def update(self, dt):
        self.spawn()