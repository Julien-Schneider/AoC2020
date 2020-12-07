import itertools as it
import helper

data = helper.get_input(4).split("\n\n")[:-1]

def val_byr(val, ignore=False):
    val = int(val)
    if 1920 <= val <= 2002:
        return True
    else:
        return False

def val_iyr(val, ignore=False):
    val = int(val)
    if 2010 <= val <= 2020:
        return True
    else:
        return False

def val_eyr(val, ignore=False):
    val = int(val)
    if 2020 <= val <= 2030:
        return True
    else:
        return False

def val_hgt(val, ignore=False):
    val, unit = int(val[:-2]), val[-2:]
    if unit == "cm":
        vmin = 150
        vmax = 193
    elif unit == "in":
        vmin = 59
        vmax = 76
    else:
        return False

    if vmin <= val <= vmax:
        return True
    else:
        return False

def val_hcl(val, ignore=False):
    if len(val) != 7:
        return False
    vchars = set("0123456789abcdef")
    val = set(val[1:])
    return val.issubset(vchars)
    

def val_ecl(val, ignore=False):
    vecl = {"amb", "blu", "brn", "gry", "grn", "hzl", "oth"}
    return val in vecl

def val_pid(val, ignore=False):
    if len(val) != 9:
        return False
    int(val)
    return True

def val_cid(val, ignore=True):
    return True

fields = {"byr": val_byr,
          "iyr": val_iyr, 
          "eyr": val_eyr,
          "hgt": val_hgt,
          "hcl": val_hcl,
          "ecl": val_ecl,
          "pid": val_pid,
          }
c = 0
print(len(data))
for passport in data:
    passport = passport.replace("\n", " ")
    passport = {x.split(":", 1)[0]: x.split(":", 1)[1] for x in passport.split(" ") if x[:3] != "cid"}
    if len(passport) != 7:
        continue
    for field in fields:
        try:
            if not fields[field](passport[field]):
                break
        except:
            break
    else:
        c += 1
print(c)
