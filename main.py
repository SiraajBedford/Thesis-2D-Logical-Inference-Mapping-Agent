import numpy as np
from numpy import genfromtxt
import pygame
import random as rd
import time as tm

from classes.environment import Environment
from classes.agent import Agent

env=Environment()
agent=Agent()

my_map_1=env.gen_env_from_csv("maps/example_map_case_2.csv")

cnt=0
my_map_1, previous=agent.place_agent_in_env(my_map_1,rd.randint(0, 4),rd.randint(0, 4))

for i in range(0,5):
    print("Hello")



# try:
#     while True:
#
#         print(my_map_1)
#         tm.sleep(1.00)
#
#         num1=rd.randint(0, 4)
#         num2=rd.randint(0, 4)
#
#         num3=rd.randint(0, 4)
#         num4=rd.randint(0, 4)
#
#         if cnt==0: my_map_1,prev_num=agent.update(my_map_1, previous,num3,num4,num1,num2)
#         # if cnt>=1: my_map_1,prev_num=agent.update(my_map_1, prev_num,num3,num4,num1,num2)
#
#         # print(cnt,previous,num1,num2)
#         # cnt+=1
#
# except KeyboardInterrupt:
#     pass
