import pygame
import math

pygame.init()

win = pygame.display.set_mode((1000, 1000))
pygame.display.set_caption("Sim")

clock = pygame.time.Clock()
framerate = 30

doves_list = []
food_list = []
food_count = 0

class food(object):

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw(self, win):
        color = (25, 100, 25)
        center = (self.x, self.y)
        pygame.draw.circle(win, color, center, 10)

class dove(object):

    global framerate

    def __init__(self, x, y, vel):
        self.x = x
        self.y = y
        self.vel = vel
        self.start = True

    def find_closest_food(self):
        global food_list
        if food_count <= 0:
            return
        pos = pygame.math.Vector2(self.x, self.y)
        closest_food = min([f for f in food_list], key=lambda f: pos.distance_to(pygame.math.Vector2(f.x, f.y)))
        return closest_food

    def move(self, closest_food):
        global food_count
        delx = closest_food.x - self.x
        dely = closest_food.y - self.y
        if (abs(dely) > 10 or abs(delx) > 10):
            theta = math.atan(delx / dely)
            self.x += math.sin(theta) * self.vel * (abs(delx) / delx)
            self.y += math.cos(theta) * self.vel * (abs(dely) / dely)
        else:
            print(food_list.index(closest_food))
            food_list.remove(closest_food)
            food_count -= 1

    def draw(self, win):
        color = (25, 100, 220)

        if not self.start:
            closest_food = self.find_closest_food()
            self.move(closest_food)
        else:
            self.start = False

        center = (self.x, self.y)
        pygame.draw.circle(win, color, center, 10)


def gen_doves_and_food(amount):
    global doves_list
    global food_list
    global food_count

    length = win.get_width()
    interval = length / (amount )
    for i in range(amount):
        doves_list.append(dove((i * interval), 10, 7))

    for i in range(4):
        for j in range(4):
            food_list.append(food(i * 200 + 200, j * 100 + 250))
            food_count += 1


gen_doves_and_food(1)
print('length: ' + str(len(food_list)))

run = True
while run:
    clock.tick(framerate)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    win.fill((0, 0, 0))

    for i in range(len(food_list)):
        food_list[i].draw(win)

    for i in range(len(doves_list)):
        doves_list[i].draw(win)



    pygame.display.update()

pygame.quit()