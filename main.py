import pygame
import random
import dove
import generations_controller
import math

doves_list = []
doves_sprites = pygame.sprite.Group([])
food_sprites = pygame.sprite.Group([])
vel = 5

class food(object):

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.sprite = pygame.sprite.Sprite()
        self.sprite.image = pygame.Surface((20, 20), pygame.SRCALPHA)
        pygame.draw.circle(self.sprite.image, (50, 200, 50), (10, 10), 10)
        self.sprite.rect = pygame.Rect(self.x, self.y, 10, 10)

def get_offset(i, amount):
    length = 1000
    space = length / (amount + 1)
    offset = (i + 1) * space
    return offset

def gen_doves_and_food(dove_amount, food_amount):
    global doves_list
    global doves_sprites
    global vel

    amount = food_amount
    length = 1000
    count = math.ceil(dove_amount / 4)
    for i in range(count):
        d = (dove.dove(get_offset(i, count), 30, vel + (random.randrange(-1, 2))))
        doves_list.append(d)
        doves_sprites.add(d.sprite)
    for i in range(count):
        d = (dove.dove(get_offset(i, count), 970, vel + (random.randrange(-1, 2))))
        doves_list.append(d)
        doves_sprites.add(d.sprite)
    for i in range(count):
        d = (dove.dove(30, get_offset(i, count), vel + (random.randrange(-1, 2))))
        doves_list.append(d)
        doves_sprites.add(d.sprite)
    for i in range(count):
        d = (dove.dove(970, get_offset(i, count), vel + (random.randrange(-1, 2))))
        doves_list.append(d)
        doves_sprites.add(d.sprite)

    for i in range(food_amount):
        f = food(random.randint(200, 800), random.randint(200, 800))
        food_sprites.add(f.sprite)

def new_gen(sdl):
 print()

def main():
    global doves_list
    global doves_sprites
    global framerate
    global win
    gen_doves_and_food(3, 3)
    for dove in doves_list:
        print(dove)
    suc_doves = generations_controller.run_gen(doves_list, doves_sprites, food_sprites)
    for dove in suc_doves:
        print(dove)
    new_list = new_gen(suc_doves)

main()

pygame.quit()