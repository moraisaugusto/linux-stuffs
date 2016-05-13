#!/bin/bash

# Get all blocked IPs
BLOCKDB="blocked.ips"

#Drop only http requests
IPS=$(grep -Ev "^#" $BLOCKDB)
for i in $IPS
do
    iptables -A INPUT -p tcp -s $i --dport 80 -j DROP
done
