from Point import *
from Obstacle import *

import cs1graphics
from random import randint

class CyanObstacle(Obstacle):
  def __init__(self, maxSpeed=60, ballRadius=25, color='cyan'):    
    super().__init__(maxSpeed, ballRadius, color)
    
  def interact(self, other, game):
    if self.distance(other) < 3 * self.getRadius():
      other.speedMult (5, 3)

      # Also handle collisions
      self.checkCollision (other)
