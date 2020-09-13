# Creator: S. Bedford
# Project Topic: "Learning the structure of an agent's environment from experience"

# Import python libraries
import numpy as np # For manipulating arrays
import time as tm # To control simulation time
from numpy import genfromtxt # To import a map from as a numpy array
import csv # To import a csv file
from pyswip import Prolog

# Import user defined libraries
from classes.environment import Environment
from classes.agent import Agent

# To implement
from classes.inference import Inference
from classes.inference import Knowledge_Base

## Initial state

#Inferencer
#inference=Inference(np.array([[1,2,0,0,1]]))

# Create environment

sim_mode = 1 # Scale from 1 to 10 on the length of the map
draw = 1 # 1-yes, 0-no
loop_timeout = tm.time() + 1 * 6000  # While-loop timeout
sleep_time = 1 # In seconds, how often debugging information is reported
print_debug_info = 1 # 1-yes, 0-no
agent_moving = 1 # 1-yes, 0-no
inference_development_mode = 1 # 1-yes, 0-no

if sim_mode == 1: sim_env=np.array([[1,0,0,0,0,1]])
if sim_mode == 2: sim_env=np.array([[1,0,0,0,0,0,1]])
if sim_mode == 3: sim_env=np.array([[1,0,0,0,0,0,0,0,1]])
if sim_mode == 4: sim_env=np.array([[1,0,0,0,0,0,0,0,0,0,1]])
# sim_env = np.asarray( list(csv.reader(open("maps\\first_map.csv"))), dtype=np.int )

# Future implementation - np.where(sim_env==1)
max_x=np.shape(sim_env)[1]-2
min_x=np.shape(sim_env)[0]
env=Environment(sim_env)



# Create agent with default values
agent_coord_y_init_prev=0
agent_coord_x_init_prev=0
val_prev_init=0

agent_coord_y_init=0
agent_coord_x_init=(max_x-min_x)//2+1
agent_val_init=0

agent=Agent(agent_coord_y_init,
            agent_coord_x_init,
            agent_val_init,
            env.agent_observations(agent_coord_y_init, agent_coord_x_init),
            agent_coord_y_init_prev,
            agent_coord_x_init_prev,
            val_prev_init,
            max_x,
            min_x)


# Environment without agent
print("Environment without agent")
print(env.structure)
print()

# Place agent in evironment, must update agent value - Agent has value of 7 after initial step
if agent_moving == 1:
    print("Agent placed in environment!")
    print()
    agent.val_prev=agent.val
    agent.val=2
    env.agent_in_map(agent.y, agent.x, agent.val, agent_coord_y_init_prev,agent_coord_x_init_prev,val_prev_init)

    print("Observations: left=%d, right=%d" % env.agent_observations(agent_coord_y_init, agent_coord_x_init))
    print("Agent curent position:   y=%d, x=%d" %(agent.y, agent.x))
    print("Agent previous position: y=%d, x=%d" %(agent.y_prev, agent.x_prev))
    print(env.structure)
    if draw == 1: env.plot()

    # Initialize knowledge base
    KB=Knowledge_Base()


try:
    while True:

        tm.sleep(sleep_time)
        # Timing for debug
        test = 0
        if test == 5 or tm.time() > loop_timeout:
            break
        test = test - 1

        # Agent moving

        if agent_moving == 1:
            agent.move()
            env.agent_in_map(agent.y, agent.x, agent.val,agent.y_prev, agent.x_prev, agent.val_prev)

        # Debug Information
        if print_debug_info == 1:
            print()
            print(env.structure)
            print("Observations: left=%d, right=%d" % env.agent_observations(agent.y, agent.x))
            print("Agent curent position:   y=%d, x=%d, value=%d" %(agent.y, agent.x, agent.val))
            print("Agent previous position: y=%d, x=%d, prev_val=%d" %(agent.y_prev, agent.x_prev, agent.val_prev))
        if draw == 1: env.plot()

        # Inference
        if inference_development_mode == 1:

            # Update Knowledge base
            # Give the KB the observations and actions
            # Convert observations and actions to propositional variables
            # Only later after we have infered the state, we can include previous state as 'T_t_min_1', 'U_t_min_1', 'V_t_min_1'

            # Sumarrize [ Left Observation, Right Observation ] + [ Right_Move=1 or 0, Left_Move=1 or 0 ] + [State 1 Prev, State 2 Prev, State 3 Prev]
            # in a numoy array and print
            KB.add_sentences(env.agent_observations(agent.y, agent.x), agent.random_move)

            print("---------------------------------------------------------------------------------------------------------------")
            KB.print_KB()
            print("---------------------------------------------------------------------------------------------------------------")


            inference=Inference(0, 0)
            inference.print_prop(env.agent_observations(agent.y, agent.x), agent.random_move)




except KeyboardInterrupt:
    pass
