"""CONTAINS PLAYER CLASS"""
import pygame
from constants import *
from circleshape import CircleShape
from shot import Shot

class Player(CircleShape):

    def __init__(self, x: int, y: int):
        super().__init__(x, y , PLAYER_RADIUS)
        self.rotation = 0
        self.cooldown = 0
        self.lives = 3
        self.spawn_timer = PLAYER_SPAWN_IMMUNITY
        self.colour = (0, 255, 0)
    
    # in the player class
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def player_speed_mult(self):
        if GAME_RUNTIME / 100 < 1:
            PLAYER_SPEED_MULT = 1
        elif GAME_RUNTIME / 100 < 3:
            PLAYER_SPEED_MULT = 1 * GAME_RUNTIME / 100
        else:
            PLAYER_SPEED_MULT = 3
        return PLAYER_SPEED_MULT
    
    def draw(self, screen):
        pygame.draw.polygon(screen, self.colour, self.triangle(), 2)

    def rotate(self, dt):
         self.rotation += PLAYER_TURN_SPEED * dt * PLAYER_SPEED_MULT
    
    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt * PLAYER_SPEED_MULT
    
    def shoot(self): 
        vector = pygame.Vector2(0, 1).rotate(self.rotation) * PLAYER_SHOOT_SPEED
        if self.cooldown <= 0:
            bullet = Shot(self.position.x, self.position.y, vector)
            self.cooldown = PLAYER_SHOOT_COOLDOWN

    def update(self, dt):
        keys = pygame.key.get_pressed()

        PLAYER_SPEED_MULT = self.player_speed_mult()

        if keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(-dt)
        if keys[pygame.K_SPACE]:
            self.shoot()
        
        self.cooldown -= dt
        if self.cooldown < 0:
            self.cooldown = 0
        self.spawn_timer -= dt
        if self.spawn_timer < 0:
            self.spawn_timer = 0
            self.colour = (0, 255, 0)

    def kill(self):
        if self.spawn_timer == 0:
            self.lives -= 1
            self.spawn_timer = PLAYER_SPAWN_IMMUNITY_MAX
            self.colour = (255, 0, 0)

            if self.lives <= 0:
                super().kill()
        