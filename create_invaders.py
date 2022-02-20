import pygame as pg
from spaceships import spaceship
def createInvaders(screen, invaderSkin, bulletSkin, rows, columns, initX, initY):
    invaders = pg.sprite.Group()

    interval = invaderSkin.get_rect().size
    for i in range(0, rows):
            row = []
            for j in range(0, columns):
                invaders.add(spaceship.Invader((initX + interval[0]*1.5*i, initY + interval[1]*1.5*j), screen, invaderSkin, bulletSkin))


    return invaders
