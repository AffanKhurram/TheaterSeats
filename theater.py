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
            
        # Otherwise, try to break up the group
        if not placed:
            empty_t = []
            for index, e in enumerate(empty):
                empty_t.append((index, e))
            empty_t.sort(key=lambda x: x[1], reverse=True)
            num_left = num
            for index, e in empty_t:
                if num_left <= 0:
                    break
                if e > num_left:
                    start = seats[index].index('e')
                    buffer = min(3, 20 - (start + num_left))
                    seats[index][:start] + ('t' * (num_left + buffer)) + seats[index][start+num_left:]
                    empty[index] -= num_left
                    assigned_seats = [chr(ord('A') + index) + str(j) for j in range(start+1, start+num_left+1)]
                    assigned[identifier] = assigned_seats
                else:
                    num_left = max(0, num_left - e)
                    start = seats[index].index('e')
                    buffer = min(3, 20 - (start + e - num_left))
                    seats[index][:start] + ('t' * (e-num_left + buffer)) + seats[index][start+e-num_left:]
                    empty[index] -= e - num_left
                    assigned_seats = [chr(ord('A') + index) + str(j) for j in range(start+1, start+e-num_left+1)]
                    assigned[identifier] = assigned_seats
            



p = ''
for key, val in assigned.items():
    p += key + ' ' + ','.join(val) + '\n'

with open('out.txt', 'w') as f:
    f.write(p)

print(os.path.abspath('out.txt'))