import numpy as np

class MovementModel:
    def __init__(self):
        self.randMin = -100
        self.randMax = 100
        self.x = []
        self.y = []
        self.z = []

    def randomWalk(self):
        self.x.append(np.random.randint(self.randMin,self.randMax))
        self.y.append(np.random.randint(self.randMin,self.randMax))
        self.z.append(np.random.randint(self.randMin,self.randMax))
        print('x = ' + str(self.x) + '\t y =' + str(self.y) + '\t z =' + str(self.z))
        return [self.x, self.y, self.z]
