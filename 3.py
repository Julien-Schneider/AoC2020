import helper
from functools import reduce

data = helper.get_input(3).split("\n")[:-1]

print(sum([x[3*i % len(x)] == "#" for i, x in enumerate(data)]))
# 225

print(reduce(lambda x, y: x*y, [sum([x[dx*i % len(x)] == "#" for i, x in enumerate(data[::dy])]) for dy, dx in [(1, 1), (1, 3), (1, 5), (1, 7), (2, 1)]]))
# 1115775000
