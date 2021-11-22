import pygame
from pygame import color
from random import randint
from gameobject import GameObject
from bomb import Bomb
from ball import Ball
from player import Player
from sock import Sock
from ScoreBoard import ScoreBoard

pygame.init()

# Get the clock
clock = pygame.time.Clock()

screen = pygame.display.set_mode([500, 500])
background = pygame.image.load('images/grass.png')

all_sprites = pygame.sprite.Group()
fruit_sprites = pygame.sprite.Group()
bomb_sprites = pygame.sprite.Group()

bomb = Bomb()
all_sprites.add(bomb)
bomb_sprites.add(bomb)

ball = Ball()
all_sprites.add(ball)
fruit_sprites.add(ball)

ball1 = Ball()
all_sprites.add(ball1)
fruit_sprites.add(ball1)

sock = Sock()
all_sprites.add(sock)
fruit_sprites.add(sock)

sock1 = Sock()
all_sprites.add(sock1)
fruit_sprites.add(sock1)

player = Player()
all_sprites.add(player)

score = ScoreBoard(30, 30, 0)
all_sprites.add(score)

# Create a game loop
running = True
while running:
  # Looks at events
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False
    elif event.type == pygame.KEYDOWN:
      if event.key == pygame.K_ESCAPE:
        running = False
      elif event.key == pygame.K_LEFT:
        player.left()
        print('LEFT')
      elif event.key == pygame.K_RIGHT:
        player.right()
        print('RIGHT')
      elif event.key == pygame.K_UP:
        player.up()
        print('UP')
      elif event.key == pygame.K_DOWN:
        player.down()
        print('DOWN')
      elif event.key == pygame.K_SPACE:

        print('SPACE')

  # Clear the screen
  screen.fill((255, 255, 255))
  screen.blit(background, (0, 0))
  for entity in all_sprites:
    entity.move()
    entity.render(screen)

  fruit = pygame.sprite.spritecollideany(player, fruit_sprites)
  if fruit:
    fruit.reset()
    score.update(10)

  bomb_fruit = pygame.sprite.spritecollideany(bomb, fruit_sprites)
  if bomb_fruit:
    bomb_fruit.reset()
    score.update(-20)

  if pygame.sprite.collide_rect(player, bomb):
    running = False

  # Update the display
  pygame.display.flip()
  clock.tick(60)


