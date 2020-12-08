import helper

data = helper.get_input(8).split("\n")

print((fun:= lambda i, acc, visited: acc if i in visited else fun(*{
        "nop": lambda i, acc, val: (i+1, acc),
        "acc": lambda i, acc, val: (i+1, acc + int(val)),
        "jmp": lambda i, acc, val: (i+int(val), acc)
        }[data[i][:3]](i, acc, data[i][3:]), visited | {i}))(0, 0, set()))
# 1928

print(max([(fun:= lambda i, acc, visited, inst: (i, acc) if i in visited else fun(*{
        "nop": lambda i, acc, val: (i+1, acc),
        "acc": lambda i, acc, val: (i+1, acc + int(val)),
        "jmp": lambda i, acc, val: (i+int(val), acc),
        "": lambda i, acc, val: (i, acc)
        }[inst[i][:3]](i, acc, inst[i][3:]), visited | {i}, inst))(0, 0, set(), data[:i] + [["nop", "jmp"][line[:3]=="nop"] + line[3:]] + data[i+1:]) for i, line in enumerate(data[:-1])])[1])
# 1319
