from gameobject import GameObject
from random import randint

class Ball(GameObject):
  def __init__(self):  
    super(Ball, self).__init__(0, 0, 'strawberry.png')
    self.dx = 0
    self.dy = (randint(0, 200) / 100) + 1
    self.reset()
    
  def move(self):
    self.y += self.dy
    self.x += self.dx
    if self.y > 500:
      self.reset()
  
  def reset(self):
    self.x = randint(50, 400)
    self.y = -64 

