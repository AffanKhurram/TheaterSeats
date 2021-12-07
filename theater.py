import sys
import os

file_name = sys.argv[1]

seats = ['e' * 20] * 10
empty = [20 for i in range(10)]
assigned = {}

with open(file_name, 'r') as f:
    lines = f.read().splitlines()
    for line in lines:
        sp = line.split()
        identifier = sp[0]
        num = int(sp[1])

        placed = False
        # find the first row that I can put them into
        max_empty = 0
        for idx, i in enumerate(empty):
            # If I can put them into this row
            if empty[idx] >= num:
                placed = True
                start = seats[idx].index('e')
                buffer = min(3, 20 - (start + num))
                seats[idx] = seats[idx][:start] + ('t' * (num + buffer)) + seats[idx][start+num:]
                empty[idx] -= num + buffer
                assigned_seats = [chr(ord('A') + idx) + str(j) for j in range(start+1, start+num+1)]
                assigned[identifier] = assigned_seats
                break
            # elif empty[idx] > 
        # Otherwise, try to break up the group
        if not placed:
            pass
        
p = ''
for key, val in assigned.items():
    p += key + ' ' + ','.join(val) + '\n'

with open('out.txt', 'w') as f:
    f.write(p)

print(os.path.abspath('out.txt'))