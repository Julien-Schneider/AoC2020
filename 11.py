import helper
from itertools import product, chain

data = [[{"L": 0, ".": None}[x] for x in line] for line in helper.get_input(11).split("\n")[:-1]]

print(list(chain(*(fun:= lambda seats: new_seats if (new_seats:= [[{None: lambda c: None, 1: lambda c: c < 4, 0: lambda c: c == 0}[seats[y][x]]([seats[y+dy][x+dx] for dx, dy in product((0, 1, -1), (0, 1, -1)) if 0 <= y+dy < len(seats) and 0 <= x+dx < len(seats[0])][1:].count(1)) for x in range(len(seats[0]))] for y in range(len(seats))]) == seats else fun(new_seats))(data))).count(1))
# 2481

print(list(chain(*(fun:= lambda seats: new_seats if (new_seats:= [[{None: lambda c: None, 1: lambda c: c < 5, 0: lambda c: c == 0}[seats[y][x]](sum((explore:= lambda dx, dy, x, y, seats: 0 if not 0 <= x+dx < len(seats[0]) or not 0 <= y+dy < len(seats) else explore(dx, dy, x+dx, y+dy, seats) if seats[y+dy][x+dx] is None else seats[y+dy][x+dx])(dx, dy, x, y, seats) for dx, dy in list(product((0, 1, -1), (0, 1, -1)))[1:])) for x in range(len(seats[0]))] for y in range(len(seats))]) == seats else fun(new_seats))(data))).count(1))
# 2227
