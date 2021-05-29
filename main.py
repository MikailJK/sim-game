import pygame
import random

pygame.init()

win = pygame.display.set_mode((1000, 1000))
pygame.display.set_caption("Sim")

clock = pygame.time.Clock()
framerate = 30

doves_list = []
doves_sprites = pygame.sprite.Group([])
food_sprites = pygame.sprite.Group([])

class food(object):

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.sprite = pygame.sprite.Sprite()
        self.sprite.image = pygame.Surface((20, 20), pygame.SRCALPHA)
        pygame.draw.circle(self.sprite.image, (50, 200, 50), (10, 10), 10)
        self.sprite.rect = pygame.Rect(self.x, self.y, 10, 10)

    # def draw(self, win):
    #     color = (25, 100, 25)
    #     center = (self.x, self.y)
    #     pygame.draw.circle(win, color, center, 10)

class dove(object):

    global framerate

    def __init__(self, x, y, vel):
        self.x = x
        self.y = y
        self.vel = vel
        self.start = True
        self.sprite = pygame.sprite.Sprite()
        self.sprite.image = pygame.Surface((20, 20), pygame.SRCALPHA)
        pygame.draw.circle(self.sprite.image, (50, 10, 255), (10, 10), 10)
        self.sprite.rect = pygame.Rect(self.x, self.y, 10, 10)

    def find_closest_food(self):
        global food_list
        pos = pygame.math.Vector2(self.x, self.y)
        closest_food = min([f for f in food_sprites], key=lambda f: pos.distance_to(pygame.math.Vector2(f.rect.center)))
        return closest_food

    def move(self):
        if len(food_sprites) <= 0:
            return
        closest_food = self.find_closest_food()
        delx, dely  = closest_food.rect.x - self.x, closest_food.rect.y - self.y
        dir = pygame.math.Vector2(delx, dely)
        dir.scale_to_length(self.vel)
        self.x += dir.x
        self.y += dir.y
        self.sprite.rect.center = (self.x, self.y)
        #self.sprite.rect.center = (pygame.mouse.get_pos())
        pygame.sprite.spritecollide(self.sprite, food_sprites, True, pygame.sprite.collide_circle)



def gen_doves_and_food(dove_amount, food_amount):
    global doves_list
    global doves_sprites
    global food_list
    global food_count

    length = win.get_width()
    interval = length / (dove_amount)
    for i in range(dove_amount):
        d = (dove((500+(i*100)), 900, 5 + i * 1))
        doves_list.append(d)
        doves_sprites.add(d.sprite)

    for i in range(food_amount):
        f = food(random.randint(10, 990), random.randint(10, 990))
        food_sprites.add(f.sprite)


gen_doves_and_food(3, 100)

run = True
while run:
    clock.tick(framerate)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    win.fill((0, 0, 0))

    for i in range(len(doves_list)):
        doves_list[i].move()

    doves_sprites.draw(win)
    food_sprites.draw(win)

    pygame.display.update()

pygame.quit()