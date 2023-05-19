# assume case 1 regulation
import numpy as np
from cellstate.constants import *

def logisticFunction(L,n,SP,C,s):
    return L/(1 + np.exp(n*(s - SP))) + C

def getk23(fc):
    return logisticFunction(0.293708, -0.248768, 15.105, 0, fc)

def getkcia(fm):
    return logisticFunction(5.50768, 0.0387998, 0.991932, 0.41756,fm)

def getkvac(fc):
    return logisticFunction(2.88787, -0.679725, 14.0134, 0.160357, fc)

def getkmit(fs):
    return logisticFunction(168.632, 0.022031, 0.991933, 0.538779,fs)

def getkcyt(fc):
    return logisticFunction(2.15854, 1.00162, 8.74028, 2.62992,fc)

def getkO2(fs):
    return logisticFunction(95.3616, -0.0134783, 258.284, 0,fs)

def getkmp(fm):
    return logisticFunction(0.931282, -0.0587368, 224.854, 0.00105854, fm)


def getRegulatedRateConstant(rateConstant, attributes):
    rindex = RATE_CONSTANTS.index(rateConstant)
    
    if rindex == 0:
        return getkcia(attributes[FM])
    elif rindex == 1:
        return getk23(attributes[FC])
    elif rindex == 2:
        return attributes[KISU_GENE]
    elif rindex == 3:
        return getkmp(attributes[FM])
    elif rindex == 4:
        return getkvac(attributes[FC])
    elif rindex == 5:
        return getkmit(attributes[FS])
    elif rindex == 6:
        return getkcyt(attributes[FC])
    elif rindex == 7:
        return kres
    else:
        return getkO2(attributes[FS])
