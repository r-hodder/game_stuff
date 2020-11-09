import pygame as pg

from settings import (
    HEIGHT,
    WIDTH,
    PLAYER_COLOUR,
    PLAYER_ACC,
    PLAYER_FRICTION
)

vec = pg.math.Vector2


class Player(pg.sprite.Sprite):
    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.Surface((12, 16))
        self.image.fill(PLAYER_COLOUR)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH / 2, HEIGHT / 2)
        self.pos = vec(WIDTH / 2, HEIGHT / 2)
        self.vel = vec(0, 0)
        self.acc = vec(0, 0)
        
    def update(self):
        self.acc = vec(0, 0)
        key = pg.key.get_pressed()

        if key[pg.K_LEFT]:
            self.acc.x = -PLAYER_ACC
        if key[pg.K_RIGHT]:
            self.acc.x = PLAYER_ACC

        # Apply friction
        self.acc += self.vel * PLAYER_FRICTION
        # Equations of motion
        self.vel += self.acc
        self.pos += self.vel + 0.5 * self.acc

        # Wrap around the sides of the screen
        if self.pos.x > WIDTH:
            self.pos.x = 0
        if self.pos.x < 0:
            self.pos.x = WIDTH

        self.rect.center = self.pos
