import pandas as pd
from cellstate.constants import *
from cellstate.rates import *
from cellstate.regulation import getRegulatedRateConstant
class CellState:
    def __init__(self, initialFile,oxygen,iron,kisu,alpha,includeRateConstants=True):
        self.alpha = alpha
        dataframe = pd.read_csv(initialFile)
        self.attributes = dict()
        self.attributes[KISU_GENE] = kisu
        self.attributes[OXYGEN] = oxygen
        self.attributes[IRON] = iron
        self.attributes[ALPHA] = self.alpha
        for i in range(len(dataframe)):
            row = dataframe.iloc[i].to_numpy()
            self.attributes[row[0].strip()] = row[1]
        self.precomputedrateconstants = includeRateConstants
        if self.precomputedrateconstants:
            for rc in RATE_CONSTANTS:
                self.attributes[rc] = getRegulatedRateConstant(rc, self.attributes)
        

    def getComponents(self,stateName):
        # table 2 values
        ret = dict()
        for component in COMPONENTS:
            ret[component] = self.attributes[component]
        ret[ALPHA] = self.attributes[ALPHA]
        ret["FeCell"] = self.getFeCell()
        ret[IRON] = self.attributes[IRON]
        ret[OXYGEN] = self.attributes[OXYGEN]
        return ret
    
    def getFeCell(self):
        return FCYT * (self.attributes[CIA] + self.attributes[FC]) + FVAC*(self.attributes[F2] + self.attributes[F3]) + FMIT*(self.attributes[FM] + self.attributes[FS] + self.attributes[MP])


    def getRates(self,filePath=None):
        ret = dict()
        if filePath:
            rates = pd.read_csv(filePath).T.to_dict()
         #   print(rates)
            for key in rates:
                rateName = rates[key]['Rate']
                rateValue = rates[key][' Value']
                ret[rateName] = rateValue
        else:
            for rate in RATES:
                ret[rate] = calculateRateLaw(rate, self.attributes)
      
        for rc in RATE_CONSTANTS:
            ret[rc] = self.attributes[rc]
        return ret



