import helper
import itertools as it

data = [int(x) for x in helper.get_input(1).split("\n")[:-1]]

print([x * y for x, y in it.combinations(data, 2) if x + y == 2020][0])
# 290784

print([x * y * z for x, y, z in it.combinations(data, 3) if x + y + z == 2020][0])
# 177337980
