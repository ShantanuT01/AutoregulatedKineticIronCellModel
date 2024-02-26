# Kinetic Iron Autoregulated Cell


This repository contains code for our [paper](https://doi.org/10.1371/journal.pcbi.1011701). Navigate to each directory on the command line/terminal to execute code.

Most code is either Jupyter (Python) notebooks or Wolfram Mathematica notebooks. 

For Wolfram Mathematica notebooks, you should clear the kernel (quit) before running the contents of each notebook.

Some directories (such as `SteadyStateAnalysis/`) have a subdirectory for a Python module to help with data analysis (these modules will contain a blank `__init__.py` file).

Directories that have data (simulated, calculated, etc.) are stored in a `data/` subfolder. 

## Dependencies

There are three major languages used to build this model - Wolfram Mathematica, Python, and JavaScript. 

### Wolfram Mathematica
Wolfram Mathematica should work as is -- there are no third-party dependencies used. You will need to purchase a copy from Wolfram's website. 

### Python
For Python, it is strongly recommended to use a virtual environment to run the relevant code to avoid dependency conflicts. Anaconda was used to manage the virtual environment for development.

Install Anaconda for your operating system. Once the default environment (base) has been activated in the terminal, run from the main directory of this repository:
```
conda create --name nameOfEnvironment python=3.9
conda activate nameOfEnvironment
pip install -r requirements.txt
```
Once you are in the directory of the Jupyter notebook you want to open, run
```
jupyter notebook notebookFilePath
``` 

### JavaScript

Since JS is mostly a web-development language, you must install Node.js to run JavaScript locally. After installing Node.js, `npm` (node package manager) should be installed. 
You can verify the installation with `npm -v`. 
Navigate to the `AutomatedRegression/` folder, and run `npm install`. All dependencies should be installed. Ignore any warnings regarding vulnerabilities. 

## Directory Structure

### MatrixCalculations

This notebook finds the reduced row echelon form.

### StateData

This directory contains code to generate the state values for W, Y, D, and the hypoxic states.

### SystemSolver

This directory contains code and data for solving the W, Y, and D state unknown variables.

### AutomatedRegression

This directory contains code on creating logistic functions (the model's regulatory functions).

### Filtering

This directory contains the trend rule and targeting filters. 

### SteadyStateAnalysis

This directory has code for filters regarding steady state transitions: wandering, smoothness, and reasonableness scores. 

### TimeDependent

This directory has code for generating time dependent plots as well as predictions for the hypoxic state. 

### Stability

This directory has code for finding the Jacobian and eigenvalues, which help with determining stability of the model. 

### SensitivityAnalysis

Sensitivity data/results are computed here. 

## Citation
```
@article{thorat2023kinetic,
  title={A kinetic model of iron trafficking in growing Saccharomyces cerevisiae cells; applying mathematical methods to minimize the problem of sparse data and generate viable autoregulatory mechanisms},
  author={Thorat, Shantanu and Walton, Jay R and Lindahl, Paul A},
  journal={PLOS Computational Biology},
  volume={19},
  number={12},
  pages={e1011701},
  year={2023},
  publisher={Public Library of Science San Francisco, CA USA}
}
```
