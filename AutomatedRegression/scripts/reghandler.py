from numpy.core.numeric import indices
import pandas as pd
import numpy as np
from pandas.core.frame import DataFrame
from pandas.core.reshape.merge import merge


def mergeFiles(files):
    frames = list();
    for file in files:
        frame = pd.read_csv(file,dtype=object);
        frames.append(frame);
    i = frames[0]
    for j in range(1, len(frames)):
        temp = frames[j].iloc[:,1]
        i["Values"+str(j)]=temp;
    i = i.rename({'Variable': 'Variable', ' Value': 'W','Values1':'Y','Values2':'D'}, axis=1)
    i.to_csv("data/statedata.csv",index=False)
    

mergeFiles(["../SystemSolver/wildtypecomponents.txt","../SystemSolver/yfh1components.txt","../SystemSolver/dcomponents.txt"])
FRAME = pd.read_csv("data/statedata.csv",dtype=object)
FRAME = FRAME.transpose();

first_row = FRAME.iloc[0]
FRAME = FRAME[1:]

FRAME.columns = first_row; 
class RegHandler:
    def __init__(self, x, y) -> None:
        self.rate = y;
        self.component = x; 
        self.ind = FRAME[self.component].values
       
        self.dep = FRAME[self.rate].values

    def isValidRegFunction(self):
        x = np.argsort(np.array(self.ind,dtype=float));
      
        y = np.argsort(np.array(self.dep,dtype=float));

        return (np.array_equal(x,y) or np.array_equal(np.flip(x),y));
    
    def __str__(self) -> str:
        return self.component + " " + self.rate;
    
    

        

class RegDatabase:
    def __init__(self, rates) -> None:
        self.mapping = dict()
        for rate in rates:
            self.mapping[rate] = list();
    def addComponent(self, rate, component):
        h = RegHandler(component, rate)
        if(h.isValidRegFunction()):
            self.mapping[rate].append(component)
            return True
        else:
            return False
    def __str__(self) -> str:
        ret = ""
        for key in self.mapping.keys():
            ret+=key +": ";
            ret+=str(self.mapping[key]);
            ret+="\n"
        return ret
    def toFile(self, filepath):
        file = open(filepath,'w');
        output = str(self);
        output = output.replace(": ",",")
        output = output.replace("[","\"[")
        output = output.replace("]","]\"")
        output = output.replace("'","")
        output = "Rate,Species\n"+output
        file.write(output)
        file.flush()
        file.close()

X = first_row.values[0:8]
print(X)
Y =first_row.values[8:len(first_row.values)-3]
Y = np.append(Y,first_row.values[-1])
print(Y)
db = RegDatabase(Y);
for i in range(0, len(X)):
    component = X[i]
    for j in range(0, len(Y)):
        db.addComponent(Y[j],component);
print(db)
db.toFile("data/ratemapping.csv")
