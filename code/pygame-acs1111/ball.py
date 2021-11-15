from gameobject import GameObject
from random import randint

class Ball(GameObject):
  def __init__(self):  
    super(Ball, self).__init__(0, 0, 'strawberry.png')
    self.dy = 0
    self.dx = (randint(0, 200) / 100) + 1
    self.reset()
    
  def move(self):
    self.y += self.dy
    self.x += self.dx
    if self.x > 500:
      self.reset()
  
  def reset(self):
    side_spawn = [93, 218, 343]
    spawn = randint(0,2)
    self.y = (side_spawn[spawn])
    #self.y = randint(50, 400)
    self.x = -64 

