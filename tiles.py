import pygame as pg

from settings import LUMBER


class Platform(pg.sprite.Sprite):
    def __init__(self, x, y, w, h):
        super().__init__()
        self.image = pg.Surface((w, h))
        self.image.fill(LUMBER)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
