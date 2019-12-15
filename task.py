import json
import os

import luigi
import matplotlib
import pandas as pd
from luigi import ExternalTask, Parameter, Task, LocalTarget
import subprocess
from matplotlib_venn import venn3, venn3_circles
from matplotlib import pyplot as plt

def command(cmd):
    return subprocess.check_output(cmd, shell=True).decode("utf-8")


def handleConda(filename):
    lines = open(filename, 'r').readlines()
    del lines[-1]
    open(filename, 'w').writelines(lines)


def readLockFile(filename="Pipfile.lock", mode="default"):
    with open(filename) as json_file:
        data = json.load(json_file)

    name = []
    version = []

    for p in data[mode]:
        name.append(p)
        version.append(data[mode][p]['version'].replace("=", ""))

    df = pd.DataFrame(list(zip(name, version)), columns=["name", "version"])
    return df

def readJson(filename):
    with open(filename) as json_file:
        data = json.load(json_file)
        #
    name = []
    version =[]

    for p in data:
        name.append(p['name'])
        version.append(p['version'])

    df = pd.DataFrame(list(zip(name, version)),columns=["name","version"])
    return df

class CreateConda(Task):
    path_conda = Parameter(default="condaJSON.json")

    def run(self):
        command("conda list --json  >" + self.path_conda)
        handleConda(self.path_conda)

    def output(self):
        return LocalTarget(self.path_conda, format=luigi.format.Nop)


class CreatePip(Task):
    path_pip = Parameter(default="pipJSON.json")

    def run(self):
        command("pip list --format json >" + self.path_pip)

    def output(self):
        return LocalTarget(self.path_pip, format=luigi.format.Nop)


class CheckPipLockFile(ExternalTask):
    path_lock = Parameter(default="Pipfile.lock")

    def output(self):
        return LocalTarget(self.path_lock)

class Validation(Task):
    """
    Luigi Taks that stylize images according to a model
    """
    path_conda = Parameter(default="condaJSON.json")
    path_pip = Parameter(default="pipJSON.json")
    path_lock = Parameter(default="Pipfile.lock")
    path_out = Parameter(default="output.csv")
    def requires(self):
        return {
            'conda': self.clone(CreateConda),
            'pip': self.clone(CreatePip),
            'pipenv': self.clone(CheckPipLockFile)
        }

    def output(self):
        return LocalTarget("output.csv", format=luigi.format.Nop)

    def run(self):
        inputs = self.input()
        conda = readJson(inputs['conda'].path).rename(columns={"version": "conda_v"})
        pip = readJson(inputs['pip'].path).rename(columns={"version": "pip_v"})
        pipenvdef = readLockFile(filename=inputs['pipenv'].path).rename(columns={"version": "pipenv_def_v"})
        pipenvdev = readLockFile(filename=inputs['pipenv'].path,mode='develop').rename(columns={"version": "pipenv_dev_v"})

        finalDF = conda.merge(pip, left_on='name', right_on='name', how='outer') \
            .merge(pipenvdef, left_on='name', right_on='name', how='outer') \
            .merge(pipenvdev, left_on='name', right_on='name', how='outer')

        finalDF = finalDF.fillna("-").set_index('name')

        finalDF.to_csv(self.output().path)

class VennGraph(Task):
    path_conda = Parameter(default="condaJSON.json")
    path_pip = Parameter(default="pipJSON.json")
    path_lock = Parameter(default="Pipfile.lock")
    path_out = Parameter(default="output.csv")

    def requires(self):
        return {
            'conda': self.clone(CreateConda),
            'pip': self.clone(CreatePip),
            'pipenv': self.clone(CheckPipLockFile)
        }

    def run(self):
        inputs = self.input()
        conda = readJson(inputs['conda'].path).rename(columns={"version": "conda_v"})
        pip = readJson(inputs['pip'].path).rename(columns={"version": "pip_v"})
        pipenvdef = readLockFile(filename=inputs['pipenv'].path).rename(columns={"version": "pipenv_def_v"})
        conda_venn = set(conda['name'])
        pip_venn = set(pip['name'])
        pipenv_env = set(pipenvdef['name'])
        v = venn3([conda_venn, pip_venn, pipenv_env], ('Conda', 'Pip', 'Pipenv (default)'))
        plt.savefig(self.output().path)


    def output(self):
        return LocalTarget("testplot.png", format=luigi.format.Nop)
