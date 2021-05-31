#doves class
import pygame
import random

class dove(object):

    global framerate

    def __init__(self, x, y, vel, vision):
        self.vel = vel
        self.vision = vision
        self.energy = 0
        self.x = x
        self.y = y
        self.prev_rand_x = random.randrange(-100, 101)
        self.prev_rand_y = random.randrange(-100, 101)
        self.start = True
        self.sprite = pygame.sprite.Sprite()
        self.sprite.image = pygame.Surface((20, 20), pygame.SRCALPHA)
        pygame.draw.circle(self.sprite.image, (255, 255 - min(255, vel * 20), 255 - min(255, vel * 20)), (10, 10), 10)
        pygame.draw.circle(self.sprite.image, (255, 255, 255), (self.vision, self.vision), self.vision, width=1)

        self.sprite.rect = pygame.Rect(self.x + self.vision, self.y + self.vision, 10, 10)

    def find_closest_food(self, food_sprites):
        pos = pygame.math.Vector2(self.x, self.y)
        closest_food = min([f for f in food_sprites], key=lambda f: pos.distance_to(pygame.math.Vector2(f.rect.center)))
        if (pos.distance_to(pygame.math.Vector2(closest_food.rect.center)) > self.vision):
            return None
        return closest_food

    def move(self, food_sprites):
        if len(food_sprites) <= 0:
            return
        closest_food = self.find_closest_food(food_sprites)
        if (closest_food == None):
            # move_random
            if(self.x < 100):
                self.prev_rand_x += random.randrange(50, 60)
                #TODO make a funciton of screen width
            elif(self.x > 900):
                self.prev_rand_x += random.randrange(-60, -50)
            else:
                self.prev_rand_x += random.randrange(-60, 60)

            if (self.y < 100):
                self.prev_rand_y += random.randrange(50, 60)
                # TODO make a funciton of screen width
            elif (self.y > 900):
                self.prev_rand_y += random.randrange(-60, -50)
            else:
                self.prev_rand_y += random.randrange(-60, 60)

            dir = pygame.math.Vector2(self.prev_rand_x, self.prev_rand_y)
            dir.scale_to_length(self.vel)
            self.x += dir.x
            self.y += dir.y
            self.sprite.rect.center = (self.x, self.y)
            #self.sprite.rect.center = pygame.mouse.get_pos()
        else:
            # move towards closest food
            delx, dely  = closest_food.rect.x - self.x, closest_food.rect.y - self.y
            dir = pygame.math.Vector2(delx, dely)
            dir.scale_to_length(self.vel)
            self.x += dir.x
            self.y += dir.y
            self.sprite.rect.center = (self.x, self.y)
            #self.sprite.rect.center = pygame.mouse.get_pos()
            
        x = pygame.sprite.spritecollide(self.sprite, food_sprites, True, pygame.sprite.collide_circle)
        if len(x) > 0:
            self.energy += 1

    def __str__(self):
        return "Vel: " + str(self.vel) + " Energy: " + str(self.energy) + " x, y "  + str(self.x) + ", " + str(self.y)