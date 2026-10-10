# #!/bin/bash
# count=0
# for port in 22 80 443 8080; do
#   if [ "$port" -lt 1024 ]; then
#     count=$((count + 1))
#   fi
# done
# echo "Privileged ports: $count"

def count_port(portnum):
    if portnum < 1024:
        return True
    else:
        return False

count = 0
for port in [22, 80, 443, 8080]:
    if count_port(port) == True:
        count = count + 1
print(f"Privileged ports: {count}")
