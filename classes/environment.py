# Import python libraries

import numpy as np
from numpy import genfromtxt
import copy

# Import user defined libraries


class Environment():
    
    structure=np.array([[1,0,0,0,1]])

    def environment_one(self):
        return self.structure
    
    def gen_env_from_csv(self, path):
        return genfromtxt(path , delimiter=',')

    def agent_observations(self, agent_coord_y, agent_coord_x):
        return self.structure[agent_coord_y][agent_coord_x-1], self.structure[agent_coord_y][agent_coord_x+1]
    
    def agent_in_map(self, agent_coord_y, agent_coord_x):
        new = copy.copy(self.structure)
        new[agent_coord_y][agent_coord_x]=2
        return new
    
    