from os import path
from re import findall
from funcs import run_crack


run_crack(int(findall('[0-9]+', path.basename(__file__))[0]))
