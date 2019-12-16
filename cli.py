#!/usr/bin/env python

import argparse

# required defines a mandatory argument
# default defines a default value if not specified

parser = argparse.ArgumentParser()

### OUTPUTS
### What is the default name/path ? Please Insert Below.
parser.add_argument('-o', '--output', type=str, default='xxxx', dest='output', help="name or path output file for Specified Environment(by -e or --env)")
parser.add_argument('-e', '--env', type=str, dest='env', default='pipenv', help="name of environment for output file")
### What is the default name/path of the dependency tree ? Please Insert Below.
parser.add_argument('-odt', '--out_tree', type=str, default='zxcv', dest='o_dt', help="path of dependency tree")
### What is the default name/path of the Venn Diagram ? Please Insert Below.
parser.add_argument('-vd', '--vdg', type=str, default='zxcv', dest='vdg', help="path of venn diagram")

### INPUT FILE
parser.add_argument('-p', '--plock', type=str, default='Pipfile.lock', dest='plock', help="path of Pipfile.lock")

### Name of Dependency
parser.add_argument('-dp', '--depen', type=str, dest='depen', nargs='*', help="name of dependency to check. if empty string, checks all")


def main():
    args = parser.parse_args()
    # Store desired output file name/path
    output = args.output
    # Store desired env name (default = pipenv)
    env_name = args.env
    # Store name or path of Pipfile.lock
    pipfile_lock = args.plock
    # Store name or path of Dependency Tree
    dep_tree = args.o_dt
    # Store name or path of Venn Diagram
    vn_dgrm = args.vdg
    # Store dependency to check
    if args.depen:
        # list of dependencies to check
        depen = args.depen





#######################################
# To be removed for the final version #
#######################################
# args = parser.parse_args()
#
# # Store desired output file name/path
# output = args.output
# # Store desired env name (default = pipenv)
# env_name = args.env
# # Store name or path of Pipfile.lock
# pipfile_lock = args.plock
# # Store name or path of Dependency Tree
# dep_tree = args.o_dt
# # Store name or path of Venn Diagram
# vn_dgrm = args.vdg
# # Store dependency to check
# if args.depen:
#     # list of dependencies to check
#     depen = args.depen



# if output:
#     if env_name == 'pipenv':
#         asdf = output + ' is in a ' + env_name + ' eeeenvironment !!!'
#         print(asdf)
#         print('lol')
#         txt_file = open(pipfile_lock, 'w')
#         txt_file.write(asdf)
#     elif env_name == 'conda':
#         asdf = output + ' is in a ' + env_name + ' environment !!!'
#         print(output, ' is in a ', 'not in a pipenv ', ' environment !!!')
#         print('lol')
#         txt_file = open(pipfile_lock, 'w')
#         txt_file.write(asdf)


#################################

## python prac_arg.py -h
## python prac_arg.py -o asdf
## python prac_arg.py -o 'asdf'
## python prac_arg.py --output asdf
## python prac_arg.py --output 'asdf'
## python prac_arg.py
## python prac_arg.py -o asdf.py -e conda
## python prac_arg.py -o asdf.py --env conda
## python prac_arg.py -o asdf.py --env conda -p data/pipfileee.txt