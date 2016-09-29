# Geometry.py
# Francois Plamondon
# Summer 2003

# Primitive operations on individual points.

def translate(x, y, transX, transY):
    """translate the point x,y by transX,transY"""
    return (x+transX, y+transY)

def rotate(x, y, centerX, centerY, angle):
    """rotate the point x,y around the point centerX,centerY. angle must be a multiple of 90 degrees."""
    #The general formula is:
    #xR = (x - centerX) * cos(angle) - (y - centerY) * sin(angle) + centerX
    #yR = (x - centerX) * sin(angle) + (y - centerY) * cos(angle) + centerY"
    if angle % 90 != 0:
        raise TypeError, "angle is not a multiple of 90."
    angle = angle % 360
    if angle == 0:
        xR = x
        yR = y
    elif angle == 90:
        xR = -y + centerY + centerX
        yR = x - centerX + centerY
    elif angle == 180:
        xR = -x + centerX + centerX
        yR = -y + centerY + centerY
    else:
        xR = y - centerY + centerX
        yR = -x + centerX + centerY
    return (xR, yR)


def scale(x, y, centerX, centerY, scaleFactorX, scaleFactorY):
    """scale the point x,y. The point used as the center is (centerX,centerY)"""
    xS = (x - centerX)*scaleFactorX + centerX
    yS = (y - centerY)*scaleFactorY + centerY
    return (xS, yS)



