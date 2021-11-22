from gameobject import GameObject
from random import randint, choice

class Bomb(GameObject):
  def __init__(self):  
    super(Bomb, self).__init__(0, 0, 'images/bomb.png')
    self.dx = 0
    self.dy = 0
    self.reset()

  def move(self):
    self.x += self.dx
    self.y += self.dy
    if self.y > 500 or self.y < -64 or self.x > 500 or self.x < -64:
      self.reset()
  
  def reset(self):
    random_direction = randint(1,4)
    lanes = (93, 218, 343)
    if random_direction == 1:
      self.x = -64
      self.y = choice(lanes)
      self.dx = (randint(0, 200) / 100) + 1
      self.dy = 0
    if random_direction == 2:
      self.x = 500
      self.y = choice(lanes)      
      self.dx = ((randint(0, 200) / 100) + 1) * -1
      self.dy=0
    if random_direction == 3:
      self.y = -64
      self.x = choice(lanes)      
      self.dy = (randint(0, 200) / 100) + 1
      self.dx = 0
    if random_direction == 4:
      self.y = 500
      self.x = choice(lanes)
      self.dy = ((randint(0, 200) / 100) + 1) * -1
      self.dx = 0


