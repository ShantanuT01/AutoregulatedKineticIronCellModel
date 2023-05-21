# Automated Regression

## Purpose

Reg functions (regulatory functions) are functions that connect states together in a cell and are a mathematical tool to show transitions. It is also demonstrates the concept of autoregulation in a cell. 


## Running Code

`scripts/` directory contains Python files used in running the local server with the Desmos API. 

After installing the required dependencies, run the following commands in the terminal just inside `AutomatedRegression` folder.

```
python scripts/reghandler.py
python scripts/noderunner.py
python scripts/flagger.py 
```
The `noderunner.py` script will open a webbrowser. After computing the appropriate regression values, it will open a new window and repeat with the remaining calculations. Windows are automatically closed

`reghandler.py` merges the individual state values into one .csv file for convenience. 

`flagger.py` eliminates "poor choices" for regression. 

## Results

All regression results are stored in the subdirectory `AutomatedRegression/data/regressionresults`.

Run `scripts/mathematicagetter.py` to create the `.wls` file containing the Mathematica code for the reg functions.

`logistic_functions.wls` contains the code for Mathematica functions.
