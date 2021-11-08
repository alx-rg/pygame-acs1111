import pygame
from pygame import color
pygame.init()

screen = pygame.display.set_mode([500, 500])

# Create a game loop
running = True
while running:
  # Looks at events
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False

  # Clear the screen
  screen.fill((255, 255, 255))
  # Draw a cicrle 
  i = 0
  while (i < 9):
    color = (211,211,211)
    x_axis = ((i % 3) * 140) + 100
    y_axis = (int(i / 3) * 140) + 100
    position = (x_axis, y_axis)
    i += 1
    pygame.draw.circle(screen, color, position, 50)  
    
  # Update the display
  pygame.display.flip()


