import pygame
from pygame.locals import *

pygame.init()

clock = pygame.time.Clock()
fps = 60

screen_width = 864
screen_height = 936

screen = pygame.display.set_mode((screen_width, screen_height))

pygame.display.set_caption("Otaku game")

ground_scroll = 0
scroll_speed = 4

bg = pygame.image.load("../img/bg.png")
ground_img = pygame.image.load("../img/ground.png")

otaku_group=pygame.sprite.Group()


class Otaku(pygame.sprite.Sprite):
  def __init__(self, x, y):
    pygame.sprite.Sprite.__init__(self)
    self.images = []
    self.index = 0
    self.counter = 0

    for num in range(1, 4):
      img = pygame.image.load(f"../img/otaku{num}.png")
      self.images.append(img)

    self.image = self.images[self.index]
    self.rect = self.image.get_rect()
    self.rect.center = [x, y]
  
  def update(self):
    self.counter += 1
    flap_cooldown = 5

    if self.counter > flap_cooldown:
      self.counter = 0
      self.index += 1
      if self.index >= len(self.images):
        self.index = 0

      self.image = self.images[self.index]

otaku_group = pygame.sprite.Group()

flappy = Otaku(100, int(screen_height / 2))

otaku_group.add(flappy)

run = True

while run:

  clock.tick(fps)

  screen.blit(bg, (0, 0))

  otaku_group.draw(screen)
  otaku_group.update()

  screen.blit(ground_img, (ground_scroll, 768))
  ground_scroll -= scroll_speed

  if abs(ground_scroll) > 35:
    ground_scroll = 0

  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      run = False

  pygame.display.update()

pygame.quit()