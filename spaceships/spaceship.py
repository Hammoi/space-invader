import pygame as pg
import time
import config


class Object(pg.sprite.Sprite):
    pos = (0,0)
    def __init__(self, pos, screen, skin):

        pg.sprite.Sprite.__init__(self)


        self.pos = pos
        self.skin = skin
        self.rect = skin.get_rect()

        self.size = self.skin.get_rect().size
        screen.blit(skin, pos)

    def move(self, newPos, screen):
        self.pos = (self.pos[0] + newPos[0], self.pos[1] + newPos[1])
        self.update(screen)

    def update(self, screen):
        #print(self.pos)
        screen.blit(self.skin, self.pos)

class Invader(Object):

    def __init__(self, pos, screen, skin, bulletSkin):
        self.bulletSkin = bulletSkin
        super().__init__(pos, screen, skin)

    def shoot(self, target, screen, checker):
        bullet = Bullet((self.pos[0]+self.size[0]/2,self.pos[1]), screen, self.bulletSkin)
        bullet.shoot(target, screen, checker, 10)



class Defender(Object):

    def __init__(self, pos, screen, skin, bulletSkin):
        self.bulletSkin = bulletSkin

        super().__init__(pos, screen, skin)

    def shoot(self, target, screen, checker):
        bullet = Bullet((self.pos[0]+self.size[0]/2,self.pos[1]), screen, self.bulletSkin)
        bullet.shoot(target, screen, checker, -10)


class Bullet(Object):
    def __init__(self, pos, screen, skin):
        super().__init__(pos, screen, skin)

    def shoot(self, targets, screen, checker, speed): #-10 for defender, 10 for invaders
        while self.pos[1] > 0 and self.pos[1] < config.ySize:
            super().move((0, speed), screen)
            time.sleep(0.01)

            if isinstance(targets, Defender):
                if checker(self, targets, isDefender=True):
                    config.lost = True
                    print("the defender is dead :(")

            else:

                collided = pg.sprite.spritecollide(self, targets, dokill=True, collided=checker)

                if len(collided) > 0:
                    break
            #
            # if config.alreadyHit:
            #     break


            # if len(collided) > 0:
            #     print(collided)
