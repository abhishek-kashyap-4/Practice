# -*- coding: utf-8 -*-
"""
Created on Sun Jan 22 19:31:52 2023

@author: kashy
"""

import pygame
from pygame.locals import *
 
from random import randint
import random
import math
 
def initobjs(nobj,size):
    # nature , x , y speed in x, speed in y
    
    return [ [random.randint(0,4), random.randint(25,size-25),random.randint(25,size-25),randint(0,5),randint(0,5)] for i in range(nobj)]

def naturechange(a,b):
    '''
    0 Rock > 2 , 3
    1 Paper > 0, 4
    2 Scissor > 1, 3
    3 Lizard > 1 , 4
    4 Spock > 0 , 2
    '''
    if(a==0):
        if(b==2 or b==3):
            b = a
        elif(b==1 or b==4):
            a = b
    elif(a==1):
        if(b==0 or b==4):
            b = a
        elif(b==2 or b==3):
            a = b
    elif(a==2):
        if(b==1 or b==3):
            b = a
        elif(b==0 or b==4):
            a = b
    elif(a==3):
        if(b==1 or b==4):
            b = a
        elif(b==0 or b==2):
            a = b
    elif(a==4):
        if(b==0 or b==2):
            b = a
        elif(b==1 or b==3):
            a = b
    return a,b
        
        
def distance(x1,y1,x2,y2):
    if (x1-x2 >20 or x2-x1>20 or y1-y2>20 or y2-y1>20):
        return 100
    return math.sqrt((x1-x2)*(x1-x2) + (y1-y2)*(y1-y2))
    
def update_objs(objs):
    '''
    if any objects are touching, resolve for state change. 
    
    
    '''
    
    for i in range(len(objs)):
        obj = objs[i]
        speed_x = obj[3]
        speed_y = obj[4]
        if(randint(0,30)==0):
            pass
            speed_x = randint(0,2)
            speed_y = 2-speed_x
            speed_x *= random.choice([-1,1])
            speed_y *= random.choice([-1,1])
        
        
        
        if(obj[1] <= 40):
            speed_x =abs(speed_x)
        if(obj[1] >= size -40):
            speed_x  = - abs(speed_x)
            
        if(obj[2] <= 40):
            speed_y = abs(speed_y )
        if(obj[2]>= size - 40):
            speed_y = -abs(speed_y)
          
        objs[i][1] +=speed_x
        objs[i][2] +=speed_y
        objs[i][3] = speed_x
        objs[i][4] = speed_y
    for i in range(len(objs)):
        for j in range(len(objs)):
            a ,x1,y1 ,sx,sy = objs[i]
            b , x2,y2 ,sx,sy = objs[j]
            if (distance(x1,y1,x2,y2)<30):
                objs[i][0] , objs[j][0] = naturechange(a,b)
    return objs
    
    


    
    
    

pygame.init()

speed_x = 2
speed_y = 3
size = 1000
scrn = pygame.display.set_mode((size,size))
picsize = 20
rock = pygame.image.load("rock.jpg").convert()
rock = pygame.transform.scale(rock, (picsize,picsize))
paper = pygame.image.load("paper.jpg").convert()
paper = pygame.transform.scale(paper, (picsize,picsize))
scissor = pygame.image.load("scissor.jpg").convert()
scissor = pygame.transform.scale(scissor, (picsize,picsize))
lizard = pygame.image.load("lizard.jpg").convert()
lizard = pygame.transform.scale(lizard, (picsize,picsize))
spock = pygame.image.load("spock.jpg").convert()
spock = pygame.transform.scale(spock, (picsize,picsize))
translate = [rock,paper,scissor,lizard,spock]
window = pygame.display.set_mode((size,size))
clock = pygame.time.Clock()
direction = 1
    
nobj = 100
objs = initobjs(nobj,size)



     

def displayobjs(objs):
    for obj in objs:
        i ,x ,y ,sx,sy= obj
        imp = translate[i]
        scrn.blit(imp, (x,y))
        
   

run = True
 

while run:
    pygame.event.get()
    
    
    clock.tick(60)
    objs = update_objs(objs)
    displayobjs(objs)
    pygame.display.update()
 
    window.fill((0,0,0))
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            run = False