from logic import PropKB, Expr, dpll_satisfiable,associate,pl_resolution,tt_entails
import random as rd

import time as tm
import re

# For graph mapping
#import cairo
from igraph import Graph, plot, GraphBase
from igraph.drawing.edge import AbstractEdgeDrawer as aed



# from agent_physical_mapping import Agent_physical
from utils import expr
open_block_1=0
not_open_block_1=1

# Expr functions for MappingAgentKB and MappingAgent

# State 1
def State1(time):
    return Expr('State_1', time) 

# Actions: [Left, Right, Up, Down, Bump]

def moved_left(time):
    return Expr('ML', time) 

def moved_right(time):
    return Expr('MR', time) 

def moved_up(time):
    return Expr('MU', time) 

def moved_down(time):
    return Expr('MD', time) 

def moved_bumped(time):
    return Expr('MB', time)

# Percepts: [left_open,right_open,
# up_open, upper_left_open, upper_right_open,
# bottom_open, bottom_left_open, bottom_right_open]

def S1(time):
    return Expr('S1', time)

def S2(time):
    return Expr('S2', time)

def S3(time):
    return Expr('S3', time)

def S4(time):
    return Expr('S4', time)

def percept_open_left_block(time):
    return Expr('L', time)
    
def percept_open_right_block(time):
    return Expr('R', time) 

def percept_open_up_block(time):
    return Expr('U', time)
    
def percept_open_upper_left_block(time):
    return Expr('UL', time) 

def percept_open_upper_right_block(time):
    return Expr('UR', time) 

def percept_open_bottom_block(time):
    return Expr('B', time)
    
def percept_open_bottom_left_block(time):
    return Expr('BL', time) 

def percept_open_bottom_right_block(time):
    return Expr('BR', time) 


def state(time):
    return Expr('State', time) 

# Symbols

def implies(lhs, rhs):
    return Expr('==>', lhs, rhs)


def equiv(lhs, rhs):
    return Expr('<=>', lhs, rhs)


# Helper Function

def new_disjunction(sentences):
    t = sentences[0]
    for i in range(1, len(sentences)):
        t |= sentences[i]
    return t

class MappingAgentKB(PropKB):
    """
    Can Use: tell(self, sentence), ask_generator(self, query), ask_if_true(self, query), retract(self, sentence)
    KB stored in  self.clauses = [] of PropKB
    
    """
    def __init__(self):

        super().__init__()
        self.states=[]
        self.kb_cnf = Expr('')
        
        # Any initial knowledge for the agent to function should be placed here - things that dont change overtime

    def clauses(self):
        print(self.kb.clauses)

    def make_action_sentence(self, action_matrix, time):
        
        # Actions done
        
        # Chain start
        #-------------------------------------------------
        if action_matrix[0] == 1:
            self.tell(moved_left(time))
            chain=moved_left(time)
            
        if action_matrix[0] == 0:
            self.tell(~moved_left(time))
            chain= ~moved_left(time)
        #-------------------------------------------------    
            
        if action_matrix[1] == 1:
            self.tell(moved_right(time))
            chain=chain & moved_right(time)
            
        if action_matrix[2] == 1:
            self.tell(moved_up(time))
            chain=chain & moved_up(time)
            
        if action_matrix[3] == 1:
            self.tell(moved_down(time))
            chain=chain & moved_down(time)
            
        if action_matrix[4] == 1:
            self.tell(moved_bumped(time))
            chain=chain & moved_bumped(time)

         # Actions not done

        if action_matrix[1] == 0:
            self.tell(~moved_right(time))
            chain=chain & ~moved_right(time)
            
        if action_matrix[2] == 0:
            self.tell(~moved_up(time))
            chain=chain & ~moved_up(time)
            
        if action_matrix[3] == 0:
            self.tell(~moved_down(time))
            chain=chain & ~moved_down(time)
            
        if action_matrix[4] == 0:
            self.tell(~moved_bumped(time))   
            chain=chain & ~moved_bumped(time)
            
        return chain
    
    def make_percept_sentence(self, percept_matrix, time):

        # Things perceived

        # Chain start
        #-------------------------------------------------
        if percept_matrix[0] == open_block_1:
            self.tell(percept_open_left_block(time))
            chain=percept_open_left_block(time)
            
        if percept_matrix[0] == not_open_block_1:
            self.tell(~percept_open_left_block(time))
            chain=~percept_open_left_block(time)
        #-------------------------------------------------

        if percept_matrix[1] == open_block_1:
            self.tell(percept_open_right_block(time))
            chain=chain & percept_open_right_block(time)

        if percept_matrix[2] == open_block_1:
            self.tell(percept_open_up_block(time))
            chain=chain & percept_open_up_block(time)
            
        if percept_matrix[3] == open_block_1:
            self.tell(percept_open_upper_left_block(time))
            chain=chain & percept_open_upper_left_block(time)
        
        if percept_matrix[4] == open_block_1:
            self.tell(percept_open_upper_right_block(time))
            chain=chain & percept_open_upper_right_block(time)

            
        if percept_matrix[5] == open_block_1:
            self.tell(percept_open_bottom_block(time))
            chain=chain & percept_open_bottom_block(time)
            # instead of having res, we can set a flag called 'flag=percept_open_bottom_block(time)' and then chain on other percept sentences

        if percept_matrix[6] == open_block_1:
            self.tell(percept_open_bottom_left_block(time))
            chain=chain & percept_open_bottom_left_block(time)
            
        if percept_matrix[7] == open_block_1:
            self.tell(percept_open_bottom_right_block(time))
            chain=chain & percept_open_bottom_right_block(time)
            
        # Things not perceived  

        if percept_matrix[1] == not_open_block_1:
            self.tell(~percept_open_right_block(time))
            chain=chain & ~percept_open_right_block(time)

        if percept_matrix[2] == not_open_block_1:
            self.tell(~percept_open_up_block(time))
            chain=chain & ~percept_open_up_block(time)
            
        if percept_matrix[3] == not_open_block_1:
            self.tell(~percept_open_upper_left_block(time))
            chain=chain & ~percept_open_upper_left_block(time)

        if percept_matrix[4] == not_open_block_1:
            self.tell(~percept_open_upper_right_block(time))
            chain=chain & ~percept_open_upper_right_block(time)
            
        if percept_matrix[5] == not_open_block_1:
            self.tell(~percept_open_bottom_block(time))
            chain=chain & ~percept_open_bottom_block(time)

        if percept_matrix[6] == not_open_block_1:
            self.tell(~percept_open_bottom_left_block(time))
            chain=chain & ~percept_open_bottom_left_block(time)

        if percept_matrix[7] == not_open_block_1:
            self.tell(~percept_open_bottom_right_block(time))
            chain=chain & ~percept_open_bottom_right_block(time)
            
        return chain  

    def add_temporal_sentences(self, time): # temporal: dependant on time since environment changes, atemporal: independant on time
        pass

