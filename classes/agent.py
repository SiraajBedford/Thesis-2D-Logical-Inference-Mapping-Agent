# Import python libraries



# Import user defined libraries

class Agent():
    
    def __init__(self, y, x, val, obs, y_prev, x_prev, val_prev):
        self.y=y
        self.x=x
        self.val=val
        self.obs=obs
        self.y_prev=y_prev
        self.x_prev=x_prev
        self.val_prev=val_prev
        
        
    def move_left(self):
        self.x=self.x-1
        return self.x
    
    def move_right(self):
        self.val_prev=self.val
        self.x_prev=self.x
        self.y_prev=self.y
        self.x=self.x+1
        
  
    def return_x(self):
        return self.x
    
    def return_y(self):
        return self.y