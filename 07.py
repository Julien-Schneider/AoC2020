import helper
from re import findall as s
from functools import lru_cache as l

d = helper.get_input(7)

print(len(set((f:= lambda n: "|".join(m) + "|" + "|".join(f(x) for x in m) if (m:= s(r"(.+) bags con.*{n}".format(n=n), d)) else n)("shiny gold").split("|"))))
# 272

print(l((f:= lambda n: sum([int(c) * (f(b) + 1) for c, b in e[n]]) if (e:= {t: s(r"(\d)+ ([\w\s]+) bags?", r) for t, r in [x.split(" bags con") for x in d.split("\n")[:-1]]})[n] else 0))("shiny gold"))
# 172246
