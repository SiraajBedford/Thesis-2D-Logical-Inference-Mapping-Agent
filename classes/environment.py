import numpy as np
from numpy import genfromtxt

class Environment():


    def gen_env_from_csv(self, path):
        return genfromtxt(path , delimiter=',')


    def print_try(self):
        print("Rick Rolled!!")
