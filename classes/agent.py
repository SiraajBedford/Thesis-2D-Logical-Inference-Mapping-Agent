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
            
    def move(self):
        
        self.random_move=np.random.randint(2) #1-right, 0-left
        print("Random next move= %d" %(self.random_move))
        
        if(self.random_move == 1):#right
            
            if self.x == self.x_max: # If space to left is not open
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
                
    def random_return(self):
        return self.random_move