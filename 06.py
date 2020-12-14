import helper

data = helper.get_input(6)[:-1].split("\n\n")

print(sum(len(set(group.replace("\n", ""))) for group in data))
# 6596

print(sum(len(group[0].intersection(*group[1:])) for group in [[set(x) for x in group.split("\n")] for group in data]))
# 3219
