from gameobject import GameObject


class Player(GameObject):
  def __init__ (self):
    super(Player, self).__init__(0, 0, 'dogblue3.png')
    self.dx = 0
    self.dy = 0
    self.reset()

  def left(self):
    if self.dx >= 93:
      self.dx -= 125

  def right(self):
    if self.dx <=343:
      self.dx += 125

  def up(self):
    if self.dy >=93:
      self.dy -= 125

  def down(self):
    if self.dy <= 343:
      self.dy += 125

  def space(self):
    pass

  def move(self):
    self.x -= (self.x - self.dx) * 0.25
    self.y -= (self.y - self.dy) * 0.25

  def reset(self):
    self.x = 250 - 32
    self.y = 250 - 32
