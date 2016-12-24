#########################################
# Programmer: Eitan Yehuda
# Date: 17/11/2014
# File Name: pop_the_balloons.py
# Description: This program is a template for a game. It demonstrates use of lists.
#########################################

import time
import pygame
pygame.init()

from math import sqrt                   # only sqrt function is needed from the math module
from random import randint,choice              # only randint function is needed from the random module

HEIGHT = 800
WIDTH  = 1000
game_window=pygame.display.set_mode((WIDTH,HEIGHT))
background = pygame.image.load("2014_happy_birthday.jpg")
background = background.convert_alpha()
background = pygame.transform.scale(background,(WIDTH,HEIGHT))

BLACK = (  0,  0,  0)                   # used colours
RED = ( 255, 0, 0)
GREEN = ( 0, 255, 0)
BLUE = ( 0, 0, 255)
YELLOW = ( 255, 255, 0)
PURPLE = ( 255, 0, 255)
TURQUOISE = ( 0, 255, 255)
outline=0                               # thickness of the shapes' outline

counter = 0                              #pop counter
missed = 0                              #miis counter
timer = 0

CLR = (RED,YELLOW,BLUE,GREEN,PURPLE,TURQUOISE)#



message = "Balloons Popped: "
message2 = "Timer: "
message3 = "Balloons Missed: "
message4 = "GAME OVER"
message5 = "Perfect Score! Great Job"
message6 = "Awesome! You almost got all the balloons"
message7 = "OK... You can do better than that"
message8 = "That was bad! Better luck next time"
message9 = "That was horrible! You need more practice" 
#---------------------------------------#
# function that calculates distance     #
# between two points in coordinate system
#---------------------------------------#
def distance(x1, y1, x2, y2):
    return sqrt((x1-x2)**2 + (y1-y2)**2)# Pythagorean theorem    

#---------------------------------------#
# function that redraws all objects     #
#---------------------------------------#
def redraw_game_window():
    game_window.blit(background, (0,0))
    text = font.render(str(counter), 1, BLACK)
    text2 = font.render(message, 1, BLACK)
    text3 = font.render(str(int(round(timer,0))), 1, BLACK)
    text4 = font.render(message2, 1, BLACK)
    text5 = font.render(str(missed), 1, BLACK)
    text6 = font.render(message3, 1, BLACK)
    game_window.blit(text,(360,0))
    game_window.blit(text2,(0,0))
    game_window.blit(text3,(910,0))
    game_window.blit(text4,(780,0))
    game_window.blit(text5,(350,760))
    game_window.blit(text6,(0,760))
    
                        
    for i in range(40):
        if balloonVisible[i] == True:
            pygame.draw.circle(game_window, balloonCLR[i], (balloonX[i], balloonY[i]), balloonR[i], outline)
                # display must be updated, in order
                                        # to show the drawings

    #endGame
    if balloonVisible == [False]*40:
        game_window.fill(BLACK)
        text7 = font2.render(message4, 1, RED)
        text = font.render(str(counter), 1, BLUE)
        text2 = font.render(message, 1, BLUE)
        game_window.blit(text7,(WIDTH/6,HEIGHT/4))
        game_window.blit(text,(WIDTH/2+140,HEIGHT/2))
        game_window.blit(text2,(WIDTH/6+115,HEIGHT/2))   
        if counter == 40:
            text8 = font.render(message5, 1, YELLOW)
            game_window.blit(text8,(WIDTH/6+80,HEIGHT/2+100))
        elif 40>counter>=30:
            text9 = font.render(message6, 1, YELLOW)
            game_window.blit(text9,(WIDTH/15,HEIGHT/2+100))
        elif 30>counter>=20:
            text10 = font.render(message7, 1, YELLOW)
            game_window.blit(text10,(WIDTH/6,HEIGHT/2+100))
        elif 20>counter>=10:
            text11 = font.render(message8, 1, YELLOW)
            game_window.blit(text11,(WIDTH/7,HEIGHT/2+100))
        else:
            text12 = font.render(message9, 1, YELLOW)
            game_window.blit(text12,(WIDTH/12,HEIGHT/2+100))
    pygame.display.update() 
       
#---------------------------------------#
# the main program begins here          #
#---------------------------------------#
exit_flag = False                       #
balloonR = [0]*40                       # create lists of 20 items each
balloonX = [0]*40                       # for balloons' properties
balloonY = [0]*40                       #
balloonSPEED = [0]*40                   #
balloonCLR = [0,0,0]*40
balloonVisible = [True]*40
for i in range(40):
    balloonX[i] = randint(0, WIDTH)     # initialize the coordinates and the size of the balloons
    balloonY[i] = randint(HEIGHT/2, HEIGHT)
    balloonR[i] = randint(20,50)
    balloonSPEED[i] = randint(3,5)
    balloonCLR[i] = choice(CLR)
    balloonVisible[i] = True
while not exit_flag:                    #
    keys = pygame.key.get_pressed()     #
    for event in pygame.event.get():    # check for any events
        if event.type == pygame.QUIT:   # If user clicked close
            exit_flag = True            # Flag that we are done so we exit this loop
        if keys[pygame.K_ESCAPE]:
            exit_flag = True  
# act upon mouse events
        if event.type == pygame.MOUSEBUTTONDOWN:
            for i in range(40):
                (cursorX,cursorY)=pygame.mouse.get_pos()
                if balloonVisible[i] == True:
                    if distance(cursorX, cursorY, balloonX[i], balloonY[i])< balloonR[i]:
                        balloonVisible[i] = False
                        counter+=1
                        print("Balloons popped: ",counter)
        
    font = pygame.font.SysFont("Ariel Black",60) # create a variable font
    font2 = pygame.font.SysFont("Ariel Black",150) # create a variable font
# move the balloons
    for i in range(40):
        balloonY[i] = balloonY[i] - balloonSPEED[i]
        if balloonVisible[i] == True:
            if balloonY[i]+balloonR[i] < 0:
                missed +=1
                balloonVisible[i]=False
# update the screen    
    redraw_game_window()
    pygame.time.delay(50)
    timer+=0.05
pygame.quit()                           # always quit pygame when done!
