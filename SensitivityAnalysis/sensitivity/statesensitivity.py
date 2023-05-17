import pandas as pd
import sensitivity.constants as constants
from sensitivity.rateconstant import RateConstant
class StateSensitivity:
    def __init__(self, filePath, state):
        self.dataframe = pd.read_csv(filePath)
        self.rateConstants = dict()
        self.state = state
        # split data file by rate constant
        rategroups = self.dataframe.groupby(constants.ALTERED_RATE_CONSTANT)

        for ratename, rateframe in rategroups:
            rc = RateConstant(ratename, rateframe)
            self.rateConstants[ratename] = rc
    
    def getRateConstantSensitivities(self):
        ret = dict()
        for rc in constants.RATE_CONSTANTS:
            ret[rc] = self.rateConstants[rc].getOverallSensitivity()
        return ret

        

