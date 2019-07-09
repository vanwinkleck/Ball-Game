from Point import *
from Obstacle import *

import cs1graphics
from random import randint

class GreenObstacle(Obstacle):
  def __init__(self, maxSpeed=50, ballRadius=30, color='green'):    
    super().__init__(maxSpeed, ballRadius, color)
    
  def interact(self, other, game):
    if self.distance(other) < 3 * self.getRadius():
      other.speedMult (0.5, 3)

      # Also handle collisions
      self.checkCollision (other)

