##!/bin/bash
#usage=87
#limit=80
#if [ "$usage" -gt "$limit" ]; then
#  echo "Disk usage ${usage}% is over ${limit}%"
#else
#  echo "Disk OK"
#fi

usage = 90
limit = 80
if usage > limit:
    #print("Disk usage " + str(usage) + " is over " + str(limit))
    print(f"Disk usage {usage}% is over {limit}%")
else:
    print("Disk OK")