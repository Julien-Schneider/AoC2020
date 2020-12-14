import helper
import re

data = helper.get_input(2)

expr = r"(\d+)-(\d+) ([a-z]): (.+)"

print(sum(int(n1) <= pwd.count(s) <= int(n2) for n1, n2, s, pwd in re.findall(expr, data)))
# 582

print(sum((pwd[int(n1)-1]+pwd[int(n2)-1]).count(s) == 1 for n1, n2, s, pwd in re.findall(expr, data)))
# 729
