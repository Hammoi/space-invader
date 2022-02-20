import pygame as pg

#Screen size
xSize = 900
ySize = 700
rows = 10
columns = 8



background = pg.image.load("./src/background.jpg")
invaderSkin = pg.image.load("./src/invader.png")
defenderSkin = pg.image.load("./src/defender.png")
bulletSkin = pg.image.load("./src/bullet.png")
invaderBulletSkin = pg.image.load("./src/invaderBullet.png")

lost = False
