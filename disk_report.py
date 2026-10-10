import os
import shutil

usage_limit = 8

def get_percentage_used(path):
    total, used, free = shutil.disk_usage(path)
    if total == 0:
        return None
    else:
        return round((used / total) * 100)

warn_count = 0
error_count = 0
count = 0

for location in ['/', '/tmp', '/null', '/home']:
    count += 1
    if os.path.exists(location):
        percentage = get_percentage_used(location)
        if percentage is None:
            print(f"ERROR {location}  could not determine usage")
            error_count += 1
        elif percentage > usage_limit:
            print(f"WARN {location}  {percentage}% limit {usage_limit}%")
            warn_count += 1
        else:
            print(f"OK {location}  {percentage}%")
    else:
        print(f"SKIP {location}  does not exist")
        error_count += 1

print(f"Total warnings: {warn_count} out of {count}")
print(f"Total errors: {error_count} out of {count}")