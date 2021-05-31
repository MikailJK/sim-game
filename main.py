import pygame
import random
import dove
import generations_controller
import dove_manager



food_sprites = pygame.sprite.Group([])
variability = 1
vision = 150
vel = 5

screen_width = 1000


class food(object):

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.sprite = pygame.sprite.Sprite()
        self.sprite.image = pygame.Surface((20, 20), pygame.SRCALPHA)
        pygame.draw.circle(self.sprite.image, (50, 200, 50), (10, 10), 10)
        self.sprite.rect = pygame.Rect(self.x, self.y, 10, 10)


def gen_food(food_amount):
    global food_sprites
    global screen_width
    food_sprites.empty()
    for i in range(food_amount):
        f = food(random.randint(screen_width * 0.2, screen_width * 0.8), random.randint(screen_width * 0.2, screen_width * 0.8))
        food_sprites.add(f.sprite)


def main():
    doves_list = []
    doves_sprites = pygame.sprite.Group([])
    global food_sprites
    food_amount = 10
    doves_amount = 10
    gen_food(food_amount)
    dove_manager.gen_doves(doves_list, doves_sprites, doves_amount, vel, vision)
    dove_manager.place_doves(doves_list, doves_amount, screen_width)

    for i in range(50):
        average_vel = 0
        average_vision = 0
        for d in doves_list:
            average_vel += d.vel
            average_vision += d.vision
        average_vel = round(average_vel / len(doves_list), 2)
        average_vision = round(average_vision / len(doves_list), 2)
        print('Average Velocity: ' + str(average_vel))
        print('Average Vision: ' + str(average_vision))
        suc_doves = generations_controller.run_gen(doves_list, doves_sprites, food_sprites)
        #for d in suc_doves:
        #    print(d)
        doves_list = dove_manager.new_gen(suc_doves, doves_list, doves_sprites, screen_width, variability)
        #print(doves_list)
        dove_manager.place_doves(doves_list, len(doves_list), screen_width)
        gen_food(food_amount)
        #input("Press Enter for Next Generation")


main()

pygame.quit()
