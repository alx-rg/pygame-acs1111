from gameobject import GameObject
from random import randint

class Sock(GameObject):
  def __init__(self):  
    super(Sock, self).__init__(0, 0, 'apple.png')
    self.dy = (randint(0, 200) / 100) + 1
    self.dx = 0
    self.reset()
    
  def move(self):
    self.y += self.dy
    self.x += self.dx
    if self.y > 500:
      self.reset()
  
  
  def reset(self):
    lanes = [93, 218, 343]
    spawn = randint(0,2)
    self.x = (lanes[spawn])
    # self.x = randint(50, 400)
    self.y = -64 

