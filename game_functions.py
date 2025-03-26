import pygame
import sys
import random
from bubble import Bubble 

ADDBUBBLE = pygame.USEREVENT + 1

def check_events(game_settings, screen, player, bubbles, stats, play_button):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                player.moving_right = True
            if event.key == pygame.K_LEFT:
                player.moving_left = True
            if event.key == pygame.K_UP:
                player.moving_up = True
            if event.key == pygame.K_DOWN:
                player.moving_down = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                player.moving_right = False
            if event.key == pygame.K_LEFT:
                player.moving_left = False
            if event.key == pygame.K_UP:
                player.moving_up = False
            if event.key == pygame.K_DOWN:
                player.moving_down = False
        elif event.type == ADDBUBBLE:
            create_bubble(game_settings, screen, bubbles)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_play_button(stats, play_button, mouse_x, mouse_y)

def check_play_button(stats, play_button, mouse_x, mouse_y):
    if play_button.rect.collidepoint(mouse_x, mouse_y):
        stats.game_active = True

def create_bubble(game_settings, screen, bubbles):
    new_bubble = Bubble(screen, game_settings)
    bubbles.add(new_bubble)

def update_bubbles(player, bubbles, stats, sb, gm_settings):
    for bubble in bubbles:
        if bubble.rect.colliderect(player.rect):
            bubbles.remove(bubble)
            stats.score += bubble.bubble_radius 
            if (int(stats.score / gm_settings.bonus_score)) > stats.bonus:
                stats.level += 1
                sb.prepare_level()
                stats.bonus += 1
                bubble.kill() 

def update_screen(game_settings, screen, player, bubbles, clock, stats, play_button, sb):
    screen.fill(game_settings.bg_color)
    
    player.blit_me()
    
    for bubble in bubbles:
        bubble.blit_me()
     
    sb.draw_score()
     
    clock.tick(30)
    
    if not stats.game_active:
        play_button.draw_button()
    
    pygame.display.flip()

def setup_timers():
    pygame.time.set_timer(ADDBUBBLE, 250)