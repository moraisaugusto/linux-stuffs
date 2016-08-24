#!/usr/bin/env python3 

import sys
import os

def main(argv):
    size = argv[1].split("=")
    size = size[1]

    title = argv[2].split("=")
    title = title[1]

    HEADER = '\033[1;37m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    FAIL = '\033[91m'
    NORMAL = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

    contact = BOLD +"Server Configured by:\n \t"+BLUE+"Augusto Morais <aflavio at gmail.com>\n"+ NORMAL
    os.system("clear")

    title = "figlet -fsmall -w" + size + " '" + title + "'" 
    params = "--size=" + size + " --cpu --memory --storage=sda --lastlogins --distroDetail"
    os.system(title + " &&  echo '" + contact + "' && ./server-status.py " + params)

if __name__ == "__main__":
    main(sys.argv)
