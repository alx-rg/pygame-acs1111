from gameobject import GameObject
from random import randint

class Ball(GameObject):
  def __init__(self):  
    super(Ball, self).__init__(0, 0, 'strawberry.png')
    self.dx = (randint(0, 200) / 100) + 1
    self.dy = 0
    self.reset()
  
  def move(self):
    self.y += self.dy
    self.x += self.dx
    if self.x > 500 or self.x < -64:
      self.reset()
  
  # def reset(self):
  #   lanes = [93, 218, 343]
  #   spawn = randint(0,2)
  #   self.y = (lanes[spawn])
  #   self.x = -64 

  def reset(self):
    randomDirection = randint(0,1)
    lanes = [93, 218, 343]
    spawn = randint(0,2)
    self.y = (lanes[spawn])
    #self.y = randint(50, 400)
    self.x = -64 
    if randomDirection == 0:
      self.dx = ((randint(0, 200) / 100) + 1) * -1
      if self.x < -64:
        self.reset()
    elif randomDirection == 1:
      self.dx = ((randint(0, 200) / 100) + 1)      
      if self.x > 500:
        self.reset()

