# Import python libraries
import numpy as np

# Import user defined libraries

class Agent():
    
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
        
        
    def reset_percept_matrix(self):
        self.percepts_at_t=np.array([0,0,0,0,0])
    
    def print_percepts_array(self):
        print("Percept matrix: %s (left open,right open,moved left,moved right,bumped) (1-yes, 0-no))" %( np.array2string(self.percepts_at_t, separator=',') ))
        
    def KB_Agent(self, percept):
        
        """The details of the representation language are hidden inside three functions that imple-
        ment the interface between the sensors and actuators on one side and the core representation
        and reasoning system on the other. M AKE -P ERCEPT -S ENTENCE constructs a sentence as-
        serting that the agent perceived the given percept at the given time. M AKE -A CTION -Q UERY
        constructs a sentence that asks what action should be done at the current time. Finally,
        M AKE -A CTION -S ENTENCE constructs a sentence asserting that the chosen action was ex-
        ecuted. The details of the inference mechanisms are hidden inside T ELL and A SK . Later
        sections will reveal these details."""
        
        
        # Persistent: A knowledge base, may contain some background knowledge
        # Persistent: t, a counter initially zero
        
        # Tell and Ask may involve INFERENCE
        
        # Tell(KB, MAKE-PERCEPT-SENTENCE(percept, t))
        # MAKE-PERCEPT-SENTENCE(percept, t)
        
        
        # action = Ask(KB, MAKE-ACTION-QUERY(t))
        
        
        # Tell(KB, MAKE-ACTION-SENTENCE(action, t))
        
        
        
        # t=t+1
        # return action 
        pass
    
    
    def MAKE_PERCEPT_SENTENCE(self, percept, t):
        pass
    
    
    def MAKE_ACTION_QUERY(self, t):
        pass
    
    
    def MAKE_ACTION_SENTENCE(action, t):
        pass
        
    def move(self):
        
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

                
    def move_right(self):
        if self.x == self.x_max: # If space to right is not open
           self.x_prev=self.x
           pass           

        else:
            
            self.val_prev=self.val
            self.x_prev=self.x
            self.y_prev=self.y
            self.x=self.x+1
            
    def move_left(self):
            
        if self.x == self.x_min: # If space to left is not open
            self.x_prev=self.x
            pass
        
        else:
            self.val_prev=self.val
            self.x_prev=self.x
            self.y_prev=self.y
            self.x=self.x-1

                
    def random_return(self):
        return self.random_move