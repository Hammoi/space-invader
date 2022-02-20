import pygame as pg
import config

stopThread = False

def stop():
    global stopThread
    stopThread = True


def defenderListener(defender, screen, background):

    while not stopThread and not config.lost:

        keys = pg.key.get_pressed()  #checking pressed keys
        if keys[pg.K_RIGHT] and defender.pos[0] < config.xSize-defender.size[0]:
            defender.move((.01,0), screen)
        if keys[pg.K_LEFT] and defender.pos[0] > 0:
            defender.move((-.01,0), screen)
