import helper

data = helper.get_input(4).split("\n\n")[:-1]

print(len([passport for passport in data if all([x in passport for x in ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]])]))
# 200

print(len([passport for passport in data if len((decoded := [x.split(":", 1) for x in passport.replace("\n", " ").split(" ") if x[:3] != "cid"])) >= 7 and all(
         {"cid": lambda val: True,
          "byr": lambda val: 1920 <= int(val) <= 2002,
          "iyr": lambda val: 2010 <= int(val) <= 2020, 
          "eyr": lambda val: 2020 <= int(val) <= 2030,
          "hgt": lambda val: 150 <= int(val[:-2]) <= 193 if val[-2:] == "cm" else 59 <= int(val[:-2]) <= 76,
          "hcl": lambda val: len(val) == 7 and set(val[1:]).issubset("0123456789abcdef"),
          "ecl": lambda val: val in {"amb", "blu", "brn", "gry", "grn", "hzl", "oth"},
          "pid": lambda val: len(val) == 9 and set(val).issubset("0123456789"),
          }[field](value) for field, value in decoded)]))
# 116
