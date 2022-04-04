

import random
import timeit
import cProfile


# first option
def max_neg_elem(min_, max_, size):
    MIN = min_
    MAX = max_
    SIZE = size
    array = [random.randint(MIN, MAX) for _ in range(SIZE)]
    i = 0
    index = -1
    for i in range(len(array)):
        if array[i] < 0 and index == -1:
            index = i

        elif 0 > array[i] > array[index]:
            index = i
        i += 1

    if index != -1:
        return index

print(timeit.timeit('max_neg_elem(-10, -1, 100)', number=10000, globals=globals()))       # 2.945386476                           
print(timeit.timeit('max_neg_elem(-100, -1, 100)', number=10000, globals=globals()))      # 2.921355809
print(timeit.timeit('max_neg_elem(-1000, -1, 100)', number=10000, globals=globals()))     # 3.072040997
print(timeit.timeit('max_neg_elem(-10000, -1, 100)', number=10000, globals=globals()))    # 3.014964291
print(timeit.timeit('max_neg_elem(-100000, -1, 100)', number=10000, globals=globals()))   # 3.1126099089999997
print(timeit.timeit('max_neg_elem(-1000000, -1, 100)', number=10000, globals=globals()))  # 2.9872058399999997


cProfile.run('max_neg_elem(-1000000000000, 1000000000000, 1000000)')

'''
         3000006 function calls in 3.395 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.008    0.008    3.395    3.395 <string>:1(<module>)
        1    0.882    0.882    3.387    3.387 ex_1.py:9(max_neg_elem)
  1000000    1.814    0.000    1.923    0.000 random.py:175(randrange)
  1000000    0.533    0.000    2.456    0.000 random.py:238(randint)
        1    0.000    0.000    0.000    0.000 {len}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
  1000000    0.109    0.000    0.109    0.000 {method 'random' of '_random.Random' objects}
        2    0.049    0.025    0.049    0.025 {range}
'''
# second option

def max_neg_elem(min_, max_, size):
    MIN = min_
    MAX = max_
    SIZE = size
    array = [random.randint(MIN, MAX) for _ in range(SIZE)]
    min_negative = 0
    max_negative = 0

    for numb in array:
        if min_negative > numb:
            min_negative = numb
    max_negative = min_negative

    for numb in array:
        if numb > min_negative:
            max_negative = numb
            min_negative = max_negative
            

    return max_negative
    



print(timeit.timeit('max_neg_elem(-10, -1, 100)', number=10000, globals=globals()))      # 2.940320692
print(timeit.timeit('max_neg_elem(-100, -1, 100)', number=10000, globals=globals()))     # 3.154200708
print(timeit.timeit('max_neg_elem(-1000, -1, 100)', number=10000, globals=globals()))    # 3.203120707
print(timeit.timeit('max_neg_elem(-10000, -1, 100)', number=10000, globals=globals()))   # 2.866443597
print(timeit.timeit('max_neg_elem(-100000, -1, 100)', number=10000, globals=globals()))  # 2.638366982000001
print(timeit.timeit('max_neg_elem(-1000000, -1, 100)', number=10000, globals=globals())) # 2.891487992


cProfile.run('max_neg_elem(-1000000000000, 1000000000000, 1000000)')
'''
         3000004 function calls in 3.176 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.007    0.007    3.176    3.176 <string>:1(<module>)
        1    0.575    0.575    3.169    3.169 ex_1.py:53(max_neg_elem)
  1000000    1.926    0.000    2.024    0.000 random.py:175(randrange)
  1000000    0.539    0.000    2.563    0.000 random.py:238(randint)
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
  1000000    0.098    0.000    0.098    0.000 {method 'random' of '_random.Random' objects}
        1    0.031    0.031    0.031    0.031 {range}


'''
# third option

def max_neg_elem(min_, max_, size):
    MIN = min_
    MAX = max_
    SIZE = size
    array = [random.randint(MIN, MAX) for _ in range(SIZE)]
    ready =  max(array)
    return ready


print(timeit.timeit('max_neg_elem(-10, -1, 100)', number=10000, globals=globals()))      # 2.627704127
print(timeit.timeit('max_neg_elem(-100, -1, 100)', number=10000, globals=globals()))     # 2.6507939849999995
print(timeit.timeit('max_neg_elem(-1000, -1, 100)', number=10000, globals=globals()))    # 2.9339211260000004
print(timeit.timeit('max_neg_elem(-10000, -1, 100)', number=10000, globals=globals()))   # 2.9235756140000007
print(timeit.timeit('max_neg_elem(-100000, -1, 100)', number=10000, globals=globals()))  # 3.0911728709999995
print(timeit.timeit('max_neg_elem(-1000000, -1, 100)', number=10000, globals=globals())) # 2.8686442140000015


cProfile.run('max_neg_elem(-1000000000000, 1000000000000, 1000000)')

'''
         3000005 function calls in 2.824 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.008    0.008    2.824    2.824 <string>:1(<module>)
        1    0.426    0.426    2.816    2.816 ex_1.py:105(max_neg_elem)
  1000000    1.706    0.000    1.805    0.000 random.py:175(randrange)
  1000000    0.511    0.000    2.316    0.000 random.py:238(randint)
        1    0.043    0.043    0.043    0.043 {max}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
  1000000    0.099    0.000    0.099    0.000 {method 'random' of '_random.Random' objects}
        1    0.031    0.031    0.031    0.031 {range}
'''



