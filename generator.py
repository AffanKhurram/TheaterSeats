import random

registrations = random.randint(2, 50)

s = ''
for i in range(registrations):
    seats = random.randint(1, 5)
    s += 'R' + str(i) + ' ' + str(seats) + '\n'

with open('in.txt', 'w') as f:
    f.write(s)