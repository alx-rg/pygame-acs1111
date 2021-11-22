import pygame

class ScoreBoard(pygame.sprite.Sprite):
  def __init__(self, x, y, score):
    super(ScoreBoard, self).__init__() 
    self.score = score
    self.show_score = score
    self.font = pygame.font.SysFont('Arial', 25)
    self.surf = self.font.render(f"{self.score}", False, (204, 255, 0))
    self.dx = 0
    self.dy = 0
    self.y = y
    self.x = x

  def update(self, points):
    self.score += points

  def move(self):
    self.x += self.dx
    self.y += self.dy

  def render(self, screen):
    if self.score < self.show_score:
      self.show_score -= 1
    elif self.score > self.show_score:
      self.show_score +=1
    self.surf = self.font.render(f"{self.show_score}", False, (204, 255, 0))
    screen.blit(self.surf, (self.x, self.y))

  def reset(self):
    self.score = 0
