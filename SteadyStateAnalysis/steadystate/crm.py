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
                for i in range(len(regpooldata)):
                    row = regpooldata.iloc[i].to_dict()
            
                    if row[constants.SENSED_SPECIES].strip() == species and row[constants.RATE_CONSTANT].strip() == rateConstant:
                        if row["n"] >= 1:
                            nError += (row["n"] - 1)
                        else:
                            nError += (abs(1.0/row["n"]) - 1)
                        
                        meanSpecies = np.mean(constants.STATES[species])
                        spError += abs(row["SP"] - meanSpecies)/meanSpecies
        return spError + nError

                        


    def __str__(self) -> str:
        return "Case " + str(self.id)
    
    
    