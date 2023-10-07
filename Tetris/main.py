import pygame
import sys
import pygame.locals as pg_locals
from game import Game
from block import *

pygame.init()

screen = pygame.display.set_mode((550,620))
pygame.display.set_caption("Tetris")
icon = pygame.image.load("tetris.png")
pygame.display.set_icon(icon)

title_font = pygame.font.Font(None, 40)
next_surface = title_font.render("Next", True, Colors.yellow)
score_surface = title_font.render("Score", True, Colors.orange)
game_over_surface = title_font.render("GAME OVER", True, Colors.red)
play_again_surface = title_font.render("Play Again", True, Colors.purple)

next_rect = pygame.Rect(345, 55, 170, 180)
score_rect = pygame.Rect(345, 315, 170, 60)
play_again_rect = pygame.Rect(345, 520, 170, 50)

clock = pygame.time.Clock()
game = Game()
GAME_UPDATE = pygame.USEREVENT
pygame.time.set_timer(GAME_UPDATE, 250)

left_pressed = False
right_pressed = False
down_pressed = False
move_time = 0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if game.game_over == True:
                game.game_over = False
                game.reset()
            if event.key == pygame.K_LEFT and game.game_over == False:
                left_pressed = True
            if event.key == pygame.K_RIGHT and game.game_over == False:
                right_pressed = True
            if event.key == pygame.K_DOWN and game.game_over == False:
                down_pressed = True
            if event.key == pygame.K_UP and game.game_over == False:
                game.rotate()
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                left_pressed = False
            if event.key == pygame.K_RIGHT:
                right_pressed = False
            if event.key == pygame.K_DOWN:
                down_pressed = False
        if event.type == GAME_UPDATE and game.game_over == False:
            game.move_down()
        if event.type == pg_locals.MOUSEBUTTONDOWN:
            if game.game_over and play_again_rect.collidepoint(event.pos):
                game.game_over = False
                game.reset()

    current_time = pygame.time.get_ticks()
    if left_pressed and current_time - move_time >= 110:
        game.move_left()
        move_time = current_time
    if right_pressed and current_time - move_time >= 110:
        game.move_right()
        move_time = current_time
    if down_pressed and current_time - move_time >= 110:
        game.move_down()
        game.update_score(0, 1)
        move_time = current_time
        
            
    score_value_surface = title_font.render(str(game.score), True, Colors.white)
    screen.fill(Colors.brunswick_geen)
    screen.blit(next_surface, (400, 20, 50, 50))
    screen.blit(score_surface, (390, 280, 50, 50)) 
    if game.game_over == True:
        screen.blit(game_over_surface, (345, 450, 50, 50))
        pygame.draw.rect(screen, Colors.teal, play_again_rect, 0, 15)
        screen.blit(play_again_surface, play_again_rect.move(15, 15))
    pygame.draw.rect(screen, Colors.teal, score_rect, 0, 15)
    screen.blit(score_value_surface, score_value_surface.get_rect(centerx = score_rect.centerx,
                                                                  centery = score_rect.centery))
    pygame.draw.rect(screen, Colors.teal, next_rect, 0, 15)
    game.draw(screen)
    
    pygame.display.update()
    clock.tick(60)