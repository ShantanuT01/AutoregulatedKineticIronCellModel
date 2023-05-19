# Michaelis Menten constants
KCYT = 10
KMIT = 20
KVAC = 20
KCIA = 20 
KISU = 100
KRESO2 = 1
KF2 = 200 
O2SP = 1 

# components
FC = "FC"
F2 = "F2"
F3 = "F3"
FM = "FM"
MP = "MP"
O2 = "O2"
CIA = "CIA"
FS = "FS"

COMPONENTS = [CIA, F2,F3,FC,FM,FS,MP,O2]
# technically an environmental variable but it is just a constant
CARBON = 100
KISU_GENE = "kisu"
IRON = "IRON"
OXYGEN = "OXYGEN"
# other variables
kres = 36.36363636363636363636
FCYT = 0.8
FMIT = 0.1
FVAC = 0.1

# rates
RCIA = "Rcia"
R23_NAME = "R23"
RISU = "Risu"
RMP = "Rmp"
RVAC = "Rvac"
RMIT = "Rmit"
RCYT = "Rcyt"
RRES = "Rres"
RO2_NAME = "RO2"
# dilution terms
DFC = "DFC"
DCIA = "DCIA"
DF2 = "DF2"
DF3 = "DF3"
DFM = "DFM"
DFS = "DFS"
DMP = "DMP"
DO2 = "DO2"

ALPHA = "alpha"
RATES = [RCIA, R23_NAME, RISU, RMP, RVAC, RMIT, RCYT, RRES, RO2_NAME, DFC, DCIA, DF2, DF3, DFM, DFS, DMP, DO2]
RATE_CONSTANTS = rateconstants = ["kcia","k23","kisu","kmp","kvac","kmit","kcyt","kres","kO2"]