"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)



numbers = set()

for text, call in zip(texts, calls):
    for diff in range(0, 2):
        numbers.add(text[diff])
        numbers.add(call[diff])

print(f"{len(numbers)} different telephone numbers are there  in the records.")