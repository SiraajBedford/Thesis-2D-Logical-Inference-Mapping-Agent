# Creator: S. Bedford (21093741@sun.ac.za)
# Project Topic: "Learning the structure of an agent's environment from experience"
# "main.py" - File for implementing agent-controlled entity in environment with learning
   
def print_debug():
    print("Observations: left=%d, right=%d" % env.agent_observations(agent_coord_y_init, agent_coord_x_init))
    print("Agent curent position:   y=%d, x=%d" %(agent.y, agent.x))
    print("Agent previous position: y=%d, x=%d" %(agent.y_prev, agent.x_prev))
    print(env.structure)
    print()
    if draw == 1: env.plot()
        
# Import python libraries
import numpy as np # For manipulating arrays
import time as tm # To control simulation time

# Import user defined libraries
from environment_mapping import Environment
from agent_physical_mapping import Agent_physical

# Initial state
t_global=0

# # Create a knowledge base for the agent
# kb=PropKB()

# # Create mapping agent
# agent_1=KBAgentProgram()

# Create environment
sim_mode = 1 # Scale from 1 to 10 on the length of the map
draw = 1 # 1-yes, 0-no
loop_timeout = tm.time() + 1 * 6000  # While-loop timeout
sleep_time = 1 # In seconds, how often debugging information is reported
print_debug_info = 1 # 1-yes, 0-no
agent_moving_random = 1 # 1-yes, 0-no
agent_moving_given = 0 # 1-yes, 0-no

if sim_mode == 1: 
    sim_env=np.array([[1,0,0,0,1]])
    # Future implementation - np.where(sim_env==1)
    env=Environment(sim_env)
    max_x=np.shape(sim_env)[1]-2
    min_x=np.shape(sim_env)[0]

# Create physical agent with default values
agent_coord_y_init_prev=0
agent_coord_x_init_prev=0
val_prev_init=0
agent_coord_y_init=0
agent_coord_x_init=(max_x-min_x)//2+1
agent_val_init=0
agent=Agent_physical(agent_coord_y_init,
            agent_coord_x_init,
            agent_val_init,
            env.agent_observations(agent_coord_y_init, agent_coord_x_init),
            agent_coord_y_init_prev,
            agent_coord_x_init_prev,
            val_prev_init,
            max_x,
            min_x)

if agent_moving_given == 1:
    # Environment with physical agent
    print("\nPhysical agent placed in environment!")
    agent.val_prev=agent.val
    agent.val=2
    env.agent_in_map(agent.y, agent.x, agent.val, agent_coord_y_init_prev,agent_coord_x_init_prev,val_prev_init)
    env.print_env_structure()
    print("Agent observations: left=%d, right=%d" % env.agent_observations(agent_coord_y_init, agent_coord_x_init))
    print("Agent curent position:   y=%d, x=%d" %(agent.y, agent.x))
    print("Agent previous position: y=%d, x=%d" %(agent.y_prev, agent.x_prev))
    agent.print_percepts_array()
    print("Iteration: %d" %(t_global))
    print()
    if draw == 1: env.plot()

    try:
        while True:
            tm.sleep(sleep_time)
            # Timing for debug
            test = 0
            if test == 5 or tm.time() > loop_timeout:
                break
            test = test - 1
    
    
            ######################################################################################
            # Agent's or human's choice
            ######################################################################################

            print("\n[1] Move left")
            print("[2] Move right")
            
            # Ask for the user's choice.
            choice = input("\nWhat would you like to do? ")

            # Respond to the agent's or human's or choice.
            if choice == '1':
                print("---------------------------------------------------------")
                agent.move_left() # Update x position
                env.agent_in_map(agent.y, agent.x, agent.val,agent.y_prev, agent.x_prev, agent.val_prev) # Move agent location wrt environment
                agent.obs=env.agent_observations(agent.y, agent.x) # Sensor to update agent observations
                agent.perform_perceive_functions() # After sensor measurement updated,update percepts via a matrix
                
            elif choice == '2':
                print("---------------------------------------------------------")
                agent.move_right() 
                env.agent_in_map(agent.y, agent.x, agent.val,agent.y_prev, agent.x_prev, agent.val_prev)
                agent.obs=env.agent_observations(agent.y, agent.x) # Sensor to update agent observations
                agent.perform_perceive_functions()
            
            
            
            
            ######################################################################################
        
            # Debug Information
            if print_debug_info == 1:
                env.print_env_structure()
                print("Observations: left=%d, right=%d" % env.agent_observations(agent.y, agent.x))
                print("Agent curent position:   y=%d, x=%d, value=%d" %(agent.y, agent.x, agent.val))
                print("Agent previous position: y=%d, x=%d, prev_val=%d" %(agent.y_prev, agent.x_prev, agent.val_prev))
                agent.print_percepts_array()
            
            # Sensor reset, counter update and plot if needed
            agent.reset_percept_matrix()
            t_global=t_global+1
            print("Iteration: %d" %(t_global))
            print("---------------------------------------------------------")
            if draw == 1: 
                env.plot()
                
    except KeyboardInterrupt:
        pass









































if agent_moving_random == 1:
    
    # Environment without agent
    print("\nPhysical agent placed in environment!")
    agent.val_prev=agent.val
    agent.val=2
    env.agent_in_map(agent.y, agent.x, agent.val, agent_coord_y_init_prev,agent_coord_x_init_prev,val_prev_init)
    
    env.print_env_structure()
    print("Agent observations: left=%d, right=%d" % env.agent_observations(agent_coord_y_init, agent_coord_x_init))
    print("Agent curent position:   y=%d, x=%d" %(agent.y, agent.x))
    print("Agent previous position: y=%d, x=%d" %(agent.y_prev, agent.x_prev))
    agent.print_percepts_array()
    print("Iteration: %d" %(t_global))
    print()
    if draw == 1: env.plot()
    
    try:
        while True:
            tm.sleep(sleep_time)
            # Timing for debug
            test = 0
            if test == 5 or tm.time() > loop_timeout:
                break
            test = test - 1
            print("---------------------------------------------------------")

            # Agent moving
            agent.move()
            env.agent_in_map(agent.y, agent.x, agent.val,agent.y_prev, agent.x_prev, agent.val_prev)
            agent.obs=env.agent_observations(agent.y, agent.x) # Sensor to update agent observations
            agent.perform_perceive_functions()
            
            # Debug Information
            if print_debug_info == 1:
                env.print_env_structure()
                print("Observations: left=%d, right=%d" % env.agent_observations(agent.y, agent.x))
                print("Agent curent position:   y=%d, x=%d, value=%d" %(agent.y, agent.x, agent.val))
                print("Agent previous position: y=%d, x=%d, prev_val=%d" %(agent.y_prev, agent.x_prev, agent.val_prev))
                agent.print_percepts_array()
            
            agent.reset_percept_matrix()
            t_global=t_global+1
            print("Iteration: %d" %(t_global))
            print("---------------------------------------------------------")

            if draw == 1: 
                env.plot()

    except KeyboardInterrupt:
        pass