from Ball import *
from Wall import *
from Obstacle import *
##from RedObstacle import *
##from PurpleObstacle import *
from GreenObstacle import *

from time import sleep, time

class BallGame:
  _addMoveTime = 5
  
  def __init__(self, numObstacles=0, width=500, height=500,
               ballRadius=10, maxSpeed=100, moveDir='to mouse'):
    # BallGame can re-define Ball's class variables, as desired
    Ball._width = width
    Ball._height = height

    self._radius = ballRadius

    self._maxSpeed = maxSpeed

    self._paper = cs1graphics.Canvas(width, height)
    self._paper.setAutoRefresh(False)

    # create random walls
    self._walls = []
##    for i in range(numObstacles // 2):
##      w = Wall ()
##      self._walls.append(w)
##      self._paper.add(w.getGraphicalRep())

    # create random obstacles
    self._obstacles = []
    for i in range(numObstacles):
##      if i <= (1/2)*numObstacles:
##        b = Obstacle(maxSpeed=self._maxSpeed // 2)	# , color='blue')
##      elif i <= (3/4)*numObstacles:
##        b = Red (maxSpeed = self._maxSpeed // 2)
##      else:
##        b = Purple (maxSpeed = self._maxSpeed // 2)
      b = Obstacle (maxSpeed = self._maxSpeed // 2)
      self._paper.add(b.getGraphicalRep())
      self._obstacles.append(b)

    # create player's Ball
    self._ball = Ball(maxSpeed = self._maxSpeed)
    self._ball.setColor('orange')
    self._paper.add (self._ball.getGraphicalRep())

    # variables facilitating player movement
    self._lastMousePos = self._paper.getMouseCoordinates()
    self._lastMoveTime = time()-5
    self._moveDir = moveDir

    # number of moves available
    self._numMoves = 3
    self._dispMoves = cs1graphics.Text (str(self._numMoves))
    self._dispMoves.setFontSize (20)
    self._dispMoves.setFontColor ('magenta')
    self._dispMoves.moveTo (20,20)
    self._paper.add (self._dispMoves)

    # points
    self._points = 0
    self._dispPts = cs1graphics.Text (str(self._points))
    self._dispPts.setFontSize (20)
    self._dispPts.setFontColor ('red')
    self._dispPts.moveTo (width - 20, 20)
    self._paper.add (self._dispPts)
    
    self._paper.refresh()
    
  def run(self):
    lastUpdateTime = time()
    movesTime = 0
    while True:
      currentTime = time()
      timeStep = currentTime - lastUpdateTime
      
      movesTime += timeStep
      if movesTime > BallGame._addMoveTime:
        movesTime -= BallGame._addMoveTime
        self._updateNumMoves(1)

      # move Ball:     
      self._checkMouseMove()
      self._ball.update (timeStep)

      # check if player's Ball collides with obstacles
      b = self._ball
      for b2 in self._obstacles:
        b2.interact(b, self)

      # check if player's Ball collides with walls
      b = self._ball
      for w in self._walls:
        w.checkCollision (b)

      # move Obstacles
      for b in self._obstacles:
        b.update(timeStep)
        
      # check balls for collisions
      for i in range(len(self._obstacles)):
        # only need to check balls at index i with those at index > i
        #     (rest already checked)
        for b2 in self._obstacles[i+1:]:
          self._obstacles[i].checkCollision(b2)

        # check if obstacle collides with wall        
        for w in self._walls:
          w.checkCollision(self._obstacles[i])
        
      self._paper.refresh()
      lastUpdateTime = currentTime

  def addObstacle (self, obstacle):
    self._obstacles.append (obstacle)
    self._paper.add (obstacle.getGraphicalRep())

  def addWall (self, wall):
    self._walls.append (wall)
    self._paper.add (wall.getGraphicalRep())

  def _checkMouseMove (self):
    b = self._ball
    mousePos = self._paper.getMouseCoordinates()
    # ignore minor movement (< 15)
    if mousePos.distance(self._lastMousePos) >= 15:
      # if equals:
      #     'mouse dir' -- move ball in direction mouse moved
      #     'to mouse'  -- move ball towards mouse position
      if self._numMoves > 0 and time()-self._lastMoveTime > 0.1:
        if self._moveDir == 'mouse dir':
          mouseDiff = mousePos - self._lastMousePos
          mvDir = Point (mouseDiff.getX(), mouseDiff.getY())
        else:
          mvDir = Point (mousePos.getX(), mousePos.getY()) - b.getPosition()
        mvDir.normalize()
        b.setVelocity (b.getVelocity().magnitude() * mvDir)
        self._updateNumMoves(-1)
        self._lastMoveTime = time()
      self._lastMousePos = mousePos

  def adjustPoints (self, amtChange):
    self._points += amtChange
    if self._points < 0:
      self._points = 0
    self._dispPts.setMessage (str(self._points))

  def _updateNumMoves (self, amtChange):
    self._numMoves += amtChange
    if (self._numMoves < 0):
      self._numMoves = 0
    self._dispMoves.setMessage (str(self._numMoves))

if __name__ == '__main__':
  game = BallGame(width=800, height=650, maxSpeed=250,
			moveDir='mouse dir')
##                        moveDir='to mouse')

  w = Wall (400, 325, 400, 5)
  game.addWall (w)

  for i in range(10):
    b = Obstacle (maxSpeed=150)
    game.addObstacle (b)

  b2 = GreenObstacle (maxSpeed=50, ballRadius=20)
  game.addObstacle (b2)

  game.run()
