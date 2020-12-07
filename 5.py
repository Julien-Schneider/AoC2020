import helper

data = helper.get_input(5).split("\n")[:-1]

print(max(8 * int(code[:7].translate(str.maketrans("BF", "10")), 2) + int(code[7:].translate(str.maketrans("RL", "10")), 2) for code in data))
# 998

print((start:=-100)*0 + (temp := sorted([8 * int(code[:7].translate(str.maketrans("BF", "10")), 2) + int(code[7:].translate(str.maketrans("RL", "10")), 2) for code in data]))[[start - (start:=seat) for seat in (temp)].index(-2)]-1)
# 676
