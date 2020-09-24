# 3 main goals

Add propositional logic between functional layers
Add learning for grouping and splitting states
Add ability to construct depependancy graphs

# Setting up the movement

Fix action matrix

# Creator: S. Bedford (21093741@sun.ac.za)
# Project Topic: "Learning the structure of an agent's environment from experience"
# "agent.py" - Agent and robot implementation


# Import python libraries
import numpy as np

# Global variables
open_block=1
not_open_block=0
open_block_1=1
not_open_block_1=0
################
left_obs=0
left_percept=0
################
right_obs=1
right_percept=1
################
up_obs=2
up_percept=2
################
upper_left_obs=3
upper_left_percept=3
################
upper_right_obs=4
upper_right_percept=4
################
bottom_obs=5
bottom_percept=5
################
bottom_left_obs=6
bottom_left_percept=6
################
bottom_right_obs=7
bottom_right_percept=7


# Import user defined libraries

class Agent_physical():
    
    ####################################################################################
    # Agent sensor initialization
    ####################################################################################
    
    def __init__(self, y, x, val, obs, y_prev, x_prev, val_prev,x_max,x_min,y_max,y_min,t):
        self.y=y
        self.x=x
        self.val=val
        self.obs=obs
        self.y_prev=y_prev
        self.x_prev=x_prev
        self.val_prev=val_prev
        self.x_max=x_max
        self.x_min=x_min
        self.y_max=y_max
        self.y_min=y_min
        self.random_move=0
        self.percepts_at_t=np.array([0,0,0,0,0,0,0,0])
        self.actions_at_t=np.array([0,0,0,0,0])
        self.action_history=[]
        self.t=t
        
        
   
    
    ################        
    # Vision sensor    
    ################
                      
    def print_obs(self):
        print("Observations of agent:")
        print((self.obs))
        
    def perceived_left_open_at_t(self):#
        if self.obs[left_obs] == not_open_block: # left block of agent is not open
            self.percepts_at_t[left_percept] = not_open_block
        if self.obs[left_obs] == open_block: # left block of agent is open
            self.percepts_at_t[left_percept] = open_block
            

    def perceived_right_open_at_t(self):#
        if self.obs[right_obs] == not_open_block: # right block of agent is not open
            self.percepts_at_t[right_percept] = not_open_block_1
        if self.obs[right_obs] == open_block: # right left block of agent is open
            self.percepts_at_t[right_percept] = open_block_1


    def perceived_up_at_t(self):#
        if self.obs[up_obs] == not_open_block: # upper block of agent is not open
            self.percepts_at_t[up_percept] = not_open_block_1
        if self.obs[up_obs] == open_block: # upper block of agent is open
            self.percepts_at_t[up_percept] = open_block_1


    def perceived_upper_left_at_t(self):#
        if self.obs[upper_left_obs] == not_open_block: # upper left block of agent is not open
            self.percepts_at_t[upper_left_percept] = not_open_block_1
        if self.obs[upper_left_obs] == open_block: # upper left block of agent is open
            self.percepts_at_t[upper_left_percept] = open_block_1


    def perceived_upper_right_at_t(self):#
        if self.obs[upper_right_obs] == not_open_block: # upper right block of agent is not open
            self.percepts_at_t[upper_right_percept] = not_open_block_1
        if self.obs[upper_right_obs] == open_block: # upper right block of agent is open
            self.percepts_at_t[upper_right_percept] = open_block_1

    
    def perceived_bottom_at_t(self):#
        if self.obs[bottom_obs] == not_open_block: # bottom block of agent is not open
            self.percepts_at_t[bottom_percept] = not_open_block_1
        if self.obs[bottom_obs] == open_block: # bottom block of agent is open
            self.percepts_at_t[bottom_percept] = open_block_1


    def perceived_bottom_left_at_t(self):#
        if self.obs[bottom_left_obs] == not_open_block: # bottom left block of agent is not open
            self.percepts_at_t[bottom_left_percept] = not_open_block_1
        if self.obs[bottom_left_obs] == open_block: # bottom block of agent is open
            self.percepts_at_t[bottom_left_percept] = open_block_1

    def perceived_bottom_right_at_t(self):#
        if self.obs[bottom_right_obs] == not_open_block: # bottom rightblock of agent is not open
            self.percepts_at_t[bottom_right_percept] = not_open_block_1
        if self.obs[bottom_right_obs] == open_block: # bottom block of agent is open
            self.percepts_at_t[bottom_right_percept] = open_block_1
    

    def perceived_at_t(self):
        self.perceived_left_open_at_t()
        self.perceived_right_open_at_t()
        self.perceived_up_at_t()
        self.perceived_upper_left_at_t()
        self.perceived_upper_right_at_t()
        self.perceived_bottom_at_t()
        self.perceived_bottom_left_at_t()
        self.perceived_bottom_right_at_t()
        

            
    def update_percepts(self):  
        self.perceived_at_t()
        
    def update_actions(self):  
        self.actions_performed_at_t()
        
    def return_percepts(self):
        return self.percepts_at_t()
    
    def return_actions(self):
        return self.actions_at_t()
        
        
    def reset_actions_and_percepts(self):
        self.actions_at_t=np.array([0,0,0,0,0])
        self.percepts_at_t=np.array([0,0,0,0,0,0,0,0])
    
    def print_percepts_array(self):
        #print("Percept matrix: %s (left_open,right_open,up_open,upper_left_open,upper_right_open,bottom_open,bottom_left_open,bottom_right_open) (%d-yes, %d-no))" %( np.array2string(self.percepts_at_t, separator=','),op,not_op ))
        #print("Percept matrix: %s [l,r,u,u_l,u_r,b,b_l,b_r] (open_block=1,not_open_block=0))" %( np.array2string(self.percepts_at_t, separator=',')))
        print("Percept top:    %d %d %d  [upper_left, uppper, upper_right]" %( self.percepts_at_t[upper_left_percept],self.percepts_at_t[up_percept],self.percepts_at_t[upper_right_percept]   ))
        print("Percept middle: %d 2 %d  [left,Agent_in_Environment,right]" %( self.percepts_at_t[left_percept],self.percepts_at_t[right_percept]   ))
        print("Percept bottom: %d %d %d  [bottom_left,bottom,bottom_right]" %( self.percepts_at_t[bottom_left_percept],self.percepts_at_t[bottom_percept],self.percepts_at_t[bottom_right_percept]   ))
     
    ####################################################################################
    # RULES for the robot the agent controls in the environment
    ####################################################################################
    
    def move(self): # agent moves randomly
        self.random_move=np.random.randint(4) # 0-left, 1-right, 2-up, 3-down
        
        if self.random_move == 0:
            self.move_left()
        if self.random_move == 1:
            self.move_right()
        if self.random_move == 2:
            self.move_up()
        if self.random_move == 3:
            self.move_down()
    
    def print_move(self):
        if self.random_move == 0:
            print("Moved = %d (left)" %(self.random_move))
        if self.random_move == 1:
            print("Moved = %d (right)" %(self.random_move))
        if self.random_move == 2:
            print("Moved = %d (up)" %(self.random_move))
        if self.random_move == 3:
            print("Moved = %d (down)" %(self.random_move))
           
            
    ##################
    # Move Logic
    ##################
            
    def move_left(self): # Control action by user input for moving left 
        self.action_history.extend('l')
        self.t=self.t+1  
        if self.obs[left_obs] == 1 and self.action_history[self.t-1] == 'l': # If space to left is not open
            self.x_prev=self.x
        else:
            self.val_prev=self.val
            self.x_prev=self.x
            self.y_prev=self.y
            self.x=self.x-1
                        
    def move_right(self): # Control action by user input for moving right 
        self.action_history.extend('r')
        self.t=self.t+1
        if self.obs[right_obs] == 1 and self.action_history[self.t-1] == 'r': # If space to right is not open
           self.x_prev=self.x
        else:
            self.val_prev=self.val
            self.x_prev=self.x
            self.y_prev=self.y
            self.x=self.x+1

    def move_up(self): # Control action by user input for moving right 
        self.action_history.extend('u')
        self.t=self.t+1
        if self.obs[up_obs] == 1 and self.action_history[self.t-1] == 'u': # If space to bottom is not open
           self.y_prev=self.y
        else:
            self.val_prev=self.val
            self.x_prev=self.x
            self.y_prev=self.y
            self.y=self.y-1
            
    def move_down(self): # Control action by user input for moving right 
        self.action_history.extend('d')
        self.t=self.t+1
        if self.obs[bottom_obs] == 1 and self.action_history[self.t-1] == 'd': # If space to bottom is not open
           self.y_prev=self.y
        else:
            self.val_prev=self.val
            self.x_prev=self.x
            self.y_prev=self.y
            self.y=self.y+1
            
    ####################################################################################
    # Robot sensor implmentation
    ####################################################################################
        
    ################
    # Action sensor  
    ################         
            
    def moved_left_at_t(self): # left move stored in self.actions_at_t[0]
        
        if self.x == self.x_prev-1 or (self.action_history[self.t-1] == 'l' and self.x == self.x_prev and self.y == self.y_prev): # agent moved left
            self.actions_at_t[0] = 1
        else:
            self.actions_at_t[0] = 0  
            
    def moved_right_at_t(self): # right move stored in self.actions_at_t[1]
        if self.x == self.x_prev+1 or (self.action_history[self.t-1] == 'r' and self.x == self.x_prev and self.y == self.y_prev):# agent moved right
            self.actions_at_t[1] = 1
        else:
            self.actions_at_t[1] = 0  
            
    def moved_up_at_t(self): # up move stored in self.actions_at_t[2]
        if self.y == self.y_prev-1 or (self.action_history[self.t-1] == 'u' and self.x == self.x_prev and self.y == self.y_prev): # agent moved up
            self.actions_at_t[2] = 1
        else:
            self.actions_at_t[2] = 0     
            
    def moved_down_at_t(self): # down move stored in self.actions_at_t[3]
        if self.y == self.y_prev+1 or (self.action_history[self.t-1] == 'd' and self.x == self.x_prev and self.y == self.y_prev): # agent moved down
            self.actions_at_t[3] = 1
        else:
            self.actions_at_t[3] = 0    
            
    def bumped_at_t(self):# 
        if (self.x == self.x_prev and self.y == self.y_prev): # bump move stored in self.actions_at_t[4]
            self.actions_at_t[4] = 1
        # if self.x != self.x_prev or self.y != self.y_prev:
        else:
            self.actions_at_t[4] = 0  
            
    def actions_performed_at_t(self):
        self.moved_left_at_t()
        self.moved_right_at_t()
        self.moved_up_at_t()
        self.moved_down_at_t()
        self.bumped_at_t()
            
    def print_actions_array(self):
        print("Actions matrix: %s (moved_left, moved_right, moved_up, moved_down, bumped) (1-yes, 0-no))" %( np.array2string(self.actions_at_t, separator=',')))
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            

            
            