# rate law expressions

import cellstate.constants as constants
from cellstate.constants import *
def michaelisMenten(k, s,km):
    return (k*s)/(s+km)

def Rcyt(kcyt, iron):
    return michaelisMenten(kcyt,iron, constants.KCYT)

def Rmit(kmit, fc):
    return michaelisMenten(kmit, fc, constants.KMIT)

def Rvac(kvac, fc):
    return michaelisMenten(kvac, fc, constants.KVAC)

def Rcia(kcia, fc):
    return michaelisMenten(kcia, fc, constants.KCIA)

def Risu(kisu, fm,o2):
    return michaelisMenten(kisu,fm,constants.KISU) *(constants.O2SP/(constants.O2SP + o2))

def Rmp(kmp, fm, o2):
    return kmp * fm * o2

def RO2(kO2, oxygen, o2):
    return kO2*(oxygen - o2)

def Rres(fs, o2):
    return michaelisMenten(constants.kres, o2, constants.KRESO2) * fs

def R23(k23, f2, oxygen):
    return michaelisMenten(k23, f2, constants.KF2) * oxygen

def dilution(alpha, component):
    return alpha * component

def calculateRateLaw(rate, attributes):
    rate = rate.strip()
    if rate == RCIA:
        return Rcia(attributes["kcia"], attributes[FC])
    elif rate == R23_NAME:
        return R23(attributes["k23"],attributes[F2],attributes[OXYGEN])
    elif rate == RISU:
        return Risu(attributes[KISU_GENE], attributes[FM], attributes[O2])
    elif rate == RVAC:
        return Rvac(attributes["kvac"], attributes[FC])
    elif rate == RMIT:
        return Rmit(attributes["kmit"], attributes[FC])
    elif rate == RCYT:
        return Rcyt(attributes["kcyt"], attributes[IRON])
    elif rate == RRES:
        return Rres(attributes[FS], attributes[O2])
    elif rate == RO2_NAME:
        return RO2(attributes["kO2"],attributes[OXYGEN], attributes[O2])
    elif rate == RMP:
        return Rmp(attributes["kmp"],attributes[FM], attributes[O2])
    else:
        # a dilution term
        componentName = rate[1:]
        return dilution(attributes[ALPHA], attributes[componentName])
    