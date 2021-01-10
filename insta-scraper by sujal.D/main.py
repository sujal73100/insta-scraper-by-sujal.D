



Green_Font = '\u001b[32m'
Magenta_Font = '\u001b[35m'
Reset_Font = '\033[0m'

print (Green_Font + "=====================================================================")
print                ("Insta Information Gathering - by Sujal Darode")
print ("=====================================================================")

print  (Magenta_Font + "######  #   #  ###### #######     #           #######                                ")
print  (               "  #     ##  #  #         #       # #          #                                      ")
print  (               "  #     # # #  ######    #      #####         #   ###                                ")
print  (               "  #     #  ##       #    #     #     #     O  #   # #                                ") 
print  (               "######  #   #  ######    #    #       #       #######    version:1.1  by:Sujal Darode" + Reset_Font)
    



#!/bin/env python3

import os, sys
sys.path.append(os.getcwd()+"/.lib/")
import argparse
from api import *

ap = argparse.ArgumentParser()
ap.add_argument("-u", "--user", required=True, help="username of account to scan")
ap.add_argument("-p", "--post", action="store_true", help="image info of user uploads")
args = vars(ap.parse_args())
	
os.system("clear")

if args['user']:
	user_info(usrname=args["user"])

if args['post']:
	post_info()
