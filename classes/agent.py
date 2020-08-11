# -*- coding: utf-8 -*-

"""
Maps percepts to actions

Agent program skeletons: they take the current percept as input from the sensors and return an 
action to the actuators.

"""

class Simple_Agent():
    
    def __init__(self, x, obs):
        self.x=x
        self.obs=obs
        
    def move_left(self):
        self.x=self.x-1
        return self.x
    
    def move_right(self):
        self.x=self.x+1
        return self.x
    


class Agent():
    
    # def __init__(self, y_prev, x_prev, y, x, map_now, obs_seq):   
    #     self.x = x
    #     self.y = y
    #     self.x_prev=x_prev
    #     self.y_prev=y_prev
    #     self.map_now = map_now
    #     self.obs_seq=obs_seq
    
    def __init__(self, x, obs):
        self.x=x
        self.obs=obs
        
    
    def initial_agent_state(self):
        #Cannot initially be on surrounding 1s
        self.map_now[self.x][self.y]=2
        return self.map_now
        
        
    def move_right(self):
        #cannot move to a 1-square
        self.y_prev=self.y
        self.x_prev=self.x
        self.y=self.y+1
        
        #if the right most block is open, then move else remain
        return self.y
        
    def move_left(self):
        #cannot move to a 1-square
        self.y_prev=self.y
        self.x_prev=self.x
        self.y=self.y-1
        return self.y
    
    
    def stay_on_square(self):
        
        if self.map_now[self.x][self.y+1]==1:
            self.y=self.y_prev
            self.x=self.x_prev
            
    def observation_sequence(self):
        self.obs_seq[0]=self.map_now[self.x][self.y]
        self.obs_seq[1]=self.map_now[self.x][self.y]
        self.obs_seq[2]=self.map_now[self.x][self.y]
        self.obs_seq[3]=self.map_now[self.x][self.y]
        self.obs_seq[4]=self.map_now[self.x][self.y]
        self.obs_seq[5]=self.map_now[self.x][self.y]
        self.obs_seq[6]=self.map_now[self.x][self.y]
        self.obs_seq[7]=self.map_now[self.x][self.y]
        self.obs_seq[8]=self.map_now[self.x][self.y]
            
  