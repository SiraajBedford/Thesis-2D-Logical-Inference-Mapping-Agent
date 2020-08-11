# Import python libraries
import numpy as np
import time as tm


# Import user defined libraries

from classes.environment import Environment
from classes.agent import Agent
from classes.KB import KBase
from classes.inference import Inference

# Initial state

env=Environment()
agent_coord_y_init=0
agent_coord_x_init=1
agent=Agent(agent_coord_y_init, agent_coord_x_init, env.agent_observations(agent_coord_y_init, agent_coord_x_init))
env.agent_in_map(agent.y, agent.x)

# While-loop for simulation of movement of agent in environment

try:
    while True:  
        env.agent_in_map(agent.y, agent.x)
        print(env.structure)
        tm.sleep(1.00)
        agent.move_right()


except KeyboardInterrupt:
    pass















