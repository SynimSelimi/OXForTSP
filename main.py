# Ordered Crossover Operator
# https://www.hindawi.com/journals/cin/2017/7430125/
import random
import collections

def crossover(p1, p2, with_placement = False):
    c1 = [0] * len(p1)
    
    numbers = random.sample(range(1, len(p1) - 1), 2)
    numbers.sort()
    [a, b] = numbers
    [a, b] = [2, 4]

    for e in range(a, b + 1):
        c1[e] = p1[e]
        
    remaining = list(set(p2) - set(c1))

    p2_r = collections.deque(p2)
    p2_r.rotate(len(p2) - b - 1)
    p2_r = list(p2_r)

    print("cutoff", f"{a}:{b}", p1[a:b+1], b - a)
    print("remaining", remaining)

    
    i = b + 1 if with_placement else 0
    for el in p2_r:
        if el in remaining:
            c1[i] = el
            if with_placement:
                end_of_array = i == len(p2) - 1
                i = 0 if end_of_array else i + 1
            else:
                cutoff = i == (a - 1)
                i = b + 1 if cutoff else i + 1

    return c1

p1 = [7, 3, 1, 8, 2, 4, 6, 5]
p2 = [4, 3, 2, 8, 6, 7, 1, 5]

# p1 = [3, 4, 8, 2, 7, 1, 6, 5]
# p2 = [4, 2, 5, 1, 6, 8, 3, 7]

c1 = crossover(p1, p2)
print("p1: ", p1)
print("p2: ", p2)
print("c1: ", c1)
