#!/usr/bin/env python

import argparse
import datetime


parser = argparse.ArgumentParser()

parser.add_argument('-cnv', '--con_env', type=str, dest='con_env', help='name or path of Conda Env File // Type . for default.') # For Conda
parser.add_argument('-pnv', '--pip_env', type=str, dest='pip_env', help='name or path of Pip Env File // Type . for default.')   # For Pip, not PIPENV
parser.add_argument('-ppv', '--pnv_env', type=str, dest='pnv_env', help='name or path of Pipfile.lock // Type . for default.')   # For Pipenv
parser.add_argument('-vd', '--vdg', type=str, dest='vdg', help="name or path of venn diagram // Type . for default")  # for Venn Diagram
parser.add_argument('-cf', '--csv', type=str, dest='csv', help="name or path of csv file of dependencies // Type . for default") # for CSV File of Dependencies
parser.add_argument('-dt', '--dep_tree', type=str, dest='dep_tree', help="name or path of dependency tree // Type . for default") # for Dependency Tree
parser.add_argument('-dp', '--depen', type=str, dest='depen', nargs='*', help="name of dependency to check. if empty string, checks all")


def main():
    args = parser.parse_args()

    # Store Conda Environment File name/path
    con_env = args.con_env
    # Store Pip Environment File name/path
    pip_env = args.pip_env
    # Store Pipfile.lock File name/path
    pnv_env = args.pnv_env
    # Store Venn Diagram File name/path
    vdg = args.vdg
    # Store Dependency CSV File name/path
    csv = args.csv
    # Store Dependency Tree File name/path
    dep_tree = args.dep_tree
    # Store Dependency Name to Check
    depen = args.depen

    if con_env and con_env == '.':
        con_env = 'condaJson.json'
    if pip_env and pip_env == '.':
        pip_env = 'pipJson.json'
    if pnv_env and pnv_env == '.':
        pnv_env = 'Pipfile.lock'
    if vdg and vdg == '.':
        datetime_str = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
        vdg = 'output/vnn_diag' + datetime_str + '.png'
    if csv and csv == '.':
        datetime_str = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
        csv = 'output/dep_output' + datetime_str + '.csv'
    if dep_tree and dep_tree == '.':
        datetime_str = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
        dep_tree = 'output/dep_tree' + datetime_str + '.txt'
    if depen and depen[0] == '.':
        depen = '.'
        # other wise it's a list of dependencies


#################################