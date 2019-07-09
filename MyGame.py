from BallGame import *
from Wall import *
from Obstacle import *
from RedObstacle import *
from PurpleObstacle import *
from GreenObstacle import *
from CyanObstacle import *
game = BallGame(width=800, height=650, maxSpeed=250,
			moveDir='mouse dir')
##                        moveDir='to mouse')

w = Wall (400, 325, 400, 5)
game.addWall (w)

w2 =Wall (325, 400, 400, 5)
game.addWall (w2)

w3 =Wall (375, 500, 300, 5)
game.addWall (w3)

w4 =Wall(250, 250, 250, 5)
game.addWall (w4)

for i in range(10):
  b = Obstacle (maxSpeed=150)
  
  game.addObstacle (b)

b2 = GreenObstacle (maxSpeed=50, ballRadius=20)
game.addObstacle (b2)

b3 = RedObstacle (maxSpeed=50, ballRadius=20)
game.addObstacle (b3)

b4 = PurpleObstacle (maxSpeed=100, ballRadius=10)
game.addObstacle (b4)

b5 = CyanObstacle (maxSpeed=60, ballRadius=15)
game.addObstacle (b5)

game.run()
