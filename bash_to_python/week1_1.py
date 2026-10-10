##!/bin/bash
#for host in web01 web02 db01; do
#  echo "Checking $host"
#done
#echo "Done"

def check_hosts(host):
    print("Checking " + host)

for host in ["web01", "web02", "db01"]:
    check_hosts(host)
print("Done")