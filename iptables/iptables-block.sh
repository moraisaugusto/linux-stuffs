#!/bin/bash

# Get all blocked IPs
BLOCKDB="blocked.ips"
#BLOCKDB="connected-SMTP.log"

#Drop only http requests
IPS=$(grep -Ev "^#" $BLOCKDB)
for i in $IPS
do
    iptables -A INPUT -p tcp -s $i --dport 80 -j DROP
done



# Force SYN packets check
iptables -A INPUT -p tcp ! --syn -m state --state NEW -j DROP

#Force Fragments packets check
iptables -A INPUT -f -j DROP

#XMAS packets
iptables -A INPUT -p tcp --tcp-flags ALL ALL -j DROP

#DROP all NULL packets
iptables -A INPUT -p tcp --tcp-flags ALL NONE -j DROP


