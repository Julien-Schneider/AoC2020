import helper

data = [(x[0], int(x[1:])) for x in helper.get_input(12).split("\n")[:-1]]

print((fun := lambda instr, x, y, d: abs(x) + abs(y) if not instr else fun(instr[1:], *{
    "N": (x, y+instr[0][1], d), "S": (x, y-instr[0][1], d), "E": (x+instr[0][1], y, d),
    "W": (x-instr[0][1], y, d), "L": (x, y, (d+instr[0][1]//90)%4), "R": (x, y, (d-instr[0][1]//90)%4),
    "F": (x+[1, 0, -1, 0][d] * instr[0][1], y+[0, 1, 0, -1][d] * instr[0][1], d)
}[instr[0][0]]))(data, 0, 0, 0))
# 1010

print((fun := lambda instr, wx, wy, x, y: abs(x) + abs(y) if not instr else fun(instr[1:], *{
    "N": (wx, wy+instr[0][1], x, y), "S": (wx, wy-instr[0][1], x, y), "E": (wx+instr[0][1], wy, x, y), "W": (wx-instr[0][1], wy, x, y),
    "L": (wx*[1, 0, -1, 0][(instr[0][1]//90)%4] + wy*[0, -1, 0, 1][(instr[0][1]//90)%4], wx*[0, 1, 0, -1][(instr[0][1]//90)%4] + wy*[1, 0, -1, 0][(instr[0][1]//90)%4], x, y),
    "R": (wx*[1, 0, -1, 0][(instr[0][1]//90)%4] + wy*[0, 1, 0, -1][(instr[0][1]//90)%4], wx*[0, -1, 0, 1][(instr[0][1]//90)%4] + wy*[1, 0, -1, 0][(instr[0][1]//90)%4], x, y),
    "F": (wx, wy, x+wx*instr[0][1], y+wy*instr[0][1])
}[instr[0][0]]))(data, 10, 1, 0, 0))
# 52742
