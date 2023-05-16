#script to help notify if regression results need to be manually updated
from HTMLWriter import getCSVFile
bestregs = list(); 
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


class Equation:
    def __init__(self, comp, rate,L,n,SP,C,r2) -> None:
        self.comp = comp
        self.rate = rate
        self.L = L
        self.SP = SP
        self.C = C
        self.n = n; 
        self.r2 = r2
    def __eq__(self, o: object) -> bool:
        return o.comp == self.comp and o.rate == self.rate
    def __str__(self) -> str:
        parts = [self.comp,self.rate,self.L,self.n, self.SP,self.C,self.r2]
        return ', '.join(parts)
    def isBetter(self, o):
        if(abs(float(self.n)) < abs(float(o.n))):
            return True
        else:
            return False
        
def isBestRegression(L,SP,C, r2):
    try:
        if(r2.strip()=="1"):
            if(float(L) < 0):
                return False
            elif(float(SP) < 0):
                return False
            elif float(C) < 0:
                return False
        else:
            return False
        return True
    except:
        return False
def flagResults(filepath):
    file = open(filepath,'r');
    contents = file.read()
    lines = contents.splitlines();
    ret = list();
    #L, n, SP, C,
    lines = lines[1:]
    for l in lines:
        flag = False; 
        parts = l.split(",")
        r2 = parts[-1].strip()
        comp = parts[0]
        rate = parts[1]
        L = parts[2]
        n = parts[3]
        SP = parts[4]
        C = parts[5]
        if(r2 != "1"):
            flag = True
        else:
            try:
                if(float(C)< 0):
                    flag = True
                elif float(L) < 0:
                    flag = True
                elif float(SP) < 0:
                    flag = True
            except:
                #assume something went wrong with regression
                flag = True
                

        if(flag):
            tup=(comp, rate)
            ret.append(tup)
        else:
            temp = Equation(comp,rate,L,n,SP,C,r2)
            if(isBestRegression(L,SP, C, r2)):
                found = False 
                for k in bestregs:
                    if(k==temp):
                        found = True
                        if(temp.isBetter(k)):
                            bestregs.remove(k)
                            bestregs.append(temp)
                if(not found):
                    bestregs.append(temp)
                        
    file.close()
    return ret; 

sets = list()
for i in range(1, 7):
    f = getCSVFile(i)
    results = flagResults(f)
    sets.append(results)

def intersection(a,b):
    return list(set(a) & set(b))

s = intersection(sets[0],sets[0])
for i in range(1, len(sets)):
    s = intersection(s, sets[i])
print(bcolors.FAIL + "Regressions that failed across all 6 tries: " +bcolors.ENDC)
print(s)

if(len(bestregs) < (3+4+1+4+4+1+3)):
    print("Found Regressions: ", len(bestregs))
    print(bcolors.WARNING+"Not all regressions were found to be ideal!"+bcolors.ENDC)
else:
    print(bcolors.OKGREEN + "All regressions were ideal."+bcolors.ENDC)
print("Best Reg Pool:")
#print("Sensed Species, Rate Constant, L, n, SP, C, R^2")
def sortFunc(a):
    return a.rate
bestregs.sort(key=sortFunc)
mp = open("data/regressionresults/finalpool.csv",'w+')
mp.write("Sensed Species, Rate Constant, L, n, SP, C, R^2\n")
for elem in bestregs:
    mp.write(str(elem)+"\n")
mp.flush()
mp.close()

FSKMIT = "F2, kmit, 3.6911*10^12, 2.6596, 18.7543, 0.487841, 0.9978"
O2KO2 = "O2, kO2, 107.554,9.25168, 1.1293, 18.4559,1"





            



    