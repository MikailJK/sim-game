# Generates new groups of doves
# Places doves in a list around border of screen
import dove
import random

def get_offset(i, amount, width):
    space = width / (amount + 1)
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

def place_doves(doves_list, dove_amount, screen_width):

    num_list = split(dove_amount, 4)
    count = 0
    for i in range(num_list[0]):
        doves_list[count].x, doves_list[count].x = get_offset(i, num_list[0], screen_width), 30
        count += 1
    for i in range(num_list[1]):
        doves_list[count].x, doves_list[count].y  = get_offset(i, num_list[1], screen_width), screen_width - 30
        count += 1
    for i in range(num_list[2]):
        doves_list[count].x, doves_list[count].y = 30, get_offset(i, num_list[2], screen_width)
        count += 1
    for i in range(num_list[3]):
        doves_list[count].x, doves_list[count].y = screen_width, get_offset(i, num_list[3], screen_width)
        count += 1
    count = 0

def new_gen(sdl, doves_list, doves_sprites, width, var):
    doves_sprites.empty()
    surviving = 0
    dead = 0
    new = 0
    new_list = []
    for d in sdl:
        if d.energy >= (d.vel * 0.5):
            d.energy = 0
            doves_sprites.add(d.sprite)
            new_list.append(d)
            nd = dove.dove(10, 10, (d.vel + random.uniform(-var, var)), (d.vision + random.uniform(-var * 50, var * 50)))
            new_list.append(nd)
            doves_sprites.add(nd.sprite)
            surviving += 1
            new += 1
        elif d.energy == 1:
            surviving += 1
            d.energy = 0
            d.x = width
            new_list.append(d)
            doves_sprites.add(d.sprite)

    print('Surviving: ' + str(surviving))
    print('New: ' + str(new))
    print('Dead: ' + str(dead))
    print('Population: ' + str(surviving + new))
    return new_list


def gen_doves(doves_list, doves_sprites, dove_amount, vel, vision):
    for i in range(dove_amount):
        d = (dove.dove(1, 1, vel + (random.randrange(-1, 2)), vision))
        doves_list.append(d)
        doves_sprites.add(d.sprite)