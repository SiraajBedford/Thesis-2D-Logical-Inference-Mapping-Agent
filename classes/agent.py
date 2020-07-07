# -*- coding: utf-8 -*-

"""
Maps percepts to actions

Agent program skeletons: they take the current percept as input from the sensors and return an 
action to the actuators.

"""
import random as rd



class Agent():
    
    
    def place_agent_in_env(self, current_map, x ,y):
        
        prev_num=current_map[x][y]
        p=current_map
        p[x][y]=2
        #current_map[x][y]=prev_num
        return p, prev_num
        
    def update(self, current_map,prev_num,x,y,x_prev,y_prev):
        m=current_map
        m[x_prev][y_prev]=prev_num
        m[x][y]=2
        current_map=m
        return prev_num,current_map
        