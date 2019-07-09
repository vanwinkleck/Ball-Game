from Point import *

from Ball import *

import cs1graphics
from random import randint

class Obstacle(Ball):
  def __init__(self, maxSpeed=50, ballRadius=10, color='blue'):    
    super().__init__(maxSpeed, ballRadius, color)

  def interact(self, other, game):
    if self.checkCollision (other):
      game.adjustPoints (1)

