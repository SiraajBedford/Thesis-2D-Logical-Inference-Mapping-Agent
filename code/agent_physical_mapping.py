# Creator: S. Bedford (21093741@sun.ac.za)
# Project Topic: "Learning the structure of an agent's environment from experience"
# "agent.py" - Agent and robot implementation


# Import python libraries
import numpy as np

# Import user defined libraries

class Agent_physical():
    
    ####################################################################################
    # Agent sensor initialization
    ####################################################################################
    
    def __init__(self, y, x, val, obs, y_prev, x_prev, val_prev,x_max,x_min):
        self.y=y
        self.x=x
        self.val=val
        self.obs=obs
        self.y_prev=y_prev
        self.x_prev=x_prev
        self.val_prev=val_prev
        self.x_max=x_max
        self.x_min=x_min
        self.random_move=0
        self.percepts_at_t=np.array([0,0,0,0,0])
     
        
        
    ####################################################################################
    # Robot sensor implmentation
    ####################################################################################
        
            
    def perceived_left_open_at_t(self):#
        if self.obs[0] == 1: # left block of agent is not open
            self.percepts_at_t[0] = 0
            
        if self.obs[0] == 0: # left block of agent is open
            self.percepts_at_t[0] = 1
            
    def perceived_right_open_at_t(self):#
        if self.obs[1] == 1: # right block of agent is not open
            self.percepts_at_t[1] = 0
            
        if self.obs[1] == 0: # right block of agent is open
            self.percepts_at_t[1] = 1
            
    # Quines for state enumeration       
            
    def perceived_move_left_at_t(self):#
        if self.x == self.x_prev-1: # agent moved left
            self.percepts_at_t[2] = 1
            
        else:
            self.percepts_at_t[2] = 0  
            
    def perceived_move_right_at_t(self):#
        if self.x == self.x_prev+1: # agent moved right
            self.percepts_at_t[3] = 1
            
        else:
            self.percepts_at_t[3] = 0
    
    
    def perceived_bump_at_t(self):#
        if self.x == self.x_prev: # agent bumped into wall
            self.percepts_at_t[4] = 1
            
        else:
            self.percepts_at_t[4] = 0  
            
            
            
    def perform_perceive_functions(self):
        self.perceived_left_open_at_t()
        self.perceived_right_open_at_t()
        self.perceived_move_left_at_t()
        self.perceived_move_right_at_t()
        self.perceived_bump_at_t()
        
    def return_percepts(self):
        return self.percepts_at_t
        
        
    def reset_percept_matrix(self):
        self.percepts_at_t=np.array([0,0,0,0,0])
    
    def print_percepts_array(self):
        print("Percept matrix: %s (left open,right open,moved left,moved right,bumped) (1-yes, 0-no))" %( np.array2string(self.percepts_at_t, separator=',') ))
    
    
    ####################################################################################
    # RULES for the robot the agent controls in the environment
    ####################################################################################
    
    def move(self): # agent moves randomly
        
        self.random_move=np.random.randint(2) #1-right, 0-left
        
        if self.random_move == 1:
            print("Random next move= %d (right)" %(self.random_move))
            
        if self.random_move == 0:
            print("Random next move= %d (left)" %(self.random_move))
        
        if(self.random_move == 1):#right
            if self.x == self.x_max: # If space to right is not open
               self.x_prev=self.x
               pass           
    
            else:
                self.val_prev=self.val
                self.x_prev=self.x
                self.y_prev=self.y
                self.x=self.x+1
        
        if(self.random_move == 0):#left
            if self.x == self.x_min: # If space to left is not open
                self.x_prev=self.x
                pass
            
            else:
                self.val_prev=self.val
                self.x_prev=self.x
                self.y_prev=self.y
                self.x=self.x-1

                
    def move_right(self): # Control action by user input for moving right 
        
        if self.x == self.x_max: # If space to right is not open
           self.x_prev=self.x
           pass           

        else:
            
            self.val_prev=self.val
            self.x_prev=self.x
            self.y_prev=self.y
            self.x=self.x+1
            
            
    def move_left(self): # Control action by user input for moving left 
            
        if self.x == self.x_min: # If space to left is not open
            self.x_prev=self.x
            pass
        
        else:
            self.val_prev=self.val
            self.x_prev=self.x
            self.y_prev=self.y
            self.x=self.x-1