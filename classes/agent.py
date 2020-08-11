# Import python libraries



# Import user defined libraries

class Agent():
    
    def __init__(self, y, x, obs):
        self.x=x
        self.y=y
        self.obs=obs
        
    def move_left(self):
        self.x=self.x-1
        return self.x
    
    def move_right(self):
        self.x=self.x+1
        return self.x
  
    def return_x(self):
        return self.x
    
    def return_y(self):
        return self.y