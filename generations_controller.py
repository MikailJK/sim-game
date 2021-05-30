#runs each generation
import pygame

pygame.init()

win = pygame.display.set_mode((800, 800))
pygame.display.set_caption("Sim")

clock = pygame.time.Clock()
framerate = 30

successful_doves = []

def run_gen(dove_list, dove_sprites, food_sprites):
    global successful_doves
    run = True
    while len(food_sprites) > 0 and len(dove_list) > 0:
        clock.tick(framerate)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        win.fill((0, 0, 0))


        for d in dove_list:
            d.move(food_sprites)
            if d.energy == 1 and d not in successful_doves:
                successful_doves.append(d)
            if d.energy >= 2:
                dove_list.remove(d)
                dove_sprites.remove(d)


        dove_sprites.draw(win)
        food_sprites.draw(win)

        pygame.display.update()

    return successful_doves