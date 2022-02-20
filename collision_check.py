import config

def collisionCheck(object, checkObject, isDefender=False):
    xRange = (checkObject.pos[0], checkObject.pos[0]+checkObject.size[0])
    yRange = (checkObject.pos[1], checkObject.pos[1]+checkObject.size[1])

    if xRange[0] <= object.pos[0] <= xRange[1] and yRange[0] <= object.pos[1] <= yRange[1]:
        print("collision detected")
        return True


    else:
        return False
