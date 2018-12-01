"""Runs the run_crack function from ./funcs.py and
starts from a different point in the manglers file
based off of its file name(i.e. crack1.py starts from line 1)"""
from os import path
from re import findall
from funcs import run_crack


run_crack(int(findall('[0-9]+', path.basename(__file__))[0]))
