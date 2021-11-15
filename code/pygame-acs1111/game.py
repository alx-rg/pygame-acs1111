import pygame
from pygame import color
from random import randint
from gameobject import GameObject
from moose import Moose
from ball import Ball
from player import Player
from sock import Sock

""" 
TO DO:
4th Step
https://github.com/Tech-at-DU/Pygame-Tutorial/tree/main/04-handling-events
"""
pygame.init()

# Get the clock
clock = pygame.time.Clock()

screen = pygame.display.set_mode([500, 500])
moose = Moose()
ball = Ball()
sock = Sock()
player = Player()
truck = GameObject(200, 200, 'bomb.png')
#surf = pygame.Surface((50, 50))
#surf.fill((255,111, 33))
#box = GameObject(120, 300, 50, 50)


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
  
  sock.move()
  sock.render(screen)

  ball.move()
  ball.render(screen)

  player.move()
  player.render(screen)

  # Draw the surface
  
  truck.render(screen)
  # Update the display
  pygame.display.flip()
  clock.tick(60)


