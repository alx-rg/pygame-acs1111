from gameobject import GameObject
from random import randint

class Sock(GameObject):
  def __init__(self):  
    super(Sock, self).__init__(0, 0, 'images/sock.png')
    self.dy = (randint(0, 200) / 100) + 1
    self.dx = 0
    self.reset()
    self.direction = 0
  
  def move(self):
    if self.direction == 0: #right
      self.y += self.dy
      if self.y > 500:
        self.reset()
    elif self.direction == 1: #left
      self.y -= self.dy
      if self.y < -64:
        self.reset()

  def reset(self):
    self.direction = randint(0, 1)
    randomDirection = randint(-64, 500)
    lanes = [93, 218, 343]
    spawn = randint(0,2)
    self.x = (lanes[spawn])
    self.y = randomDirection 
    if self.direction == 0:
        self.y = -64
    if self.direction == 1:
        self.y = 500
