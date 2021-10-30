# Ordered Crossover Operator
# https://www.hindawi.com/journals/cin/2017/7430125/
import random
import collections

p1 = [7, 3, 1, 8, 2, 4, 6, 5]
p2 = [4, 3, 2, 8, 6, 7, 1, 5]

c1 = [0] * len(p1)

numbers = random.sample(range(1, len(p1) - 1), 2)
numbers.sort()
[a, b] = numbers

print("cutoff", numbers)

for e in range(a, b + 1):
    c1[e] = p1[e]

for e in range(a, b + 1):
    c1[e] = p1[e]
    
remaining = list(set(p2) - set(c1))

p2_r = collections.deque(p2)
p2_r.rotate(b - 1)
p2_r = list(p2_r)
print(p2_r)

i = 0
for el in p2_r:
    if el in remaining:
        c1[i] = el
        if i == a - 1:
            i = b + 1
        else:
            i += 1

print("p1: ", p1)
print("p2: ", p2)
print("c1: ", c1)
