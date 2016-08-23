#!/usr/bin/env python3

import subprocess


def graph(size, title, values):
    HEADER = '\033[1;37m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    FAIL = '\033[91m'
    NORMAL = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

    title = " "[:]*5 + title + " "[:]*5 
    print (HEADER + title.center(size+20, "#"))

    for row in values:
        value = round(float(row[0][:-1]))*size/100
        for i in range(size):
            if i < value:
                print (YELLOW + "▉", end="")
            else:
                print (YELLOW + "░", end="")

        print (NORMAL + " " + row[0].rjust(4) + " - " + row[1])

def deviceUsage(resource, device=None):
    if resource == "CPU":
        cmd = "cat /proc/stat | awk '/cpu[0-9]/ {value=($2+$4)*100/($2+$4+$5); printf (\" %2.2f%% %s\\n\",value, $1) }'"
        #cmd = "cat /proc/stat | awk '/cpu[0-9]/ {value=($2+$4)*100/($2+$4+$5); printf (\"%s%s\", value, $1) }'"
    elif resource == "storage":
        cmd = "df -h | awk '/sda/ {printf (\"%5s %6s\\n\", $5, $6)}'"

    p = subprocess.Popen(cmd, 
            shell=True, 
            stdout=subprocess.PIPE, 
            stderr=subprocess.STDOUT,
            universal_newlines = True)

    process = []
    for line in p.stdout.readlines():
        detail = line.strip()
        process.append(detail.split())
    retval = p.wait()

    return process


cpu = deviceUsage("CPU")
storage=deviceUsage("storage")

graph(40, "Storage", storage)
print()
graph(40, "CPU", cpu)
