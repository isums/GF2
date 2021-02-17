import requests
import threading
import time
import random

# How many threads the program is gonna run | The more threads the more internet and pc resources are needed.
threads = 100000

# Determines the ID range that will be scanned - Default is 6000000 - 7800000
minrange = 1000000
maxrange = 9800000
# -----------------------
group_ids = [*range(minrange, maxrange)]

random.shuffle(group_ids)
popped_groups = group_ids

results = open('results.txt', 'w')
results.close()

i = 0


def groupthingy():
    current_group = popped_groups.pop()

    try:
        group = requests.get(
            f'https://groups.roblox.com/v1/groups/{current_group}')
        json = group.json()
        if '"isLocked":true' not in group.text:
            if json['owner'] == None:
                if json['publicEntryAllowed'] == True:
                    results = open('results.txt', 'a')
                    results.write(f"Group: {current_group} is claimable!\n Link : https://www.roblox.com/groups/{current_group}/")
                    results.close()
                    print(f"Successfully found a group. Group: {current_group} is claimable!\n")

            else:
                print(f"Group: {current_group} has a owner.")

    except Exception:
        print("Ran into error // Most likely a proxy error.")
        pass


groupthreads = []
for gk in range(threads):
    lt = threading.Thread(target=groupthingy)
    groupthreads.append(lt)
    lt.start()
