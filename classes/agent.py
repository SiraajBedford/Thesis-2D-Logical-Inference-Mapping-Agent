# Creator: S. Bedford (21093741@sun.ac.za)
# Project Topic: "Learning the structure of an agent's environment from experience"
# "agent.py" - Agent implementation
# Enumerates possible worlds from percepts
# Uses Knowlege base and query sentences to see which would is real  

# Import python libraries
import numpy as np

class PropKB():
    
    """You can tell and ask the KB sentences. An implementation inspired by
    'AI: A modern approach' code base for Chapter 7: Logical Agents """
    
    
    def __init__(self, sentence=None):
        self.clauses = []
        if sentence:
            self.tell(sentence)
        
        
    def tell(self, sentences):
        np.append(self.KB, sentences)
        pass
    
    
    def ask_KB(self, sentences):
        pass
    
    
    def return_KB(self):
        return self.KB

class Agent():
    
    def __init__(self,KB, percept_matrix):
        self.percept_matrix=percept_matrix
        
        
    
    # ifthe agent has not observed specific surrounding it blocks before then call it a new state
    # if it has already seen that state for example (0,0) in [1,0,0,2,0,1] the if it took different 
    # actions to get to that state then call it a new state
    
    # Inference willl work by asking "Am i in State_n ()?" -> 
    
    def KB_Agent(self):    
        
        """The details of the representation language are hidden inside three functions that imple-
        ment the interface between the sensors and actuators on one side and the core representation
        and reasoning system on the other. M AKE -P ERCEPT -S ENTENCE constructs a sentence as-
        serting that the agent perceived the given percept at the given time. M AKE -A CTION -Q UERY
        constructs a sentence that asks what action should be done at the current time. Finally,
        M AKE -A CTION -S ENTENCE constructs a sentence asserting that the chosen action was ex-
        ecuted. The details of the inference mechanisms are hidden inside T ELL and A SK . Later
        sections will reveal these details."""
        
        
        # Persistent: A knowledge base, may contain some background knowledge
        # Persistent: t, a counter initially zero
        # Tell and Ask may involve INFERENCE
        
        # Tell(KB, MAKE-PERCEPT-SENTENCE(percept, t))
        
        # MAKE-PERCEPT-SENTENCE(percept, t)
        
        # action = Ask(KB, MAKE-ACTION-QUERY(t))
        
        # Tell(KB, MAKE-ACTION-SENTENCE(action, t)) 
        
        # t=t+1
        # return action 
        pass
    
    
    def get_percepts_at_t(self, percept_matrix, t):
        pass
    
    def MAKE_PERCEPT_SENTENCE(self, percept, t):
        pass
    
    
    def MAKE_ACTION_QUERY(self, t):
        pass
    
    
    def MAKE_ACTION_SENTENCE(action, t):
        pass
    
    def inference(self):
        # infer to discover a state
        pass


