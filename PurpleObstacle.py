from Point import *
from Obstacle import *

import cs1graphics
from random import randint

class PurpleObstacle(Ball):
  def __init__(self, maxSpeed=100, ballRadius=5, color='purple'):    
    super().__init__(maxSpeed, ballRadius, color)

  def interact(self, other, game):
    if self.checkCollision (other):
      game.adjustPoints (3)

