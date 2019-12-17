#!/usr/bin/env python

import argparse
import datetime

from luigi import build, LuigiStatusCode
from task import Validation, VennGraph, checkDependency, tree

### use of timestamps will make using -tr alone VERY difficult
### as luigi will look for a file with a different timestamp
### for tree, python -m -rqlib
datetime_str = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
## to mute datetime_str, uncomment line below
# datetime_str = ''

parser = argparse.ArgumentParser()

parser.add_argument('-all', '--all', action='store_true', help="type -all to run everything")
parser.add_argument('-vg', '--vn_g', action='store_true', help="type -vg to use VennGraph()")
parser.add_argument('-vl', '--val', action='store_true', help="type -vl to use Validation()")
parser.add_argument('-cd', '--chk', action='store_true', help="type -cd to use checkDependency() // -cd -dp {name}")
parser.add_argument('-tr', '--tree', action='store_true', help="type -tr to use tree()")


parser.add_argument('-cnv', '--con_env', type=str, default='condaJson.json', dest='con_env', help='name or path of Conda Env File // Type . for default.') # For Conda
parser.add_argument('-pnv', '--pip_env', type=str, default='pipJson.json', dest='pip_env', help='name or path of Pip Env File // Type . for default.')   # For Pip, not PIPENV
parser.add_argument('-ppv', '--pnv_env', type=str, default='Pipfile.lock', dest='pnv_env', help='name or path of Pipfile.lock // Type . for default.')   # For Pipenv
parser.add_argument('-vd', '--vdg', type=str, default='output/vnn_diag' + datetime_str + '.png', dest='vdg', help="name or path of venn diagram // Type . for default")  # for Venn Diagram
parser.add_argument('-cf', '--csv', type=str, default='output/dep_output' + datetime_str + '.csv', dest='csv', help="name or path of csv file of dependencies // Type . for default") # for CSV File of Dependencies
parser.add_argument('-dt', '--dep_tree', default='output/dep_tree' + datetime_str + '.txt', type=str, dest='dep_tree', help="name or path of dependency tree // Type . for default") # for Dependency Tree
parser.add_argument('-dc', '--dep_check', type=str, default='output/dep_check' + datetime_str + '.txt', dest='dep_check', help="name or path of dependency check // Type . for default") # for Dependency Tree
parser.add_argument('-dp', '--dpn', type=str, dest='dpn', help="name of dependency to check. if empty string, checks all")
# parser.add_argument('-dp', '--dpn', type=str, dest='dpn', nargs='*', help="name of dependency to check. if empty string, checks all")  ### This accepts multiple items


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
    # Store Dependency Check File name/path
    dep_check = args.dep_check
    # Store Dependency Name to Check
    dpn = args.dpn


    if con_env and con_env == '.':
        con_env = 'condaJson.json'
    if pip_env and pip_env == '.':
        pip_env = 'pipJson.json'
    if pnv_env and pnv_env == '.':
        pnv_env = 'Pipfile.lock'
    if vdg and vdg == '.':
        vdg = 'output/vnn_diag' + datetime_str + '.png'
    if csv and csv == '.':
        csv = 'output/dep_output' + datetime_str + '.csv'
    if dep_tree and dep_tree == '.':
        dep_tree = 'output/dep_tree' + datetime_str + '.txt'
    if dep_check and dep_check == '.':
        dep_check = 'output/dep_check' + datetime_str + '.txt'
    if dpn and dpn == '.':
        dpn = 'luigi'

    # if dpn were a list
    # if dpn and dpn[0] == '.':
    #     dpn = '.'
        # otherwise it's a list of dependencies
#################################

    if args.vn_g:
        build([VennGraph(path_conda=con_env, path_pip=pip_env, path_lock=pnv_env, path_out_plot=vdg)], local_scheduler=True, detailed_summary=True)

    if args.val:
        build([Validation(path_conda=con_env, path_pip=pip_env, path_lock=pnv_env, path_out_val=csv)], local_scheduler=True, detailed_summary=True)

    if args.chk:
        build([checkDependency(path_conda=con_env, path_pip=pip_env, path_lock=pnv_env, path_out_val=csv, path_out_dep=dep_check, dependency_to_check=dpn)], local_scheduler=True, detailed_summary=True)

    if args.tree:
        build([tree(path_conda=con_env, path_pip=pip_env, path_lock=pnv_env, path_out_val=csv, path_out_tree=dep_tree)], local_scheduler=True, detailed_summary=True)

    if args.all:
        build([VennGraph(path_conda=con_env, path_pip=pip_env, path_lock=pnv_env, path_out_plot=vdg),
               Validation(path_conda=con_env, path_pip=pip_env, path_lock=pnv_env, path_out_val=csv),
               checkDependency(path_conda=con_env, path_pip=pip_env, path_lock=pnv_env, path_out_val=csv, path_out_dep=dep_check),
               tree(path_conda=con_env, path_pip=pip_env, path_lock=pnv_env, path_out_val=csv, path_out_tree=dep_tree),
               checkDependency(dependency_to_check=dpn)],
              local_scheduler=True, detailed_summary=True)