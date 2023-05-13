import pygame
from sys import exit
from random import randint

pygame.init()

screen = pygame.display.set_mode((500,800))
pygame.display.set_caption('SPACE MARAUDERS')
clock = pygame.time.Clock()
game_active = True

def update_player_pos():
    if player_x_mov < 0:
        player_rect.x += player_x_mov * player_speed
    if player_x_mov > 0:
        player_rect.x += player_x_mov * player_speed
    if player_y_mov < 0:
        player_rect.y += player_y_mov * player_speed
    if player_y_mov > 0:
        player_rect.y += player_y_mov * player_speed

def blue_enemy_movement(enemy_list):
    if enemy_list:
        for enemy_rect in enemy_list:
            enemy_rect.y += blue_speed
            screen.blit(blue_surf,enemy_rect)
        
        enemy_list = [enemy for enemy in enemy_list if enemy_rect.y < 900]

        return enemy_list
    else:
        return []

def purple_enemy_movement(enemy_list):
    if enemy_list:
        for enemy_rect in enemy_list:
            enemy_rect.y += purple_speed
            screen.blit(purple_surf,enemy_rect)  
        
        enemy_list = [enemy for enemy in enemy_list if enemy_rect.y < 900]

        return enemy_list
    else:
        return []

def green_enemy_movement(enemy_list):
    if enemy_list:
        for enemy_rect in enemy_list:
            enemy_rect.y += green_speed
            screen.blit(green_surf,enemy_rect)
        
        enemy_list = [enemy for enemy in enemy_list if enemy_rect.y < 900]

        return enemy_list
    else:
        return []

# def collisions()

### SURFACES ###
background_surf = pygame.image.load('graphics/background.png').convert_alpha()
background_pos = -800

# PLAYER
player_surf = pygame.image.load('graphics/player.png').convert_alpha()
player_rect = player_surf.get_rect(midbottom = (250,700))
player_x_mov = 0
player_y_mov = 0
player_speed = 3

# ENEMY
blue_surf = pygame.image.load('graphics/enemyblue.png').convert_alpha()
purple_surf = pygame.image.load('graphics/enemypurple.png').convert_alpha()
green_surf = pygame.image.load('graphics/enemygreen.png').convert_alpha()
blue_speed = 3
purple_speed = 5
green_speed = 2

blue_enemy_rect_list = []
purple_enemy_rect_list = []
green_enemy_rect_list = []

# GAME OVER
gameover_surf = pygame.image.load('graphics/gameover.png').convert_alpha()

# TIMERS
enemy_timer = pygame.USEREVENT + 1
pygame.time.set_timer(enemy_timer,1000)

# GAMEPLAY LOOP
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if game_active:
            if event.type == pygame.KEYDOWN:
                if event.key == ord('a'):
                    player_x_mov = -1
                if event.key == ord('d'):
                    player_x_mov = 1
                if event.key == ord('w'):
                    player_y_mov = -1
                if event.key == ord('s'):
                    player_y_mov = 1
            if event.type == pygame.KEYUP:
                if event.key == ord('a'):
                    player_x_mov = 0
                if event.key == ord('d'):
                    player_x_mov = 0
                if event.key == ord('w'):
                    player_y_mov = 0
                if event.key == ord('s'):
                    player_y_mov = 0

            if event.type == enemy_timer:
                spawn = randint(0,3)
                if spawn == 0:    
                    blue_enemy_rect_list.append(blue_surf.get_rect(midbottom = ((randint(40,460)), ((randint(-95,-35))))))
                if spawn == 1:
                    purple_enemy_rect_list.append(purple_surf.get_rect(midbottom = ((randint(40,460)), ((randint(-95,-35))))))
                if spawn == 2:
                    green_enemy_rect_list.append(green_surf.get_rect(midbottom = ((randint(40,460)), ((randint(-95,-35))))))


    if game_active:
        # SCROLLING BACKGROUND
        screen.blit(background_surf,(0,background_pos))
        background_pos += 20
        if background_pos > 0:
            background_pos = -800

        # PLAYER
        update_player_pos()
        screen.blit(player_surf,player_rect)

        # ENEMY
        blue_enemy_rect_list = blue_enemy_movement(blue_enemy_rect_list)
        purple_enemy_rect_list = purple_enemy_movement(purple_enemy_rect_list)
        green_enemy_rect_list = green_enemy_movement(green_enemy_rect_list)
    
    pygame.display.update()
    clock.tick(60)