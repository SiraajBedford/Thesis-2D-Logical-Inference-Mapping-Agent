# Import python libraries
import numpy as np

# Propositional Symbols used

"""
P_t - The space to the left is empty
Q_t - The space to the right is empty
R_t - The agent moved Right
S_t - The agent moved Left
T_t_min_1 - The agent was previously in State 1
U_t_min_1 - The agent was previously in State 2
V_t_min_1 - The agent was previously in State 3

Comparison Template
# [ Left Observation, Right Observation ] + [ Right_Move=1 or 0, Left_Move=1 or 0 ] + [State 1 Prev, State 2 Prev, State 3 Prev]
# Eg [0,0,0,1,0,1,0]

"""

from classes.logic import Proposition, Constant
from classes.logic import vars, truth_table_rows


# import itertools

# Initialization

P_t,Q_t=vars('P_t','Q_t')
P_t_check = Constant(True)
Q_t_check = Constant(True)


def my_func(params):
    print(params)


# def World_Generator(*list_of_prop):
#     for p in itertools.product([True,False],repeat=1):
#         params = list_of_prop
#         my_func(params)
#         pass


class Knowledge_Base():
    
    # Includes state definitions
    # [ Left Observation, Right Observation ] + [ Right_Move=1 or 0, Left_Move=1 or 0 ] + [State 1 Prev, State 2 Prev, State 3 Prev]
    
    
    def __init__(self):
        self.KB=[]
        
    def print_KB(self):
         print(self.KB)

        
    def add_sentences(self, observations, actions):
        # Here use observations, acttion taken and state definition to summarize possible worlds
        
        # observations - [1, 0], [0, 0], [0, 1]
        # actions - 1 or 0
        
        if observations == (1, 0):
            self.KB.append(~P_t & Q_t)
            
        if observations == (0, 0):
            self.KB.append(P_t & Q_t)
 
        if observations == (0, 1):
            self.KB.append(P_t & ~Q_t)

        # if actions == 1: # moved right
        #     self.KB.append(R_t)
            
        # if actions == 0: # moved ledt
        #     self.KB.append(S_t)
        
        
        
class Inference():    
    # Returns the infered state(s) based on matched generated world with the knowledge base
    
    def __init__(self, possible_worlds, KB):
        self.possible_worlds=possible_worlds
        self.KB = KB # Knowledge Base to check all the combinations of possible worlds against
        
        
        
        
    def print_prop(self, observations, actions):
        
        if observations == (1, 0):
            P_t_check=False
            Q_t_check=True
            
        if observations == (0, 0):
            P_t_check=True
            Q_t_check=True
            
 
        if observations == (0, 1):
            P_t_check=True
            Q_t_check=False
            
        print("P_t_check: %r" %(P_t_check))
        print("Q_t_check: %r" %(Q_t_check))
        print()
        
        state_1= ~P_t & Q_t
        state_2= P_t & Q_t
        state_3= P_t & ~Q_t
        
        state_1.print_truth_table()
        state_2.print_truth_table()
        state_3.print_truth_table()
        
    def infer_state():
        # if observation implies possible world, that possible world is the true world 
        pass
        




        






























