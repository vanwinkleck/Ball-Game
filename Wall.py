from Point import *

import cs1graphics
from random import randint
from time import time

class Wall:
  _maxThick = 10
  _widthCanvas = 500
  _heightCanvas = 500

  def __init__(self, x=-1, y=-1, width=-1, height=-1, color='black'):    
    if width <= 0 or height <= 0:
        side1 = randint (Wall._maxThick // 4, Wall._maxThick)
        side2 = randint (Wall._maxThick, 20 * Wall._maxThick)
        dir = randint (1, 2)

        if dir == 1:
            width = side1
            height = side2
        else:
            width = side2
            height = side1

    if width >= height:
      self._dir = 'horz'
    else:
      self._dir = 'vert'

    self._area = Point (width, height)

    if x == -1 or y == -1:
        x = randint(0, Wall._widthCanvas - width)
        y = randint(0, Wall._heightCanvas - height)

    self._pos = Point(x, y)

    self._graphics = cs1graphics.Rectangle (width, height)
    self._graphics.moveTo(self._pos.getX(), self._pos.getY())

    if color == 'random':
      randColor = (randint(0,255), randint(0,255), randint(0,255))
      self._graphics.setFillColor(randColor)
    else:
      self._graphics.setFillColor (color)

    self._lastHitTime = time()-5
    self._lastHitBall = None
    
  def getPosition(self):
    return self._pos
    
  def setPosition(self, p):
    self._pos = p
    
  def getGraphicalRep(self):
    return self._graphics
    
#  def setColor (self, color):
#    self._graphics.setFillColor (color)

  def checkCollision (self, ball):
    if ball in self:
      if ball != self._lastHitBall or time()-self._lastHitTime > 0.25:
        self._lastHitTime = time()
        self._lastHitBall = ball
        bpos = ball.getPosition()
        r = ball.getRadius()
        if self._dir == 'horz':
          bVel = ball.getVelocity()
          bVel.setY (-bVel.getY())
          if bpos.getY() < self._pos.getY():
            bpos.setY(self._pos.getY()-r)
          else:
            bpos.setY(self._pos.getY()+r)
        else:
          bVel = ball.getVelocity()
          bVel.setX (-bVel.getX())
          if bpos.getX() < self._pos.getX():
            bpos.setX(self._pos.getX()-r)
          else:
            bpos.setX(self._pos.getX()+r)
        ball.setPosition (bpos)
        return True

    return False

  def __contains__ (self, ball):
    bp = ball.getPosition()

    x0 = self._pos.getX() - self._area.getX() // 2
    x1 = self._pos.getX() + self._area.getX() // 2
    y0 = self._pos.getY() - self._area.getY() // 2
    y1 = self._pos.getY() + self._area.getY() // 2

    r = ball.getRadius()
    if (bp.getX() + r >= x0) and (bp.getX() - r <= x1):
      if (bp.getY() + r >= y0) and (bp.getY() - r <= y1):
        return True

    return False

