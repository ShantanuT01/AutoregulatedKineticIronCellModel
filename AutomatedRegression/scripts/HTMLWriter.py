import pandas as pd
import re 
file = open("html/regression.html", "r");

MAP = pd.read_csv("data/ratemapping.csv")
STATES = pd.read_csv("data/statedata.csv",dtype=object).transpose();
first_row = STATES.iloc[0]
STATES = STATES[1:]
STATES.columns = first_row; 
def generateColumn(x,delimiter=","):
    ret = "";
    parts = x.split(delimiter)
    for p in parts:
        ret+= p +","
    ret = ret[0:len(ret)-1]+""
    return ret

#modelsetter = "calculator.setExpression({ id: 'regression', type: 'expression', latex: MODELGOESHERE });"
MODEL1 = r"'y_1~\\frac{L}{1+e^{n(x_1-S)}}+C \\{L>0, C\\geq 0, S\\geq 0\\}'" #constraints and c
MODEL2 = r"'y_1~\\frac{L}{1+e^{n(x_1-S)}}+C'" #no constraints and c
MODEL3= r"'y_1~\\frac{L}{1+e^{n(x_1-S)}} \\{L>0, S\\geq 0\\}'" #constraints and no c
MODEL4= r"'y_1~\\frac{L}{1+e^{n(x_1-S)}}'" #no constraints and no c
MODEL5 = r"'y_1~\\frac{L}{1+e^{n(x_1-S)}} +C\\{S\\geq 0\\}'"
MODEL6 = r"'y_1~\\frac{L}{1+e^{n(x_1-S)}} +C\\{L > 0\\}'"
cases = [MODEL1, MODEL2, MODEL3, MODEL4,MODEL5, MODEL6]
def findAndReplaceFile(filepath, y, x, complabel, ratelabel, model=1):
    file = open(filepath, "r");
    contents = file.read()
    modelsetter = "calculator.setExpression({ id: 'regression', type: 'expression', latex: MODELGOESHERE });"
    modelsetter = modelsetter.replace("MODELGOESHERE", cases[model-1]);
    contents = contents.splitlines()
    for j in range(0, len(contents)):
        if(contents[j].find("id: 'regression'") != -1):
            contents[j] = modelsetter;
            break;
    contents = '\n'.join(contents)
    #fresh file
    if(contents.find("X_VALUES_GO_HERE")>=0):
        contents = contents.replace("X_VALUES_GO_HERE", generateColumn(x))
        contents = contents.replace("Y_VALUES_GO_HERE", generateColumn(y))
        contents = contents.replace("RATELABELGOESHERE", ratelabel);
        contents = contents.replace("COMPONENTLABELGOESHERE", complabel);
    #file that has already been written to
    else:
        contents = re.sub("\[.*?\]", generateColumn(x), contents);
        rindex = contents.rfind(generateColumn(x)[1:-1])
        contents= contents[0:rindex]+ "Y_VALUES_GO_HERE," + contents[rindex+len(generateColumn(x)):]
        contents = contents.replace("Y_VALUES_GO_HERE", generateColumn(y)[1:])
        metasetter = """//metadata setter
var RATEVAR = "RATELABELGOESHERE";
var COMPVAR = "COMPONENTLABELGOESHERE";
//metadata ender
        """;
        metasetter = metasetter.replace("RATELABELGOESHERE", ratelabel)
        metasetter = metasetter.replace("COMPONENTLABELGOESHERE", complabel)
        contents = contents[0:contents.find("//metadata setter")] + metasetter + contents[contents.find("var result ="):]




    file = open(filepath,  'w')
    file.write(contents);
    file.flush();
    file.close()


#test function
#findAndReplaceFile("html/regression.html","1,2,3,4","5,6,7,8")

#get data
rates = MAP["Rate"].values
species = MAP["Species"].values
def getValues(var):
    a = STATES[var].values
    return a

DESMOSMAP = dict();
i = 0;
for rate in rates:
    temp = str(getValues(rate))[1:-1]
    DESMOSMAP[rate] = [str(getValues(rate).tolist()),list()]
    spec = species[i]
    i+=1; 
    spec = spec.replace("[","").replace("]","").split(",")
    for j in range(0, len(spec)):
        spec[j] = spec[j].strip()
    for sp in spec:
        z = getValues(sp);
        DESMOSMAP[rate][1].append(str(z.tolist()))

MAP = MAP.transpose()
newmapcols = MAP.iloc[0,:]
MAP.columns = newmapcols; 

#print(DESMOSMAP["kcia"][1][1])
#findAndReplaceFile("html/regression.html",DESMOSMAP["kcia"][0], DESMOSMAP["kcia"][1][1],"FC","IDK")

def setUpFile(filepath, ratevar, compindex,model=1):
    p = DESMOSMAP[ratevar]
    compvar = ""
    valid = MAP[ratevar]["Species"]
    valid = valid[1:-1]
    valid = valid.split(", ")
    if(compindex >= len(valid)):
        return False
    compvar = valid[compindex]
    findAndReplaceFile(filepath, p[0],p[1][compindex], compvar, ratevar,model)
    return True
def setUpServer(filepath, filetowritepath):
    targetLine =  """writeToFile("results.csv",req.body.name);"""
    targetLine = targetLine[0: targetLine.find("\"")+1] + filetowritepath + targetLine[targetLine.rfind("\""):]
    file = open(filepath, "r");
    contents = file.read()
    contents = contents.splitlines()
    for j in range(0, len(contents)):
        if(contents[j].find("""writeToFile(\"""") != -1):
            contents[j] = targetLine;
            break;
    contents = '\n'.join(contents)
    file = open(filepath,'w')
    file.write(contents)
    file.flush()
    file.close()
def getCSVFile(model):
    path = "data/regressionresults/"
    files = ["results-constraintsC.csv", "results-noconstraintsC.csv","results-constraints.csv","results-noconstraints.csv","model5.csv","model6.csv"]
    return path+files[model-1]
def getRates():
    return rates; 

def clearOutputFiles():
    for i in range(1, 7):
        file = open(getCSVFile(i), 'w')
        file.write("Component, Rate, L, n, SP, C, R^2\n");
        file.flush();
        file.close()
        
#setUpFile("html/regression.html", "kcia",2,model=4)
#setUpServer("regapp.js","data/regressionresults/results-noconstraints.csv")



