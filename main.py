import pygame
import random
import dove
import generations_controller
import math

doves_list = []
doves_sprites = pygame.sprite.Group([])
food_sprites = pygame.sprite.Group([])
variability = 0.5
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


def split(x, n):
    num_list = []
    if (x < n):
        print(-1)

    elif (x % n == 0):
        for i in range(n):
            print(x // n, end=" ")
    else:
        zp = n - (x % n)
        pp = x // n
        for i in range(n):
            if (i >= zp):
                num_list.append(pp + 1)
            else:
                num_list.append(pp)
    return num_list

def gen_doves_and_food(dove_amount, food_amount):
    global doves_list
    global doves_sprites
    global vel

    amount = food_amount
    length = 800
    num_list = split(dove_amount, 4)
    for i in range(num_list[0]):
        d = (dove.dove(get_offset(i, num_list[0]), 30, vel + (random.randrange(-1, 2))))
        doves_list.append(d)
        doves_sprites.add(d.sprite)
    for i in range(num_list[1]):
        d = (dove.dove(get_offset(i, num_list[1]), 970, vel + (random.randrange(-1, 2))))
        doves_list.append(d)
        doves_sprites.add(d.sprite)
    for i in range(num_list[2]):
        d = (dove.dove(30, get_offset(i, num_list[2]), vel + (random.randrange(-1, 2))))
        doves_list.append(d)
        doves_sprites.add(d.sprite)
    for i in range(num_list[3]):
        d = (dove.dove(970, get_offset(i, num_list[3]), vel + (random.randrange(-1, 2))))
        doves_list.append(d)
        doves_sprites.add(d.sprite)

    for i in range(food_amount):
        f = food(random.randint(200, 800), random.randint(200, 800))
        food_sprites.add(f.sprite)

def new_gen(sdl):
    new_doves = []
    for d in sdl:
        if d.energy >= 2:
            new_doves.append(d)
            new_doves.append(dove.dove(1, 1, (d.vel + random.uniform(-variability, variability))))


def main():
    global doves_list
    global doves_sprites
    global framerate
    global win
    gen_doves_and_food(7, 3)
    for i in range(10):
        suc_doves = generations_controller.run_gen(doves_list, doves_sprites, food_sprites)
        for dove in suc_doves:
            print(dove)
        dove_list = new_gen(suc_doves)
        input("Press Enter for Next Generation")

main()

pygame.quit()