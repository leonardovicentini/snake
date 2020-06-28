#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__author__ = "Leonardo Vicentini"
__version__ = "01_01"


import os
import pygame
import random


boold =  False


def contact(lista):
    """
    This function returns a Boolean value True if the last element of the list is also present in other positions.
    :param list: list List to be analyzed.
    :return: bool True if the last element appears multiple times.
    """
    duplicate = False
    for i in range(0, len(lista) -1):
        if lista[i] == lista[-1]:
            if boold: print("Contact in pos: ", i)
            duplicate = True
    
    return duplicate


def random_food_pos(win_width, win_height, food_width, food_height, snake_positions):
    """
    This function returns two x and y positions in which to generate food for the snake to eat.
    :param win_width: int Pixel window width.
    :param win_height: int pixel window height.
    :param food_width: int Pixel width of the food.
    :param food_height: int Pixel height of the food.
    :param snake_position: list List of positions of the squares that make up the snake.
    :return xf: int Position x acceptable for food.
    :return yf int Position y acceptable for food.
    """
    invalid = True

    while invalid:
        
        xf = random.randrange(0, win_width - food_width, food_width)
        yf = random.randrange(0, win_height - food_height, food_height)
        
        if not ([xf, yf] in snake_positions):
            invalid = False

    return xf, yf


if __name__ == "__main__":

    if boold: print("Start main")

    # Initializing pygame variables
    pygame.init()
    sfondo = 0, 0, 0
    snake_color = 0, 200, 0
    food_color = 200, 0, 0
    text_color = 0, 220, 0
    w_width, w_height = 800, 500
    win = pygame.display.set_mode((w_width, w_height))
    big_font = pygame.font.SysFont("comicsans", int(w_width/8), True)
    medium_font = pygame.font.SysFont("comicsans", int(w_width/10))
    small_font = pygame.font.SysFont("comicsans", int(w_width/12))
    pygame.display.set_caption("Snake")
    run = True

    # Game variables
    score = 0
    r_width, r_height = 25, 25
    speed_x, speed_y = r_width, 0
    snake_parts_position = [[0, 0], [25, 0], [50, 0]]
    x_food, y_food = random_food_pos(w_width, w_height, r_width, r_height, snake_parts_position)

    while run:
        
        # Scoreboard
        score_text = small_font.render(f"{score}", 1, text_color)

        # reading input for changing direction by updating 'speed_x' and 'speed_y'
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and speed_x != r_width: speed_x, speed_y = -r_width, 0
        if keys[pygame.K_RIGHT] and  speed_x != -r_width: speed_x, speed_y = r_width, 0
        if keys[pygame.K_UP] and speed_y != r_height: speed_x, speed_y = 0, -r_height
        if keys[pygame.K_DOWN] and speed_y != -r_height: speed_x, speed_y = 0, +r_height
        
        # Updating
        x_new_snake_head = snake_parts_position[-1][0] 
        y_new_snake_head = snake_parts_position[-1][1] 
        x_new_snake_head += speed_x
        y_new_snake_head += speed_y
        if x_new_snake_head != x_food or y_new_snake_head != y_food: snake_parts_position = snake_parts_position[1:]
        snake_parts_position.append([x_new_snake_head, y_new_snake_head])

        # Score assignment
        if x_new_snake_head == x_food and y_new_snake_head == y_food:
            x_food, y_food = random_food_pos(w_width, w_height, r_width, r_height, snake_parts_position)
            score += 1

        # Make sure it doesn't come out of the box
        for i in range(0, len(snake_parts_position)):
            if snake_parts_position[i][0] > (w_width - r_width): snake_parts_position[i][0] = 0
            if snake_parts_position[i][1] > (w_height - r_height): snake_parts_position[i][1] = 0
            if snake_parts_position[i][0] < 0: snake_parts_position[i][0] = w_width
            if snake_parts_position[i][1] < 0: snake_parts_position[i][1] = w_height
        
        if boold: print(f"Snake head position: x = {snake_parts_position[-1][0]} y = {snake_parts_position[-1][1]}\tSnake speed: x = {speed_x} y = {speed_y}\tFood position x = {x_food} y = {y_food}\tSnake parts position = {snake_parts_position}")
        
        if contact(snake_parts_position): run = False

        # Drawing objects
        win.fill(sfondo) 
        win.blit(score_text, (w_width - score_text.get_rect().width, 0))
        for x_part, y_part in snake_parts_position:
            pygame.draw.rect(win, snake_color, (x_part, y_part, r_width, r_height))
        pygame.draw.rect(win, food_color, (x_food, y_food, r_width, r_height))
        
        pygame.display.update() 
        pygame.time.delay(50)

        for event in pygame.event.get():
            if event.type == pygame.QUIT or run == False:
                if boold: print("Showing results...")
                final_score = medium_font.render(f"Score:  {score}", 1, text_color)
                win.fill(sfondo) 
                win.blit(final_score, ((w_width - final_score.get_rect().width)/2, (w_height - final_score.get_rect().height)/2))
                pygame.display.update()
                pygame.time.delay(2000)
                if boold: print("Quitting...")
                run = False

    pygame.quit()

    if boold: print("End main")
