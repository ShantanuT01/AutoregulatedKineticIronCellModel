import pandas as pd
import numpy as np
import steadystate.constants as constants
# possible state variables


class CRMSingleState:
    def __init__(self,id,regulation, filePath, independentVariable) -> None:
        self.sensedSpecies = regulation
        self.id = id
        self.data = pd.read_csv(filePath)
        self.independent = independentVariable

    def getArcLengthOfComponent(self, component):
        distance = 0.0
        # find Euclidean distance between consecutive (x,y) coordinate pairs
        y = self.data[component].values
        x = self.data[self.independent].values
        for i in range(len(x) - 1):
            distance += np.hypot(x[i]-x[i+1],y[i]-y[i+1])
        return distance

    def getLinearDistance(self, component):
        y = self.data[component].values
        x = self.data[self.independent].values
        # start of state
        x0,y0 = x[0],y[0]
        # end of state
        x1,y1 = x[-1], y[-1]
        return np.hypot(x0-x1,y0-y1)

    def getWanderingScore(self):
        errors = []
        for component in constants.COMPONENTS:
            simArcLength = self.getArcLengthOfComponent(component)
            minArcLength = self.getLinearDistance(component)
            errors.append(np.abs(simArcLength - minArcLength)/minArcLength * 100)
        return np.mean(errors)
    
    def getSmoothnessScore(self):
        smoothness = 0.0
        for component in constants.COMPONENTS:
            y = self.data[component].values
            smoothness += np.sum(np.abs(np.diff(y)/y[:-1]) * 100)
        return smoothness





