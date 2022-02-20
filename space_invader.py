from shutil import move
import threading
import pygame as pg
from spaceships import spaceship
import time
import create_invaders as create
import move_invaders as move
import defender_listener as defListener
import collision_check as check
import config

#########################################################################
#                                                                       #
#              			Space Invader - Hanyi Liu		                #
#              			last revised: 2/19/22                           #
#                                                                       #
#   			Classic space invader game recreated in Python using    #
#                               the library PyGame.  	      		    #
#########################################################################





pg.init()
pg.font.init()
#Game imgs

config.invaderSkin = pg.transform.rotozoom(config.invaderSkin, 0, 1/8)
config.defenderSkin = pg.transform.rotozoom(config.defenderSkin, 0, 1/8)
config.bulletSkin = pg.transform.rotozoom(config.bulletSkin, 0 , 1/20)
config.invaderBulletSkin = pg.transform.rotozoom(config.invaderBulletSkin, 0 , 1/20)

bulletSize = config.bulletSkin.get_rect().size
invaderBulletSize = config.invaderBulletSkin.get_rect().size
invaderSize = config.invaderSkin.get_rect().size

print("invader size: {}".format(invaderSize))
#Screen setup
screen = pg.display.set_mode((config.xSize,config.ySize))
screen.fill((0,0,0))
pg.display.set_caption('Super Cool Space Invader')

#Game setup
clock = pg.time.Clock()





#Main loop
running = True



invaders = create.createInvaders(screen, config.invaderSkin, config.invaderBulletSkin, config.rows, config.columns, 100, 100)

defender = spaceship.Defender((100, 600), screen, config.defenderSkin, config.bulletSkin)

# def updateAll(objects, screen):
#     flatList = [item for sublist in objects for item in sublist]
#
#     for object in flatList:
#         object.update(screen)






stopThread = False
updateDisplay = True
invaderThread = threading.Thread(target=move.moveInvaders, args=(invaders, defender, screen, config.background))
invaderThread.start()

defenderThread = threading.Thread(target=defListener.defenderListener, args=(defender, screen, config.background))
defenderThread.start()


while running:

    #screen.blit(config.background, (0,0))



    for e in pg.event.get():
        if e.type == pg.QUIT: #If user quits
            print("User quit.")
            running = False
            move.stop()

            invaderThread.join()
            pg.quit()
            print("Successfully quit")

        if e.type == pg.KEYDOWN:
            if not config.lost:

                # if e.key == (pg.K_LEFT):
                #     defender.move((-10,0), screen)
                # elif e.key == (pg.K_RIGHT):
                #     defender.move((10,0), screen)
                if e.key == (pg.K_SPACE):
                    shootThread = threading.Thread(target=defender.shoot, args=(invaders, screen, check.collisionCheck))
                    shootThread.start()





    if config.lost:

        myfont = pg.font.SysFont('Comic Sans MS', 30)
        textsurface = myfont.render('Yikes man you lost :(', False, (255, 255, 255))
        screen.blit(textsurface,(config.xSize/2,config.ySize/2))

                # shootThread.join()
                # print("bullet shot")

    # direction = 1
    # for i in range(0,len(invaders)):
    #     for j in range(0,len(invaders[i])):
    #         invader = invaders[i][j]
    #         print(invader.pos[0])
    #         print("{}\n".format(config.xSize))
    #         if(direction == 1):
    #             if(invader.pos[0] >= config.xSize): #TODO: add image pixels to position too
    #                 direction = 0
    #             invader.move((8,0), screen)
    #         else:
    #             if(invader.pos[0] <= 0):
    #                 direction = 1
    #             invader.move((-8,0), screen)
    #
    #         time.sleep(.1)
    #
    #         invader.update(screen)

    #defender.update(screen)

    # if updateDisplay:
    #     print("called")
    #pg.display.update()
        #updateDisplay = False
