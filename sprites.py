import pygame as pg

from settings import (
    HEIGHT,
    WIDTH,
    PLAYER_COLOUR,
    PLAYER_ACC,
    PLAYER_FRICTION,
    PLAYER_GRAVITY,
    LUMBER
)

vec = pg.math.Vector2


class Player(pg.sprite.Sprite):
    def __init__(self, game):
        pg.sprite.Sprite.__init__(self)
        self.game = game
        self.image = pg.Surface((12, 16))
        self.image.fill(PLAYER_COLOUR)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH // 2, HEIGHT // 2)
        self.pos = vec(WIDTH // 2, HEIGHT // 2)
        self.vel = vec(0, 0)
        self.acc = vec(0, 0)

    def jump(self):
        self.rect.x += 1
        hits = pg.sprite.spritecollide(self, self.game.platforms, False)
        self.rect.x -= 1
        if hits:
            self.vel.y = -3

    def update(self):
        self.acc = vec(0, PLAYER_GRAVITY)
        key = pg.key.get_pressed()

        if key[pg.K_LEFT]:
            self.acc.x = -PLAYER_ACC
        if key[pg.K_RIGHT]:
            self.acc.x = PLAYER_ACC

        # Apply friction
        self.acc.x += self.vel.x * PLAYER_FRICTION
        # Equations of motion
        self.vel += self.acc
        self.pos += self.vel + 0.5 * self.acc

        # Wrap around the sides of the screen
        if self.rect.left > WIDTH:
            self.pos.x = 0
        if self.rect.right < 0:
            self.pos.x = WIDTH

        self.rect.midbottom = self.pos
