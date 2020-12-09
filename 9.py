import helper
from itertools import combinations
import time

data = [int(x) for x in helper.get_input(9)[:-1].split("\n")]

print((weakness:=[x for i, x in enumerate(data[25:]) if x not in {z + y for z, y in combinations(data[i:i+25], 2)}][0]))
# 50047984

print([min(data[i:j]) + max(data[i:j]) for i, j in combinations(range(len(data)), 2) if sum(data[i:j]) == weakness][0])
# 5407707
