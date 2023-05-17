import pandas as pd
import sensitivity.constants as constants

class RateConstant:
    def __init__(self,varname,dataframe):
        self.dataframe = dataframe
        # sort frame by factor
        self.dataframe = self.dataframe.sort_values(by=[constants.FACTOR])
        self.rate = varname
        self.baseIndex = 0
        for i in range(len(self.dataframe)):
            if self.dataframe.iloc[i].to_dict()[constants.FACTOR] == 1:
                self.baseIndex = i

    def getBaseConcentration(self, component):
        # get row where factor == 1
        return self.dataframe.iloc[self.baseIndex].to_dict()[component]
    
    def getPercentDifference(self, component):
        rawConcentrations = self.dataframe[component].values
        baseline = self.getBaseConcentration(component)
        return (rawConcentrations - baseline)/baseline * 100.0

    def getComponentSensitivity(self, component):
        percent = self.getPercentDifference(component)
        
        # use estimated slope from Taylor series approximation
        # each element in the array is separated by a scale factor of 0.01
        
        numerator = percent[self.baseIndex - 2] - 8 * percent[self.baseIndex - 1] + 8*percent[self.baseIndex + 1] + percent[self.baseIndex + 2]
        denominator = 12 * (0.01)
        return (numerator/denominator)/self.getBaseConcentration(component)



    def getOverallSensitivity(self):
        sensitivity = 0.0
        for component in constants.COMPONENTS:
            # take absolute value since we care about magnitude
            sensitivity += abs(self.getComponentSensitivity(component))
           # print("Sensitivity for",self.rate, "for", component, "is", self.getComponentSensitivity(component))
        return sensitivity/len(constants.COMPONENTS)
