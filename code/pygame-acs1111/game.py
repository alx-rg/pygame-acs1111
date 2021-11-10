import pygame
from pygame import color
from random import randint
from gameobject import GameObject
from moose import Moose
from ball import Ball


pygame.init()

# Get the clock
clock = pygame.time.Clock()

screen = pygame.display.set_mode([500, 500])
moose = Moose()
ball = Ball()
sock = GameObject(77, 77, 'strawberry.png')
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

  # Clear the screen
  screen.fill((255, 255, 255))
  
  moose.move()
  
  # Draw the surface
  moose.render(screen)
  ball.render(screen)
  sock.render(screen)
  truck.render(screen)
  # Update the display
  pygame.display.flip()
  clock.tick(60)


