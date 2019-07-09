from Point import *
from Wall import *

import cs1graphics
from random import randint
from time import time

class Ball:
  _width = 500
  _height = 500

  def __init__(self, maxSpeed=100, ballRadius=10, color='random'):    
    self._radius = ballRadius
    x = randint(self._radius, self._width - self._radius)
    y = randint(self._radius, self._height - self._radius)
    self._position = Point(x, y)
    self._maxSpeed = maxSpeed

    xDir = randint(-self._maxSpeed, self._maxSpeed)
    yDir = randint(-self._maxSpeed, self._maxSpeed)
    self._velocity = Point(xDir, yDir)
    self._velocity.normalize()
    vel = randint(self._maxSpeed // 2, self._maxSpeed)
    self._velocity = self._velocity * vel

    self._startTime = time()
    self._multTime = 0
    self._multSpeed = 1

    self._graphics = cs1graphics.Circle(self._radius)
    if color == 'random':
      randColor = (randint(0,255), randint(0,255), randint(0,255))
      self._graphics.setFillColor(randColor)
    else:
      self._graphics.setFillColor (color)
    self._graphics.moveTo(self._position.getX(), self._position.getY())
    
  def getGraphicalRep(self):
    return self._graphics

  def getRadius(self):
    return self._radius
    
  def getPosition(self):
    return self._position
    
  def getVelocity(self):
    return self._velocity
    
  def setPosition(self, p):
    self._position = p
    
  def setVelocity(self, v):
    self._velocity = v

  def speedMult (self, mult, multTime):
    self._multSpeed = mult
    self._multTime = multTime
    self._startTime = time()

  def setColor (self, color):
    self._graphics.setFillColor (color)

  def distance (self, other):
    return self._position.distance(other.getPosition())

  def collision (self, other):
    # implements non-inertial collisions:
    #    ball directions change normally upon collision,
    #    but ball velocities do not change
    mag = self.getVelocity().magnitude()
    otherMag = other.getVelocity().magnitude()
    
    p = self._position - other.getPosition()
    p.normalize()
    v = other.getVelocity() - self.getVelocity()

    if p * v > 0:
      alpha = p*v
      vel = self.getVelocity() + alpha*p
      otherVel = other.getVelocity() - alpha*p
      vel.normalize()
      otherVel.normalize()
      self.setVelocity( vel * mag ) 
      other.setVelocity( otherVel * otherMag ) 

  def checkCollision (self, other):
    if isinstance (other, Ball):
      if self.distance(other) < (self.getRadius() + other.getRadius()):
        self.collision (other)
        return True
      else:
        return False
    elif isinstance (other, Wall):
      return True
    else:
      return False

  def update(self, timeStep):
    if time()-self._startTime < self._multTime:
      self._position = self._position + self._multSpeed * self._velocity * timeStep
    else:
      self._position = self._position + self._velocity * timeStep

    # check for collision with vertical edge
    if self._position.getX() < self._radius:
      self._position.setX(self._radius)
      self._velocity.setX(-self._velocity.getX())
    elif self._position.getX() > self._width - self._radius:
      self._position.setX(self._width - self._radius)
      self._velocity.setX(-self._velocity.getX())

    # check for collision with horizotal edge
    if self._position.getY() < self._radius:
      self._position.setY(self._radius)
      self._velocity.setY(-self._velocity.getY())
    elif self._position.getY() > self._height - self._radius:
      self._position.setY(self._height - self._radius)
      self._velocity.setY(-self._velocity.getY())
      
    self._graphics.moveTo(self._position.getX(), self._position.getY())

