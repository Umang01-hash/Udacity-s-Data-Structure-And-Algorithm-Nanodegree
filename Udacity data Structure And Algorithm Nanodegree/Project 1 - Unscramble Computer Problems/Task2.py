

import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""

dialed = {call[0]: int(call[3]) for call in calls}
receives = {call[1]: int(call[3]) for call in calls}
receives_ex_dialed = dict()

for (k, v), (k2, v2) in zip(dialed.items(), receives.items()):
    if k in receives.keys():
        dialed[k] = v + receives[k]
    if k2 not in dialed.keys():
        receives_ex_dialed[k2] = v2

dialed.update(receives_ex_dialed)

maxD = max(dialed, key=lambda key: dialed[key])

print(f"{maxD} spent the longest time, {dialed[maxD]} seconds, on the "
      f"phone during September 2016.")
