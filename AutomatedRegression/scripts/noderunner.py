from subprocess import call
import subprocess
import webbrowser
from time import sleep
from selenium import webdriver
from HTMLWriter import setUpServer
from HTMLWriter import getRates, setUpFile, getCSVFile, clearOutputFiles

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

# Note that you have to specify path to script
rates = getRates()
RUNTIME = 8
LOCALHOST = "http://localhost:8080"
def runServer(time,url):
   # webbrowser.open(url,0)
    driver = webdriver.Chrome()
    try:
        server = subprocess.Popen(["node", "regapp.js"])
        driver.get(url)
        sleep(2)
        server.wait(4)
    except subprocess.TimeoutExpired:
        server.kill()
        driver.close()
        
print(bcolors.OKBLUE+"Starting Regression scripts"+bcolors.ENDC)
clearOutputFiles()
print(bcolors.OKGREEN + "Successfully cleared output files!" + bcolors.ENDC);
for m in range(1, 7):
    print("Getting Regression Model", m)
    for rate in rates:
        for i in range(0,4):
            outcome = setUpFile("html/regression.html", rate, i,model=m)
            if(not outcome):
                continue
            setUpServer("regapp.js",getCSVFile(m))
            runServer(RUNTIME, LOCALHOST)
    print(bcolors.OKGREEN + "Finished model", m, bcolors.ENDC)







