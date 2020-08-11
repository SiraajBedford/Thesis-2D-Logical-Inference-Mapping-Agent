import numpy as np
from numpy import genfromtxt
import pygame
import random as rd
import time as tm

from classes.environment import Environment
from classes.agent import Simple_Agent

env=Environment()
my_map_1=env.gen_env_from_csv("maps/first_map.csv")
#agent=Simple_Agent(1,1,1,1,my_map_1,init_obs_seq)

try:
    while True:  
        print(my_map_1)
        tm.sleep(1)


except KeyboardInterrupt:
    pass















