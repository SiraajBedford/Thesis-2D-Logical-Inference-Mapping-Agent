import os
import numpy as np
from numpy import genfromtxt
import turtle
import random
import pygame
import matplotlib.pyplot as plt


# f=open("maps\\example_map.csv",'r')


# print(f.read())



# my_data = genfromtxt('maps\\example_map.csv', delimiter=',')




pygame.init()
gameDisplay = pygame.display.set_mode((500,500))
pygame.display.set_caption("New Window")



clock=pygame.time.Clock()

crashed=False


pygame.draw.rect(gameDisplay,'r',10)

while not crashed:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True
            
        print(event)
        
    pygame.display.update()
    clock.tick(60)

pygame.quit()
quit()
    


