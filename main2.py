# Ordered Crossover Operator
# https://www.hindawi.com/journals/cin/2017/7430125/
import random
import collections

def rotate(arr, n):
    r_arr = collections.deque(arr)
    r_arr.rotate(len(arr) - n - 1)
    r_arr = list(r_arr)
    return r_arr

def crossover(p1, p2, with_rotate = False, with_placement = False):
    c1 = [0] * len(p1)
    
    numbers = random.sample(range(1, len(p1) - 1), 2)
    numbers.sort()
    [a, b] = numbers
    [a, b] = [2, 4]

    for e in range(a, b + 1):
        c1[e] = p1[e]
        
    rem = list(set(p2) - set(c1))

    new_rem = []
    p2_r = rotate(p2, b) if with_rotate else p2
    for el in p2_r:
        if el in rem:
            new_rem.append(el)

    print("cutoff", f"{a}:{b}", p1[a:b+1], b - a)
    print("remaining", new_rem)

    i = b + 1 if with_placement else 0
    for el in p2_r:
        if el in new_rem:
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

c1 = crossover(p1, p2, True)
print("p1: ", p1)
print("p2: ", p2)
print("c1: ", c1)
