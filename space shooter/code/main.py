import pygame
from os.path import join
from random import randint

#general setup
pygame.init()
WINDOW_WIDTH, WINDOW_HEIGHT = 900, 600
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Space Shooter")
running = True
clock = pygame.time.Clock()


#imports
path = join('images', 'player.png')
player_surf = pygame.image.load(path).convert_alpha()
player_rect = player_surf.get_frect(center = (WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2))
player_dir = pygame.math.Vector2(1, 1)
player_speed = 300

star_surf = pygame.image.load(join('images', 'star.png')).convert_alpha()
star_positions = [(randint(0, WINDOW_WIDTH), randint(0, WINDOW_HEIGHT)) for i in range(20)]

meteor_surf = pygame.image.load(join('images', 'meteor.png')).convert_alpha()
meteor_rect = meteor_surf.get_frect(center = (WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2))

laser_surf = pygame.image.load(join('images', 'laser.png')).convert_alpha()
laser_rect = laser_surf.get_frect(bottomleft = (20, WINDOW_HEIGHT - 20))


while running:
    dt = clock.tick() / 1000

    # event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # draw the game
    
    #Stars
    display_surface.fill('darkgray')
    for pos in star_positions:
        display_surface.blit(star_surf, pos)
        
    #Meteor and laser
    display_surface.blit(meteor_surf, meteor_rect)
    display_surface.blit(laser_surf, laser_rect)
    
    #Player and movement dir
    player_rect.center += player_dir * player_speed * dt
    if player_rect.right >= WINDOW_WIDTH or player_rect.left <= 0:
        player_dir.x *= -1
    if player_rect.bottom >= WINDOW_HEIGHT or player_rect.top <= 0:
        player_dir.y *= -1

    
    display_surface.blit(player_surf, player_rect)
    
    pygame.display.update()
    
pygame.quit()