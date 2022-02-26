import pygame
import random

w, h = 640, 480
win = pygame.display.set_mode((w, h))


class Circle():
    def __init__(self, color, x, y, rad):
        self.color = color
        self.x = x
        self.y = y
        self.rad = rad
        self.dir = 1

    def draw(self):
        pygame.draw.circle(win, self.color, (self.x, self.y), self.rad)

    def move(self):
        if self.dir == 1:
            self.x += 0.1
            if self.x >= w:
                self.dir = -1
        elif self.dir == -1:
            self.x -= 0.1
            if self.x <= 0:
                self.dir = 1


circles = []

r, g, b = 0, 0, 0

for i in range(50):
    circles.append(Circle((r, g, b), i*w//100, i*h//100, 20))
    r += 2
    b += 2

for k in range(50):
    circles.append(Circle((r, g, b), k*w//100 + i *
                   w//100, k*h//100 + i*h//100, 20))
    r += 2
    b -= 2

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    win.fill((255, 255, 255))
    for circl in circles:
        circl.move()
        circl.draw()
    pygame.display.update()