class MappingAgent():
    
    """
    Split into:
        
    Execution level
    
    Inference level
    
    Graphing level

    
    """
     
    def __init__(self,t):
        
        # KB to store percepts and actions
        self.kb_actions_percepts = MappingAgentKB() # All the agent percepts and states are defined in this KB -- Only for 1 timestep
        # KB to state definitions
        self.state_kb=MappingAgentKB()
        # KB to store name of States for easier inference to ask self.state_kb
        self.state_name_kb=MappingAgentKB()
        # Knowledge for map reoresentation
        self.map=MappingAgentKB()
        # This variable converts the elements in a KB to a CNF sentence
        self.kb_cnf = None
        # to 'align' the agent and KB with the main implementation's time
        self.t = t
        # Capturing the states as the agent moves
        self.state_def_capture=[]
        self.state_def_capture_refined=[]
        self.state_def_capture_refined_kb=MappingAgentKB()
        
        # Visual agent map
        self.g = Graph([], directed=True)
        self.visual_style = {}
        self.current_node = 0
        self.previous_node = 0
        self.frame_slice_index = 0
        self.frame = []
        self.state_indices = [] 
        self.g.vs["name"] = []
        # self.g.vs["expression"] = []
    
    ############################################
    # Execution level
    ############################################
    
    def execute_v2(self, action_matrix, percept_matrix):
        
        # Clear KB percepts since we only need 1 time step for inference 
        # if len(self.kb_actions_percepts.clauses) == 2: 
        self.kb_actions_percepts.clauses.clear()

        # Percept and action from measurements
        self.kb_actions_percepts.make_percept_sentence(percept_matrix, self.t)
        self.kb_actions_percepts.make_action_sentence(action_matrix, self.t)
        
        
        # Inference: Ask the agent what actions it performed and percepts it saw based on a KB of only one time step
        #######################################################################
        
        start = tm.time()
        
        if self.t == 0:
            ############################
            if self.ask_if_true_dpll( moved_left(self.t) ) == False: 
                self.map.tell(moved_left(self.t)) # For moving left
                self.state_def_capture.append(moved_left(self.t))
                action_chain=moved_left(self.t)
                
            if self.ask_if_true_dpll( ~moved_left(self.t) ) == False: 
                self.map.tell(~moved_left(self.t)) # For moving left
                action_chain = ~moved_left(self.t)
                
            if self.ask_if_true_dpll( percept_open_left_block(self.t) ) == False: 
                self.map.tell(percept_open_left_block(self.t)) # For moving bump
                percept_chain = percept_open_left_block(self.t)
                
            if self.ask_if_true_dpll( ~percept_open_left_block(self.t) ) == False: 
                self.map.tell(~percept_open_left_block(self.t)) # For moving bump
                percept_chain = ~percept_open_left_block(self.t)
                
                
            ############################
                
            if self.ask_if_true_dpll( moved_right(self.t) ) == False: 
                self.map.tell(moved_right(self.t)) # For moving right
                self.state_def_capture.append(moved_right(self.t))
                action_chain = action_chain & moved_right(self.t)
                
            if self.ask_if_true_dpll( ~moved_right(self.t) ) == False: 
                self.map.tell(~moved_right(self.t)) # For moving left
                action_chain = action_chain & ~moved_right(self.t)
                
            if self.ask_if_true_dpll( moved_up(self.t) ) == False: 
                self.map.tell(moved_up(self.t)) # For moving up
                self.state_def_capture.append(moved_up(self.t))
                action_chain = action_chain & moved_up(self.t)
                
            if self.ask_if_true_dpll( ~moved_up(self.t) ) == False: 
                self.map.tell(~moved_up(self.t)) # For moving left
                action_chain = action_chain & ~moved_up(self.t)
                
            if self.ask_if_true_dpll( moved_down(self.t) ) == False: 
                self.map.tell(moved_down(self.t)) # For moving down
                self.state_def_capture.append(moved_down(self.t))
                action_chain = action_chain & moved_down(self.t)
                
            if self.ask_if_true_dpll( ~moved_down(self.t) ) == False: 
                self.map.tell(~moved_down(self.t)) # For moving left
                action_chain = action_chain & ~moved_down(self.t)
                
            if self.ask_if_true_dpll( moved_bumped(self.t) ) == False: 
                self.map.tell(moved_bumped(self.t)) # For moving bump
                self.state_def_capture.append(moved_bumped(self.t))
                action_chain = action_chain & moved_bumped(self.t)
                
            if self.ask_if_true_dpll( ~moved_bumped(self.t) ) == False: 
                self.map.tell(~moved_bumped(self.t)) # For moving left
                action_chain = action_chain & ~moved_bumped(self.t)
                
                
            if self.ask_if_true_dpll( percept_open_right_block(self.t) ) == False: 
                self.map.tell(percept_open_right_block(self.t)) # For moving bump
                percept_chain = percept_chain & percept_open_right_block(self.t)
                
            if self.ask_if_true_dpll( ~percept_open_right_block(self.t) ) == False: 
                self.map.tell(~percept_open_right_block(self.t)) # For moving bump
                percept_chain = percept_chain & ~percept_open_right_block(self.t)   
                

            if self.ask_if_true_dpll( percept_open_up_block(self.t) ) == False: 
                self.map.tell(percept_open_up_block(self.t)) # For moving bump
                percept_chain = percept_chain & percept_open_up_block(self.t)
                
            if self.ask_if_true_dpll( ~percept_open_up_block(self.t) ) == False: 
                self.map.tell(~percept_open_up_block(self.t)) # For moving bump
                percept_chain = percept_chain & ~percept_open_up_block(self.t)      

                
            if self.ask_if_true_dpll( percept_open_upper_left_block(self.t) ) == False: 
                self.map.tell(percept_open_upper_left_block(self.t)) # For moving bump
                percept_chain = percept_chain & percept_open_upper_left_block(self.t)
                
            if self.ask_if_true_dpll( ~percept_open_upper_left_block(self.t) ) == False: 
                self.map.tell(~percept_open_upper_left_block(self.t)) # For moving bump
                percept_chain = percept_chain & ~percept_open_upper_left_block(self.t)      
                
                
            if self.ask_if_true_dpll( percept_open_upper_right_block(self.t) ) == False: 
                self.map.tell(percept_open_upper_right_block(self.t)) # For moving bump
                percept_chain = percept_chain & percept_open_upper_right_block(self.t)
                
            if self.ask_if_true_dpll( ~percept_open_upper_right_block(self.t) ) == False: 
                self.map.tell(~percept_open_upper_right_block(self.t)) # For moving bump
                percept_chain = percept_chain & ~percept_open_upper_right_block(self.t)     
                
                
                
            if self.ask_if_true_dpll( percept_open_bottom_block(self.t) ) == False: 
                self.map.tell(percept_open_bottom_block(self.t)) # For moving bump
                percept_chain = percept_chain & percept_open_bottom_block(self.t)
                
            if self.ask_if_true_dpll( ~percept_open_bottom_block(self.t) ) == False: 
                self.map.tell(~percept_open_bottom_block(self.t)) # For moving bump
                percept_chain = percept_chain & ~percept_open_bottom_block(self.t)     
                
                
            if self.ask_if_true_dpll( percept_open_bottom_left_block(self.t) ) == False: 
                self.map.tell(percept_open_bottom_left_block(self.t)) # For moving bump
                percept_chain = percept_chain & percept_open_bottom_left_block(self.t)
                
            if self.ask_if_true_dpll( ~percept_open_bottom_left_block(self.t) ) == False: 
                self.map.tell(~percept_open_bottom_left_block(self.t)) # For moving bump
                percept_chain = percept_chain & ~percept_open_bottom_left_block(self.t)  
                
                
                
            if self.ask_if_true_dpll( percept_open_bottom_right_block(self.t) ) == False: 
                self.map.tell(percept_open_bottom_right_block(self.t)) # For moving bump
                percept_chain = percept_chain & percept_open_bottom_right_block(self.t)
                
            if self.ask_if_true_dpll( ~percept_open_bottom_right_block(self.t) ) == False: 
                self.map.tell(~percept_open_bottom_right_block(self.t)) # For moving bump
                percept_chain = percept_chain & ~percept_open_bottom_right_block(self.t)  
                
            
            ############################
            
            
            
        
        if self.t >= 1:
            ############################
            if self.ask_if_true_dpll( moved_left(self.t) ) == False: 
                self.map.tell(moved_left(self.t)) # For moving left
                self.state_def_capture.append(moved_left(self.t))
                action_chain=moved_left(self.t)
                
            if self.ask_if_true_dpll( ~moved_left(self.t) ) == False: 
                self.map.tell(~moved_left(self.t)) # For moving left
                action_chain = ~moved_left(self.t)
                
            if self.ask_if_true_dpll( percept_open_left_block(self.t) ) == False: 
                self.map.tell(percept_open_left_block(self.t)) # For moving bump
                percept_chain = percept_open_left_block(self.t)
                
            if self.ask_if_true_dpll( ~percept_open_left_block(self.t) ) == False: 
                self.map.tell(~percept_open_left_block(self.t)) # For moving bump
                percept_chain = ~percept_open_left_block(self.t)
                
                
            ############################
                
            if self.ask_if_true_dpll( moved_right(self.t) ) == False: 
                self.map.tell(moved_right(self.t)) # For moving right
                self.state_def_capture.append(moved_right(self.t))
                action_chain = action_chain & moved_right(self.t)
                
            if self.ask_if_true_dpll( ~moved_right(self.t) ) == False: 
                self.map.tell(~moved_right(self.t)) # For moving left
                action_chain = action_chain & ~moved_right(self.t)
                
            if self.ask_if_true_dpll( moved_up(self.t) ) == False: 
                self.map.tell(moved_up(self.t)) # For moving up
                self.state_def_capture.append(moved_up(self.t))
                action_chain = action_chain & moved_up(self.t)
                
            if self.ask_if_true_dpll( ~moved_up(self.t) ) == False: 
                self.map.tell(~moved_up(self.t)) # For moving left
                action_chain = action_chain & ~moved_up(self.t)
                
            if self.ask_if_true_dpll( moved_down(self.t) ) == False: 
                self.map.tell(moved_down(self.t)) # For moving down
                self.state_def_capture.append(moved_down(self.t))
                action_chain = action_chain & moved_down(self.t)
                
            if self.ask_if_true_dpll( ~moved_down(self.t) ) == False: 
                self.map.tell(~moved_down(self.t)) # For moving left
                action_chain = action_chain & ~moved_down(self.t)
                
            if self.ask_if_true_dpll( moved_bumped(self.t) ) == False: 
                self.map.tell(moved_bumped(self.t)) # For moving bump
                self.state_def_capture.append(moved_bumped(self.t))
                action_chain = action_chain & moved_bumped(self.t)
                
            if self.ask_if_true_dpll( ~moved_bumped(self.t) ) == False: 
                self.map.tell(~moved_bumped(self.t)) # For moving left
                action_chain = action_chain & ~moved_bumped(self.t)
                
                
            if self.ask_if_true_dpll( percept_open_right_block(self.t) ) == False: 
                self.map.tell(percept_open_right_block(self.t)) # For moving bump
                percept_chain = percept_chain & percept_open_right_block(self.t)
                
            if self.ask_if_true_dpll( ~percept_open_right_block(self.t) ) == False: 
                self.map.tell(~percept_open_right_block(self.t)) # For moving bump
                percept_chain = percept_chain & ~percept_open_right_block(self.t)   
                

            if self.ask_if_true_dpll( percept_open_up_block(self.t) ) == False: 
                self.map.tell(percept_open_up_block(self.t)) # For moving bump
                percept_chain = percept_chain & percept_open_up_block(self.t)
                
            if self.ask_if_true_dpll( ~percept_open_up_block(self.t) ) == False: 
                self.map.tell(~percept_open_up_block(self.t)) # For moving bump
                percept_chain = percept_chain & ~percept_open_up_block(self.t)      

                
            if self.ask_if_true_dpll( percept_open_upper_left_block(self.t) ) == False: 
                self.map.tell(percept_open_upper_left_block(self.t)) # For moving bump
                percept_chain = percept_chain & percept_open_upper_left_block(self.t)
                
            if self.ask_if_true_dpll( ~percept_open_upper_left_block(self.t) ) == False: 
                self.map.tell(~percept_open_upper_left_block(self.t)) # For moving bump
                percept_chain = percept_chain & ~percept_open_upper_left_block(self.t)      
                
                
            if self.ask_if_true_dpll( percept_open_upper_right_block(self.t) ) == False: 
                self.map.tell(percept_open_upper_right_block(self.t)) # For moving bump
                percept_chain = percept_chain & percept_open_upper_right_block(self.t)
                
            if self.ask_if_true_dpll( ~percept_open_upper_right_block(self.t) ) == False: 
                self.map.tell(~percept_open_upper_right_block(self.t)) # For moving bump
                percept_chain = percept_chain & ~percept_open_upper_right_block(self.t)     
                
                
                
            if self.ask_if_true_dpll( percept_open_bottom_block(self.t) ) == False: 
                self.map.tell(percept_open_bottom_block(self.t)) # For moving bump
                percept_chain = percept_chain & percept_open_bottom_block(self.t)
                
            if self.ask_if_true_dpll( ~percept_open_bottom_block(self.t) ) == False: 
                self.map.tell(~percept_open_bottom_block(self.t)) # For moving bump
                percept_chain = percept_chain & ~percept_open_bottom_block(self.t)     
                
                
            if self.ask_if_true_dpll( percept_open_bottom_left_block(self.t) ) == False: 
                self.map.tell(percept_open_bottom_left_block(self.t)) # For moving bump
                percept_chain = percept_chain & percept_open_bottom_left_block(self.t)
                
            if self.ask_if_true_dpll( ~percept_open_bottom_left_block(self.t) ) == False: 
                self.map.tell(~percept_open_bottom_left_block(self.t)) # For moving bump
                percept_chain = percept_chain & ~percept_open_bottom_left_block(self.t)  
                
                
                
            if self.ask_if_true_dpll( percept_open_bottom_right_block(self.t) ) == False: 
                self.map.tell(percept_open_bottom_right_block(self.t)) # For moving bump
                percept_chain = percept_chain & percept_open_bottom_right_block(self.t)
                
            if self.ask_if_true_dpll( ~percept_open_bottom_right_block(self.t) ) == False: 
                self.map.tell(~percept_open_bottom_right_block(self.t)) # For moving bump
                percept_chain = percept_chain & ~percept_open_bottom_right_block(self.t)  
         
            

            ############################
            
        # print(action_chain)
        # print(percept_chain)
        
                
        end = tm.time()
        #######################################################################
        print("Inference time: %f s" %((end - start)))

        #######################################################################
        

        # From percept and actions define the state -- replace with infered expression
        state = percept_chain & action_chain; # maybe we can clean this up with simplify
        # state = percept_chain ; # maybe we can clean this up with simplify
        # Define generated state name at time t
        State_name=self.return_nth_state()
        # Tell a seperate KB those names -- might remove
        self.state_name_kb.tell(State_name) 
        # Might remove
        self.map.tell(State_name) 
        
        
        # Tell the unrefined data list the defined infered state
        self.state_def_capture.append(State_name |'==>'| state )
        # Tell a KB the state definition at time t
        self.state_kb.tell( State_name |'==>'| state ) # give the name of states so we can do inference
        
        
        self.create_graph()
        
        self.t += 1
    
    
    ############################################
    #  Inference level
    ############################################
    
    
    # KB to CNF needed: CNF KB is the conjunction of clauses in the KB
    def kb_to_cnf(self):
        self.kb_cnf = associate('&', self.kb_actions_percepts.clauses)
        return self.kb_cnf
    
    # For any KB
    def any_kb_to_cnf(self, KB_clauses):# give clauses
        CNF_KB_sentence = associate('&', KB_clauses)
        return CNF_KB_sentence
      
    def ask_if_true_dpll(self, query): # inference via
        self.kb_to_cnf() # The knowledge base are facts joined by conjunctions    
        query1 =  expr( str(query) )
        return dpll_satisfiable(  ( self.kb_cnf ) & ~(query1) ) # proof by unsatisfiability
    
    def any_ask_if_true_dpll(self, query, KB_clauses): # inference via
        IN_CNF=self.any_kb_to_cnf(KB_clauses) # The knowledge base are facts joined by conjunctions    
        query1 =  expr( str(query) )
        return dpll_satisfiable(  ( IN_CNF ) & ~(query1) ) # proof by unsatisfiability
    
    def ask_if_true_dpll_state_def_KB(self, query): # inference via
        query1 =  expr( str(query) )
        IN_CNF=self.any_kb_to_cnf(self.state_kb.clauses) # The knowledge base are facts joined by conjunctions    
        return dpll_satisfiable(  ( IN_CNF ) & ~(query1) ) # proof by unsatisfiability
    
    def ask_if_true_resolution(self, query): # inference via
        return pl_resolution(self.kb_actions_percepts, query)
        # self.ask_if_true_resolution( self.state_1() |'==>'| ~percept_open_left_block(self.t) & percept_open_right_block(self.t))
    
    def any_ask_if_true_resolution(self, query,KB_entire): # inference via
        return pl_resolution(KB_entire, query)
    
    
    def ask_if_true_model_checking(self, query): # inference via
        return tt_entails( expr(str(self.kb_to_cnf())), expr(str(query)))
        # if self.ask_if_true_model_checking(~percept_open_left_block(self.t)):
        #     print("Agent in State 1")
    
    def any_ask_if_true_model_checking(self, query,KB_clauses): # inference via
        return tt_entails( expr(str(self.any_kb_to_cnf(KB_clauses))), expr(str(query)))
        # if self.ask_if_true_model_checking(~percept_open_left_block(self.t)):
        #     print("Agent in State 1")

        
    def agent_choice(self):
        return rd.choice(['a','d','w','s'])
        # return rd.choice(['a','d'])
        # return rd.choice(['d'])
        # return rd.choice(['a'])
        # return rd.choice(['w'])
        # return rd.choice(['s'])

    def return_nth_state(self):
        s=Expr('State'+ '_' + str(self.t), self.t) 
        return s
   
    def string_format_big(self, string):
        x = string.split("==>")
       
        pre=x[0]
        pre=re.sub(r'\(\d+\)', '', pre)
        pre=pre.replace('(','').replace(')','')
        
        post=x[1]
        post=post.replace('(','').replace(')','')
        post=''.join([i for i in post if not i.isdigit()])
        
        return pre + " ==>" + post
    
    def string_format_small(self, string):
        string = re.sub(r'\(\d+\)', '', string)
        return string.replace('(','').replace(')','')
    
    def transform_sentence(self, sentence):
        
        sentence=str(sentence)
        
        if len(sentence) <= 8:
            return self.string_format_small(sentence)
        
        if len(sentence) >= 10:
            return self.string_format_big(sentence)
    
    def convert_list_to_kb(self):
        for i in range(len(self.state_def_capture)):
            self.state_def_capture_refined_kb.tell( expr( self.state_def_capture[i] ) )
      
    def get_final_kb(self):
        self.convert_to_refined()
        self.convert_list_to_kb()
        return self.state_def_capture_refined_kb.clauses
    
    def convert_to_refined(self):
        # for i in range(len(self.state_def_capture)):
        self.state_def_capture_refined.append( self.transform_sentence( str(self.state_def_capture[self.t]) ) )
      
    def print_refined(self):
        self.convert_to_refined()
        return self.state_def_capture_refined
    
    ############################################
    #  Graphing level - Take representative learned list and convert into graph
    ############################################ 
    
    def create_vertex(self, sentence):
        pass
    
    def create_edge(self, sentence):
        pass
    
    def create_graph(self): # filtering through the data in state_def_capture_refined and capture that data in a graph for future use
        """
        Takes in self.state_def_capture_refined and builds a map using igraph and some rules
        """
        
        self.convert_to_refined()

        # Read index values from State to State
        # Store the index of the last state_def_capture_refined sentencebeing used
        
        # self.g = Graph([(0,1), (1,1), (0,2), (2,0), (2,3), (3,4), (4,4), (4,2), (2,5), (5,0), (6,3), (5,6)], directed=True)
        # self.g = Graph([], directed=True)
        # self.g.vs["name"] = ["State_0", "State_1", "State_2", "State_3", "State_4", "State_5", "State_6"]
        # self.g.vs["age"] = [25, 31, 18, 47, 22, 23, 50]
        # self.g.vs["gender"] = ["f", "m", "f", "m", "f", "m", "m"]
        # self.g.es["is_formal"] = [False, False, True, True, True, False, True, False, False]
        # self.g.vs["label"] = self.g.vs["name"] #assign each node label to the name
        # self.g.es["label"] = ["ML", "MR", "MU", "MD", "MB"] #assign each node label to the name
        # self.g.es["label"] = ["A", "B", "C"] #assign each node label to the name
       
        # self.g.vs["name"]=[]
        
        
        
        if len( self.state_def_capture_refined[self.t] ) > 7 : # A state and not a move
            self.frame.clear()
            self.state_indices.append(self.t) # Store the place to access node
            
            # self.frame = self.state_def_capture_refined[self.frame_slice_index : self.t+1]
            self.frame = self.state_def_capture_refined[self.frame_slice_index+1 : self.t+1]
            
            if len(self.frame) == 3: # agent did receive bump percept and we make a self-looping edge, must update current_node to equal previous_node 
                print(self.frame)
                print("frame length: %d" %(len(self.frame)))
               
                
                if len(self.g.vs["name"])<0: 
                    # self.g.add_edge(self.g.vs["name"][-1], self.g.vs["name"][-1], label= self.frame[0] + '&' + self.frame[1] )
                    
                    # if len( self.g.es["label"][-1] )  
                    
                    if (self.frame[0] == 'ML' and self.frame[1] == 'MB') or (self.frame[0] == 'MB' and self.frame[1] == 'ML'):
                        self.g.add_edge(self.g.vs["name"][-1], self.g.vs["name"][-1], label= self.frame[0] + '&' + self.frame[1] )
                        
                        
                    if (self.frame[0] == 'MR' and self.frame[1] == 'MB') or (self.frame[0] == 'MB' and self.frame[1] == 'MR'):
                        self.g.add_edge(self.g.vs["name"][-1], self.g.vs["name"][-1], label= self.frame[0] + '&' + self.frame[1] )
                        
                        
                    if (self.frame[0] == 'MU' and self.frame[1] == 'MB') or (self.frame[0] == 'MB' and self.frame[1] == 'MU'):
                        self.g.add_edge(self.g.vs["name"][-1], self.g.vs["name"][-1], label= self.frame[0] + '&' + self.frame[1] )
                        
                        
                        
                    if (self.frame[0] == 'MD' and self.frame[1] == 'MB') or (self.frame[0] == 'MB' and self.frame[1] == 'MD'):
                        self.g.add_edge(self.g.vs["name"][-1], self.g.vs["name"][-1], label= self.frame[0] + '&' + self.frame[1] )
                
                
                if len(self.g.vs["name"])>=1: 
                    # self.g.add_edge(self.g.vs["name"][-1], self.g.vs["name"][-1], label= self.frame[0] + '&' + self.frame[1] )
                    
                    # if len( self.g.es["label"][-1] )  
                    
                    # try:
                    # Evaluate last edge's label, then add to that label by concatenation?
                      # if self.g.vs["name"][-1]
                      # if self.g.es["label"][-1] = 'ML&MB' or 'MR&MB' or 'MD&MB' or 'MD&MB'
                    # if 'MB' in self.g.es["label"][-1]:
                    #     self.g.es["label"][-1] = self.g.es["label"][-1] + ',' +   self.frame[0] + '&' + self.frame[1]
                        
                    # except:
                    
                  
                                                        
                    
                    if (self.frame[0] == 'ML' and self.frame[1] == 'MB') or (self.frame[0] == 'MB' and self.frame[1] == 'ML'):
                        move_and_bump=self.frame[0] + '&' + self.frame[1] 
                        self.g.add_edge(self.g.vs["name"][-1], self.g.vs["name"][-1], label=move_and_bump )
                        
                        # if 'MB' in self.g.es["label"][-1]:
                        #     self.g.es["label"][-1] = self.g.es["label"][-1] + ',' +   self.frame[0] + '&' + self.frame[1]
                        
                        
                    if (self.frame[0] == 'MR' and self.frame[1] == 'MB') or (self.frame[0] == 'MB' and self.frame[1] == 'MR'):
                        move_and_bump=self.frame[0] + '&' + self.frame[1] 
                        self.g.add_edge(self.g.vs["name"][-1], self.g.vs["name"][-1], label= move_and_bump)
                        
                        # if 'MB' in self.g.es["label"][-1]:
                        #     self.g.es["label"][-1] = self.g.es["label"][-1] + ',' +   self.frame[0] + '&' + self.frame[1]
                        
                        
                    if (self.frame[0] == 'MU' and self.frame[1] == 'MB') or (self.frame[0] == 'MB' and self.frame[1] == 'MU'):
                        move_and_bump=self.frame[0] + '&' + self.frame[1] 
                        self.g.add_edge(self.g.vs["name"][-1], self.g.vs["name"][-1], label= move_and_bump)
                        
                        # if 'MB' in self.g.es["label"][-1]:
                        #     self.g.es["label"][-1] = self.g.es["label"][-1] + ',' +   self.frame[0] + '&' + self.frame[1]
                        
                        
                    if (self.frame[0] == 'MD' and self.frame[1] == 'MB') or (self.frame[0] == 'MB' and self.frame[1] == 'MD'):
                        move_and_bump=self.frame[0] + '&' + self.frame[1] 
                        self.g.add_edge(self.g.vs["name"][-1], self.g.vs["name"][-1], label= move_and_bump )
                    
                        # if 'MB' in self.g.es["label"][-1]:
                        #     self.g.es["label"][-1] = self.g.es["label"][-1] + ',' +   self.frame[0] + '&' + self.frame[1]
                    
                    
                    if 'MB' in self.g.es["label"][ self.g.get_eid(self.g.vs["name"][-1], self.g.vs["name"][-1]) ] :
                        self.g.es["label"][ self.g.get_eid(self.g.vs["name"][-1], self.g.vs["name"][-1]) ]=self.g.es["label"][ self.g.get_eid(self.g.vs["name"][-1], self.g.vs["name"][-1]) ]  + ',' +   self.frame[0] + '&' + self.frame[1]
                    
                    # self.g.es["label"]= self.frame[0] + '&' + self.frame[1] 
                # x = self.state_def_capture_refined[self.t].split("==>")
                # self.g.add_vertex(name=x[0], expression=x[1])
                # self.g.vs["label"] = self.g.vs["name"] 
                
                
            # if len(self.frame) == 2 and len(self.g.vs["name"]) <= 2: # agent did not receive bump percept and we can proceed to make a new node (vertex), must update current_node and previous_node
            if len(self.frame) == 2 : # agent did not receive bump percept and we can proceed to make a new node (vertex), must update current_node and previous_node

                print(self.frame)
                print("frame length: %d" %(len(self.frame)))
            
            
                if self.frame[0] == 'ML':
                    x = self.frame[1].split("==>")
                    self.g.add_vertex(name=x[0], expression=x[1])
                    
                    if len(self.g.vs["name"]) >= 2: 
                        self.g.add_edge(self.g.vs["name"][-2], self.g.vs["name"][-1], label="ML")
                        # self.g.es["label"] = self.frame[0]
                        # self.g.es["label"].extend(self.frame[0])  
                        

                
                if self.frame[0] == 'MR':
                    x = self.frame[1].split("==>")
                    self.g.add_vertex(name=x[0], expression=x[1])
                    
                    if len(self.g.vs["name"]) >= 2: 
                        self.g.add_edge(self.g.vs["name"][-2], self.g.vs["name"][-1], label="MR")
                        # self.g.es["label"] = self.frame[0]
                        # self.g.es["label"].extend(self.frame[0])  
            
                if self.frame[0] == 'MU':
                    x = self.frame[1].split("==>")
                    self.g.add_vertex(name=x[0], expression=x[1])
                    
                    if len(self.g.vs["name"]) >= 2: 
                        self.g.add_edge(self.g.vs["name"][-2], self.g.vs["name"][-1], label="MU")
                        # self.g.add_edge(self.g.vs["name"][-2], self.g.vs["name"][-1])
                        # self.g.es["label"] = self.frame[0]
                        # self.g.es["label"].extend(self.frame[0])  
                
                if self.frame[0] == 'MD':
                    x = self.frame[1].split("==>")
                    self.g.add_vertex(name=x[0], expression=x[1])      
                    
                    if len(self.g.vs["name"]) >= 2: 
                        self.g.add_edge(self.g.vs["name"][-2], self.g.vs["name"][-1], label="MD")
                        # self.g.add_edge(self.g.vs["name"][-2], self.g.vs["name"][-1])
                        # self.g.es["label"].extend(self.frame[0])  
                     
                        
                        
                        
                        
           ##########################################     
            # if len(self.frame) == 2 and len(self.g.vs["name"]) >= 3: # agent did not receive bump percept and we can proceed to make a new node (vertex), must update current_node and previous_node
            #     print(self.frame)
            #     print("frame length: %d" %(len(self.frame)))
            
            #     # if self.g.vs["expression"][-1] == self.g.vs["expression"][-2]:
            #     #     pass
            
            #     if self.g.vs["expression"][-1] != self.g.vs["expression"][-2]:
                
            #         if self.frame[0] == 'ML':
            #             x = self.frame[1].split("==>")
            #             self.g.add_vertex(name=x[0], expression=x[1])
                        
            #             if len(self.g.vs["name"]) >= 2: 
            #                 self.g.add_edge(self.g.vs["name"][-2], self.g.vs["name"][-1])
            #                 self.g.es["label"] = self.frame[0]
                            
    
                    
            #         if self.frame[0] == 'MR':
            #             x = self.frame[1].split("==>")
            #             self.g.add_vertex(name=x[0], expression=x[1])
                        
            #             if len(self.g.vs["name"]) >= 2: 
            #                 self.g.add_edge(self.g.vs["name"][-2], self.g.vs["name"][-1])
            #                 self.g.es["label"] = self.frame[0]
                
            #         if self.frame[0] == 'MU':
            #             x = self.frame[1].split("==>")
            #             self.g.add_vertex(name=x[0], expression=x[1])
                        
            #             if len(self.g.vs["name"]) >= 2: 
            #                 self.g.add_edge(self.g.vs["name"][-2], self.g.vs["name"][-1])
            #                 self.g.es["label"] = self.frame[0]
                    
            #         if self.frame[0] == 'MD':
            #             x = self.frame[1].split("==>")
            #             self.g.add_vertex(name=x[0], expression=x[1])      
                        
            #             if len(self.g.vs["name"]) >= 2: 
            #                 self.g.add_edge(self.g.vs["name"][-2], self.g.vs["name"][-1])
            #                 self.g.es["label"] = self.frame[0]
            
       
        
            self.frame_slice_index = self.state_indices[-1] # update the new slice position to be the index of the last place you saw a state in state_def_capture_refined
            

                

    def plot_created_graph(self):
        # self.create_graph()
        
        # Modify general style
        layout = self.g.layout("fr") # circle, drl, fr, grid_fr, kk, large, random, rt, rt_circular, sphere, # fr seems the best
        self.visual_style["layout"] = layout
        self.visual_style["margin"] = 130
        #self.visual_style["bbox"] = (400, 400)
        
        # Modify vertex style
        self.visual_style["vertex_size"] = 40
        self.visual_style["vertex_label_size"] = 10
        self.visual_style["vertex_label"] = self.g.vs["name"]
        self.visual_style["vertex_label_dist"] = 0
        self.visual_style["vertex_label_angle"] = 3
        self.visual_style["vertex_label_angle"]=0
        self.visual_style["vertex_label_color"] = "black"
        self.visual_style["vertex_color"] = "yellow"
        
        # Modify edge style
        self.visual_style["edge_arrow_size"] = 1
        self.visual_style["edge_width"] = 2
        
        return plot(self.g, **self.visual_style)

            



    
