from math import *
import numpy as np
def addVectors(angle1, length1, angle2, length2):
    x = sin(angle1) * length1 + sin(angle2) * length2
    y = cos(angle1) * length1 + cos(angle2) * length2
    length = hypot(x, y)
    angle = 0.5 * pi - atan2(y, x)
    return (angle, length)

def sigmoid(z):
    return 1.0/(1+np.exp(-5*(z-1)))