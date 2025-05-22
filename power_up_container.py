"""containes all power_ups"""
import pygame
from constants import *
from random import randint
from power_ups import PowerUp
from shoot_speed_buff import ShootSpeedBuff

class PowerUpContainer(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self, self.containers)
        self.powerups = []
        self.spawn_timer = POWERUP_SPAWN_RATE
        self.is_spawned = False
        self.containers = None
        self.powerup_types = [ShootSpeedBuff]

    def update(self, dt):
        self.spawn_timer -= dt
        if self.spawn_timer < 0:
            self.spawn_timer = POWERUP_SPAWN_RATE
            if len(self.powerup_types) == 1:
                powerup = self.powerup_types[0]()
                powerup.update(dt)
                print("Powerup spawned")
            else:
                num = randint(0, len(self.powerup_types) - 1)
                powerup = self.powerup_types[num]()
                powerup.update(dt)
                print("Powerup spawned (else clause)")