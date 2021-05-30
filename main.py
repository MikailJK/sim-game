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

screen_width = 800

class food(object):

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.sprite = pygame.sprite.Sprite()
        self.sprite.image = pygame.Surface((20, 20), pygame.SRCALPHA)
        pygame.draw.circle(self.sprite.image, (50, 200, 50), (10, 10), 10)
        self.sprite.rect = pygame.Rect(self.x, self.y, 10, 10)

def get_offset(i, amount):
    global screen_width
    space = screen_width / (amount + 1)
    offset = (i + 1) * space
    return offset


def split(x, n):
    num_list = []
    if (x < n):
        for i in range(x):
            num_list.append(int(1))
        for i in range(n-x):
            num_list.append(int(0))

    elif (x % n == 0):
        for i in range(n):
            num_list.append(int(x/n))
    else:
        zp = n - (x % n)
        pp = x // n
        for i in range(n):
            if (i >= zp):
                num_list.append(pp + 1)
            else:
                num_list.append(pp)
    return num_list

def place_doves(dove_amount):
    global doves_list
    global doves_sprites
    global vel
    global screen_width

    num_list = split(dove_amount, 4)
    count = 0
    for i in range(num_list[0]):
        doves_list[count].x, doves_list[count].x = get_offset(i, num_list[0]), 30
        count += 1
    for i in range(num_list[1]):
        doves_list[count].x, doves_list[count].y  = get_offset(i, num_list[1]), screen_width - 30
        count += 1
    for i in range(num_list[2]):
        doves_list[count].x, doves_list[count].y = 30, get_offset(i, num_list[2])
        count += 1
    for i in range(num_list[3]):
        doves_list[count].x, doves_list[count].y = screen_width, get_offset(i, num_list[3])
        count += 1
    count = 0

def gen_food(food_amount):
    global food_sprites
    global screen_width
    for i in range(food_amount):
        f = food(random.randint(screen_width * 0.2, screen_width * 0.8), random.randint(screen_width * 0.2, screen_width * 0.8))
        food_sprites.add(f.sprite)

def gen_doves(dove_amount):
    global doves_sprites
    global doves_list
    for i in range(dove_amount):
        d = (dove.dove(1, 1, vel + (random.randrange(-1, 2))))
        doves_list.append(d)
        doves_sprites.add(d.sprite)

def new_gen(sdl):
    global doves_list
    global doves_sprites
    new_doves = []
    new_doves.clear()
    doves_sprites.empty()
    surviving = 0
    dead = 0
    new = 0
    for d in sdl:
        if d.energy >= 2:
            d.energy = 0
            new_doves.append(d)
            doves_sprites.add(d.sprite)
            nd = dove.dove(10, 10, (d.vel + random.uniform(-variability, variability)))
            new_doves.append(nd)
            doves_sprites.add(nd.sprite)
            surviving += 1
            new += 1
        elif d.energy == 1:
            surviving += 1
            d.energy = 0
            d.x = screen_width
            new_doves.append(d)
            doves_sprites.add(d.sprite)
        else:
            dead += 1

    doves_list.clear()
    doves_list = new_doves
    print('Surviving: ' + str(surviving))
    print('New: ' + str(new))
    print('Dead: ' + str(dead))


def main():
    global doves_list
    global doves_sprites
    global food_sprites
    global framerate
    global win
    food_amount = 4
    doves_amount = 5
    gen_food(food_amount)
    gen_doves(doves_amount)
    place_doves(doves_amount)
    for i in range(100):
        suc_doves = generations_controller.run_gen(doves_list, doves_sprites, food_sprites)
        for dove in suc_doves:
           print(dove)
        new_gen(suc_doves)
        #print(doves_list)
        place_doves(len(doves_list))
        gen_food(food_amount)
        input("Press Enter for Next Generation")

main()

pygame.quit()