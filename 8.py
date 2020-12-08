import helper

d = helper.get_input(8).split("\n")

print((f:= lambda i, a, v: a if i in v else f(*{
        "n": lambda i, a, w: (i+1, a),
        "a": lambda i, a, w: (i+1, a + int(w)),
        "j": lambda i, a, w: (i+int(w), a)
        }[d[i][0]](i, a, d[i][3:]), v | {i}))(0, 0, set()))
# 1928

print(max([(f:= lambda i, a, v, c: (i, a) if i in v else f(*{
        "n": lambda i, a, w: (i+1, a),
        "a": lambda i, a, w: (i+1, a + int(w)),
        "j": lambda i, a, w: (i+int(w), a),
        "": lambda i, a, w: (i, a)
        }[c[i][:1]](i, a, c[i][3:]), v | {i}, c))(0, 0, set(), d[:i] + [["nop", "jmp"][l[0]=="n"] + l[3:]] + d[i+1:]) for i, l in enumerate(d[:-1])])[1])
# 1319
