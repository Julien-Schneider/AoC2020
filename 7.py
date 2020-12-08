import helper
import re
from functools import lru_cache

data = helper.get_input(7)

print(len(set((fun:= lambda name: "|".join(matches) + "|" + "|".join(fun(x) for x in matches) if (matches:= re.findall(r"(.+) bags contain.*{name}".format(name=name), data)) else name)("shiny gold").split("|"))))
# 272

print(lru_cache((fun:= lambda name: sum([int(count) * (fun(bag) + 1) for count, bag in contains[name]]) if (contains:= {target: re.findall(r"(\d)+ ([\w\s]+) bags?", rules) for target, rules in [x.split(" bags contain ") for x in data.split("\n")[:-1]]})[name] else 0))("shiny gold"))
# 172246
