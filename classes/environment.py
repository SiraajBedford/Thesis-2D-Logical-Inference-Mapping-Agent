# Import python libraries
import numpy as np
from numpy import genfromtxt
import copy
import matplotlib.pyplot as plt

# Import user defined libraries

class Environment():
    
    def __init__(self, input_env):
        self.structure=input_env
        self.ref_array=copy.deepcopy(input_env)#Constant reference array

    def environment_one(self):
        return self.structure   
    
    def gen_env_from_csv(self, path):
        return genfromtxt(path , delimiter=',')

    def agent_observations(self, agent_coord_y, agent_coord_x):
        return self.ref_array[agent_coord_y][agent_coord_x-1], self.ref_array[agent_coord_y][agent_coord_x+1]
    
    def agent_in_map(self, agent_coord_y, agent_coord_x, agent_val, agent_coord_y_prev, agent_coord_x_prev, agent_val_prev):

        self.structure[agent_coord_y_prev][agent_coord_x_prev]=self.ref_array[agent_coord_y_prev][agent_coord_x_prev]
        self.structure[agent_coord_y][agent_coord_x]=agent_val
        
        
    def agent_in_map_static(self, agent_coord_y, agent_coord_x, agent_val, agent_coord_y_prev, agent_coord_x_prev, agent_val_prev):

        self.structure[agent_coord_y_prev][agent_coord_x_prev]=0
        self.structure[agent_coord_y][agent_coord_x]=agent_val
        
    def print_env_structure(self):
        print("Current World: %s" %( np.array2string(self.structure, separator=',') ))
    
    def copy(self):
        return copy.deepcopy(self)
    
    def write_val_map(self, env_coord_y, env_coord_x, prev_agent_val):
        self.structure[env_coord_y][env_coord_x]=prev_agent_val
        
    def plot(self):
        plt.rcParams['figure.figsize']=(0.1,0.1)
        plt.matshow(self.structure, cmap='gray')
        plt.show()