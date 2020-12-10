import helper
from functools import lru_cache

data = [0] + sorted([int(x) for x in helper.get_input(10).split("\n")[:-1]])

print((t:=[y - x for x, y in zip(data, data[1:] + [max(data) + 3])]).count(1) * t.count(3))
# 2400

print((fun:= lru_cache(lambda i: 1 if data[i] == max(data) else sum([fun(i+j+1) * ((data[i+j+1] - data[i]) <= 3) for j, _ in enumerate(data[i+1:i+4])])))(0))
# 338510590509056
