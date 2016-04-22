#Lab 8
#Johanna O'Day

import numpy as np

class Molecule:
    """Contains particle objects, spring constant and equilibrium length"""

    def __init__(self,Position1,Position2,M1,M2,k,L0):
        self.p1 = Particle(Position1, M1)
        self.p2 = Particle(Position2, M2)
        self.k = k
        self.L0 = L0 
        
    def get_displ(self):
        return tuple(np.subtract(self.p1.pos,self.p2.pos))

    def get_force(self):
        return self.k*self.L0
            