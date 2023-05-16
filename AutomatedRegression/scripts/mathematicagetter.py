f = open("data/regressionresults/finalpool.csv",'r')
lines = f.readlines()
reglib = dict()
first = 0;
for line in lines:
    if(first == 0):
        first+=1
        continue
    key = line.split(", ")[1].strip()
    if(key not in reglib.keys()):
        reglib[key] = list()
        reglib[key].append(line)
    else:
        reglib[key].append(line)
def createMathematicaFunction(name, params, body,localvars):
    ret = name+"["
    for i in range(0, len(params)):
        params[i] = params[i].strip()+"_"
    locals = ','.join(localvars)
    ret+=",".join(params)+"]:=\n"
    ret+="Module[{"+locals+"},\n"
    code = "\n".join(body)
    ret+=code+"\n]"
    return ret

def createSwitchStatement(cases, retvals,vartolookat):
    line = list()
    line.append(vartolookat)
    for i in range(0, len(retvals)):
        line.append(cases[i])
        line.append(retvals[i])
    internal = ",".join(line)
    return "Switch["+internal+"]"

#sample input: FC, k23, 28.7472, -0.681373, 11.4286, 0, 1
def createRegFunctionLine(params):
    parts = params.split(",")
    L = parts[2]
    n = parts[3]
    SP = parts[4]
    C = parts[5]
    x = parts[0].strip()+"[t]"
    p = [L,n,SP,C,x]
    varname = parts[0].strip().lower()+"case"
    line = varname +" = "+"RegFunction["+','.join(p)+"];"
    return line

def createBody(rate):
    caselist = reglib[rate]
    firstpart = list()
    retvals = list()
    casestolookat = list()
    for f in caselist:
        parse = createRegFunctionLine(f).strip(); 
        firstpart.append(parse)
        c = f.split(", ")[0].strip() + "L"
        retval = parse[0:parse.find("=")].strip()
        casestolookat.append(c)
        retvals.append(retval)
    vartolookat = "list"
    firstpart.append(createSwitchStatement(casestolookat, retvals, vartolookat))
    return firstpart

    
localvars0 = ["ciacase","fscase","o2case"]
localvars1 = ["fccase","f3case"]
localvars2 = ["f2case","fmcase","mpcase"];


file = open("logistic_functions.wls",'w+')
for rate in reglib.keys():
    body = createBody(rate)
    name = "getk"+str(rate).upper()[1:]
    localvar = list()
    parameter = ["list"]
    comps = reglib[rate]
    for comp in comps:
        localvar.append(comp.split(",")[0].strip().lower() + "case")
    file.write(createMathematicaFunction(name, parameter, body, localvar)+"\n")
file.flush()
file.close()






