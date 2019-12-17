# RQLIB
## Requirements and Libraries Finder
## Overview
### Final Project, 2019 FALL, CSCI E-29
#### Gabriel Guillen, Zinoo Park

Wouldn't it be nice if we had a way of knowing which requirements and libraries were installed or not installed where ?
It is every so annoying to find your app working at home only to find that it breaks down on Travis just because
a library or a module was not included in the Pipfile.

The features designed are as below:

1. Find libraries installed in MAIN & libraries installed via PIPENV

2. Find where the dependencies are installed. Pathwise.

3. Show Dependency Tree

4. Convert Pipfiles to Travis versions

### Final Deliverable

The end product is an app that can be executed from the command line, in which you can select a folder or environment
to analyze.

### Instalation
This app (that is still a beta) works in a Conda Environment under Windows.
In order to install it, this repository should be copied i your computer and then 
Make sure that the following dependencies are installed: 

    - python=3.6
    - luigi==2.8.10
    - matplotlib==3.1.2
    - matplotlib-venn==0.11.5
    - pandas==0.25.3
    
    
If not you have at least two different ways to do it:

#### Option 1)
Execute 

pip install luigi matplotlib pandas matplotlib_venn

In order to install the missing dependencies

#### Option 2)
In the directory where you cloned the repository run:

conda env create --file=rqlibenv.yaml

Which creates a new environment from the yaml.file

Then you will need to activate the environment by executing:

conda activate rqlibEnv

### To Run
In terminal (not pipenv shell),
```bash
python -m rqlib -all  # will run everything
python -m rqlib -vg   # will only run VennGraph()
python -m rqlib -vl   # will only run Validation()
python -m rqlib -cd   # will only run checkdependency()
python -m rqlib -cd -dp {name}   # will only run checkdependency() for a dependency
python -m rqlib -tr  # will only run tree(). Not compatible with datetime stamps.
```

### Limitations and Challenges

Due to time constraint, it was only possible to develop for only one specific virtual environment or OS. In this case,
it was in Anaconda on Windows. However, given enough resources, it may be easy to scale.

Another limitation was the integration test, since Travis does not do well with Condas Environments under Windows, we needed to simulate enough environments in our computers in order to check the integration of our code...


