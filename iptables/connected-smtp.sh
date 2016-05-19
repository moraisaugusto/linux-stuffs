netstat -plane |grep :25 |  awk '{print $5}' > connected-SMTP.log
