import helper

data = helper.get_input(5)

print(max(8 * int(code[:7], 2) + int(code[7:], 2) for code in data.translate(str.maketrans("BFRL", "1010")).split("\n")[:-1]))
# 998

print((seats := sorted(8 * int(code[:7], 2) + int(code[7:], 2) for code in data.translate(str.maketrans("BFRL", "1010")).split("\n")[:-1]))[[x - min(seats) - i for i, x in enumerate(seats)].index(1)]-1)
# 976
