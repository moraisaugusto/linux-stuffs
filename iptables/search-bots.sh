#!/bin/bash

# Config Files
file='suspected.ips'
access_log="mary_access_log"
apache_dir="/var/log/apache2/"
white_list="179.178.174.125"
blocked_ips="blocked.ips"
suspected_requests=("/uploads/2016/04/page.php")


# Getting all suspected Request from access log
for i in "$suspected_requests" 
do
    grep -R $i $apache_dir$access_log | awk '{print $1}' > $file 
done


# Match all IPs with more than 2 requests
awk -v white_list=$white_list '{h[$1]++}; END { for(k in h) if ( h[k] > 1 && k != white_list ) {print k} } ' $file > $blocked_ips 

