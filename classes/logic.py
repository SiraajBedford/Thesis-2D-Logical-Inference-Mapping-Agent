# -*- coding: utf-8 -*-

class atomic():
    
    #True/ False and is a letter/character
    
    def __init__(self):
        self.atomic_dictionary={}
        
    def print_var(self, index):
        print(self.atomic_dictionary[index])
    
    def add_atomic(self, key, value):
        self.atomic_dictionary[key] = value 
    
    def print_atomic_dictionary(self):
        print(self.atomic_dictionary)
    
    def evaluate(self):
        pass
    
    
    def print_TT(self, exp1):
        pass
 

# Let's create a dictionary, the functional way 
  
# Create your dictionary class 
class my_dictionary(dict): 
  
    # __init__ function 
    def __init__(self): 
        self = dict() 
          
    # Function to add key:value 
    def add(self, key, value): 
        self[key] = value 

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
class cmplx():
    #Buids sentences with atomic sentences
    pass



class pl_engine():
    
    def __init__(self, list_of_variables):
        self.variables=list_of_variables
        
    def print_variables(self):
        print(self.variables)    
        
        
    def build_sentence(self):
        pass        
        
        
    def evaluate_NOT(self):
        pass
    
    def evaluate_AND(self):
        pass
    
    
    def evaluate_OR(self):
      pass
  
    
    def evaluate_IMPLIES(self):
      pass
  
    
    
    def evaluate_IFF(self):
      pass