import csv

"""
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.
Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""

callers = []
whitelist = []


def D_list(input):
    """Remove duplicates from the given list"""
    return list(set(input))


with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    for text in list(reader):
        sending, receiving, timestamp = text
        whitelist.extend([sending, receiving])

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    for call in list(reader):
        calling, receiving, timestamp, seconds = call
        callers.append(calling)
        whitelist.append(receiving)


callers = D_list(callers)
whitelist = D_list(whitelist)


sus = set(callers).difference(whitelist)

print('These numbers could be telemarketers:')
for phone_number in sorted(sus):
    print(phone_number)