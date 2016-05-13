#!/bin/bash

RED='\033[0;31m'
BLUE='\033[0;34m'
GREEN='\033[1;032m'
NC='\033[0m' 

iptables_file="/etc/iptables.up.rules"
iptables_file_up="/etc/network/if-pre-up.d/iptables"


if [ ! -f $iptables_file ]; then
    iptables-save > $iptables_file

    if [ ! -f $iptables_file_up ]; then
        iptables-restore < $iptables_file
    fi 
else
    printf "${GREEN}Already exists an iptable rule file${NC}\n"
    printf "Please, check it manually\n"
    exit
fi
