import pygame as pg
import config
import time
from random import randrange
import threading
import collision_check as check
# import space_invader as main

stopThread = False

def moveDown(invaders, screen):

    for invader in invaders:
        invader.move((0,25), screen)

def stop():
    global stopThread
    stopThread = True


def moveInvaders(invaders, defender, screen, background):



    #global updateDisplay
    direction = 1
    while not stopThread:



        screen.blit(background, (0,0))

        if len(invaders.sprites()) != 0 and not config.lost:


            if(invaders.sprites()[-1].pos[0] >= config.xSize): #TODO: add image pixels to position
                direction = 0
                moveDown(invaders, screen)
            elif(invaders.sprites()[0].pos[0] <= 0):
                direction = 1
                moveDown(invaders, screen)


            for invader in invaders.sprites():

                    if direction == 1:
                        invader.move((8,0), screen)
                    else:
                        invader.move((-8,0), screen)

                    if not config.lost:
                        if randrange(500) == 1:
                            shootThread = threading.Thread(target=invader.shoot, args=(defender, screen, check.collisionCheck))
                            shootThread.start()

            if(invaders.sprites()[-1].pos[1] >= config.ySize):
                config.lost = True


            time.sleep(.01)



        else:
            myfont = pg.font.SysFont('Comic Sans MS', 30)
            textsurface = myfont.render('Congrats bro/sis you won', False, (255, 255, 255))
            screen.blit(textsurface,(config.xSize/2,config.ySize/2))


        if not config.lost:
            defender.update(screen)
        pg.display.update()
