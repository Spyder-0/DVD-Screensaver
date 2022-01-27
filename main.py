import pygame
import time

pygame.init()
width, height = 800, 600
DVD_Logo_Speed = [1, 1]
BG_Colour = 0, 0, 0

screen = pygame.display.set_mode((width, height))

DVD_Logo = pygame.image.load("DVD_Logo.png")
DVD_Logo_Rect = DVD_Logo.get_rect()


# While loop that will loop forever and ever and ever
while True:
  screen.fill(BG_Colour)

  screen.blit(DVD_Logo, DVD_Logo_Rect)
  DVD_Logo_Rect = DVD_Logo_Rect.move(DVD_Logo_Speed)

  # Keeps the DVD bouncing when hits an edge
  if DVD_Logo_Rect.left < 0 or DVD_Logo_Rect.right > width:
    DVD_Logo_Speed[0] = -DVD_Logo_Speed[0]
  if DVD_Logo_Rect.top < 0 or DVD_Logo_Rect.bottom > height:
    DVD_Logo_Speed[1] = -DVD_Logo_Speed[1]

  pygame.display.flip()
  time.sleep(10 / 1000)
