import helper
from math import prod
import sys
sys.setrecursionlimit(1500)

t, data, _ = helper.get_input(13).split("\n")

print(prod(min([(int(x) - int(t)%int(x), int(x)) for x in data.split(",") if x!="x"])))
# 3269

data = [(int(x), i%int(x)) for i, x in enumerate(data.split(",")) if x != "x"]
print((fun:= lambda v, t, i, l: t-i if (len(v) == 1 and l != 0) else fun(v, t+i, i, l) if v[0][0] - (t % v[0][0]) != v[0][1] else fun(*[(v, t+i, i, t), (v[1:], t, t - l, 0)][l != 0]))(data[1:], data[0][1], data[0][0], 0))
# 672754131923874
