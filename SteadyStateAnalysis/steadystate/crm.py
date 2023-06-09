import numpy as np
import pandas as pd
import steadystate.constants as constants
from steadystate.singlestate import CRMSingleState
class CellularRegulatoryMechanism:
    def __init__(self, caseNum, regulation, wyFilePath,wdFilePath):
        self.id = caseNum
        self.sensedSpecies = regulation
        self.dstate = CRMSingleState(caseNum, regulation, wdFilePath, constants.IRON)
        self.ystate = CRMSingleState(caseNum, regulation, wyFilePath, constants.KISU)
    
    def getSmoothnessScore(self):
        return self.dstate.getSmoothnessScore() + self.ystate.getSmoothnessScore()
    
    def getWanderingScore(self):
        return (self.dstate.getWanderingScore() + self.ystate.getWanderingScore())/2.0

    def getReasonablenessScore(self, dataPath):
        regpooldata = pd.read_csv(dataPath)
        columns = [col.strip() for col in regpooldata.columns]
        regpooldata.columns = columns
        spError = 0.0
        nError = 0.0
        for rateConstant in self.sensedSpecies:
            if rateConstant.upper().strip() == "ID":
                continue
            else:
                # iterate through rows in dataframe to find reg function
                species = self.sensedSpecies[rateConstant]
                found = False
                for i in range(len(regpooldata)):
                    row = regpooldata.iloc[i].to_dict()
                   
                    if row[constants.SENSED_SPECIES].strip() == species and row[constants.RATE_CONSTANT].strip().lower() == rateConstant.lower():
                        found = True
                        if abs(row["n"]) >= 1:
                            nError += (abs(row["n"]) - 1)
                        else:
                            nError += (abs(1.0/row["n"]) - 1)
                        
                        meanSpecies = np.mean(constants.STATES[species])
                        spError += abs(row["SP"] - meanSpecies)/meanSpecies
                if not found:
                    raise Exception(f"not found!: {species} {rateConstant}")
        return spError, nError

    def getStateTransitionData(self, state):
        if state == 'Y':
            df = self.ystate.data
            ind = self.ystate.independent
        else:
            df = self.dstate.data
            ind = self.dstate.independent
        ret = dict()
        ret[ind] = df[ind].values
        for component in constants.COMPONENTS:
            ret[component] = df[component].values/max(constants.STATES[component])
        return ret



    def __str__(self) -> str:
        return "Case " + str(self.id)
    
    
    