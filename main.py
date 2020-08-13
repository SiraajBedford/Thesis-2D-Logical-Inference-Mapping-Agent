# Import python libraries
import numpy as np
import time as tm


# Import user defined libraries

from classes.environment import Environment
from classes.agent import Agent

# To implement

# from classes.KB import KBase
# from classes.inference import Inference

# While-loop timeout

timeout = tm.time() + 4*1   # 5 minutes from now

## Initial state

# Create environment
env=Environment()

# Create agent with default values
agent_coord_y_init_prev=1000
agent_coord_x_init_prev=1000
val_prev_init=1000

agent_coord_y_init=0
agent_coord_x_init=1
agent_val_init=0

agent=Agent(agent_coord_y_init, 
            agent_coord_x_init, 
            agent_val_init, env.agent_observations(agent_coord_y_init, agent_coord_x_init), 
            agent_coord_y_init_prev, agent_coord_x_init_prev, 
            val_prev_init)

# Environment without agent
print(env.structure)

# Place agent in evironment, must update agent value - Agent has value of 7 after initial step
agent.val_prev=agent.val
agent.val=7
env.agent_in_map(agent.y, agent.x, agent.val)



# Run one left or right action

run_once = 0

# While-loop for simulation of movement of agent in environment

try:
    while True:  
        
        # Timing for debug
        test = 0
        if test == 5 or tm.time() > timeout:
            break
        test = test - 1
            
        # Debug Information
        print()
        print("Observations: left=%d, right=%d" % env.agent_observations(agent_coord_y_init, agent_coord_x_init) )
        print("Agent curent position:   y=%d, x=%d, value=%d" %(agent.y, agent.x, agent.val))
        print("Agent previous position: y=%d, x=%d, prev_val=%d" %(agent.y_prev, agent.x_prev, agent.val_prev))
        
        print(env.structure)
        tm.sleep(1.00)
        
        # # Place agent in evironment, must update agent value - Agent has value of 7 after initial step
        # agent.val_prev=agent.val
        # agent.val=7
        # env.agent_in_map(agent.y, agent.x, agent.val)
        
        # Agent position control when active and agent value updates 
        # if agent.move_left or agent.move_right:
        #     agent.prev_val=agent.val
        
        
        
        # if run_once == 0:
            
        #     agent.move_right()
        #     agent.move_right()
        #     env.write_val_map(agent.y_prev, agent.x_prev, agent.val_prev)
        #     run_once=1
        
        
        
        # Agent moving through environment
        
except KeyboardInterrupt:
    pass















