#doves class
import pygame

class dove(object):

    global framerate

    def __init__(self, x, y, vel):
        self.vel = vel
        self.energy = 0
        self.x = x
        self.y = y
        self.start = True
        self.sprite = pygame.sprite.Sprite()
        self.sprite.image = pygame.Surface((20, 20), pygame.SRCALPHA)
        pygame.draw.circle(self.sprite.image, (50, 10, 255), (10, 10), 10)
        self.sprite.rect = pygame.Rect(self.x, self.y, 10, 10)

    def find_closest_food(self, food_sprites):
        global food_list
        pos = pygame.math.Vector2(self.x, self.y)
        closest_food = min([f for f in food_sprites], key=lambda f: pos.distance_to(pygame.math.Vector2(f.rect.center)))
        return closest_food

    def move(self, food_sprites):
        if len(food_sprites) <= 0:
            return
        closest_food = self.find_closest_food(food_sprites)
        delx, dely  = closest_food.rect.x - self.x, closest_food.rect.y - self.y
        dir = pygame.math.Vector2(delx, dely)
        dir.scale_to_length(self.vel)
        self.x += dir.x
        self.y += dir.y
        self.sprite.rect.center = (self.x, self.y)
        #self.sprite.rect.center = (pygame.mouse.get_pos())
        x = pygame.sprite.spritecollide(self.sprite, food_sprites, True, pygame.sprite.collide_circle)
        if len(x) > 0:
            self.energy += 1

    def __str__(self):
        return "Vel: " + str(self.vel) + " Energy: " + str(self.energy) + " x, y "  + str(self.x) + ", " + str(self.y)