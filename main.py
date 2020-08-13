# Import python libraries
import numpy as np
import time as tm


# Import user defined libraries

from classes.environment import Environment
from classes.agent import Agent

# To implement

# from classes.KB import KBase
# from classes.inference import Inference

# Initial state

env=Environment()

agent_coord_y_init_prev=0
agent_coord_x_init_prev=0
val_prev_init=1

agent_coord_y_init=0
agent_coord_x_init=1
agent_val_init=7

agent=Agent(agent_coord_y_init, agent_coord_x_init, agent_val_init, env.agent_observations(agent_coord_y_init, agent_coord_x_init), agent_coord_y_init_prev, agent_coord_x_init_prev, val_prev_init)
#env.agent_in_map(agent.y, agent.x)

# While-loop for simulation of movement of agent in environment

try:
    while True:  
        
        # Debug Information
        print()
        print("Observations: left=%d, right=%d" % env.agent_observations(agent_coord_y_init, agent_coord_x_init) )
        print("Curent position: y=%d, x=%d, value=%d" %(agent.y, agent.x, agent.val))
        print("Previous: y=%d, x=%d, prev_val=%d" %(agent.y_prev, agent.x_prev, agent.val_prev))
        
        # Agent moving through environment
        env.agent_in_map(agent.y, agent.x)
        print(env.structure)
        tm.sleep(1.00)
        # Actions
        agent.move_right()
        
        
        


except KeyboardInterrupt:
    pass















