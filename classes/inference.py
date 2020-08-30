# Import python libraries


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

class World_Generator():
    pass


class Inference():    
    # Returns the infered state(s) based on matched generated world with the knowledge base
    
    def __init__(self, possible_worlds, KB):
        self.possible_worlds=possible_worlds
        self.KB = KB # Knowledge Base to check all the combinations of possible worlds against
        
        
    def infer_state():
        pass
        



class Knowledge_Base():
    
    # Includes state definitions
    # [ Left Observation, Right Observation ] + [ Right_Move=1 or 0, Left_Move=1 or 0 ] + [State 1 Prev, State 2 Prev, State 3 Prev]
    
    
    def __init__(self, observations, action_taken, prev_state):
        self.observations = observations # current observations of the agent, i.e., 1 or 0 to left or right [ (Left Observation) (Right Observation) ]
        self.action_taken = action_taken # if the agent decided to go left or right ( Right=1 or 0, Left=1 or 0 ), 0 false and 1 is true
        self.prev_state = prev_state # the preious state, according to state definitions, the agent was in [State 1, State 2, State 3], 0 false and 1 is true
