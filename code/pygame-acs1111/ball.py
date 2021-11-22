from gameobject import GameObject
from random import randint

class Ball(GameObject):
  def __init__(self):  
    super(Ball, self).__init__(0, 0, 'images/ball.png')
    self.dx = (randint(0, 200) / 100) + 1
    self.dy = 0
    self.reset()
    self.direction = 0
  
  def move(self):
    if self.direction == 0: #right
      self.x += self.dx
      if self.x > 500:
        self.reset()
    elif self.direction == 1: #left
      self.x -= self.dx
      if self.x < -64:
        self.reset()

  def reset(self):
    self.direction = randint(0, 1)
    randomDirection = randint(-64, 500)
    lanes = [93, 218, 343]
    spawn = randint(0,2)
    self.y = (lanes[spawn])
    self.x = randomDirection 
    if self.direction == 0:
        self.x = -64
    if self.direction == 1:
        self.x = 500

