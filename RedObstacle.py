from Point import *
from Obstacle import *

import cs1graphics
from random import randint

class RedObstacle(Obstacle):
    def __init__(self, maxSpeed=50, ballRadius=30, color='red'):
        super().__init__(maxSpeed, ballRadius, color)

    def interact(self, other, game):
        if self.checkCollision (other):
            game.adjustPoints (-1)  
