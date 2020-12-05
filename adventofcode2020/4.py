import fileinput
import re

lines = [line.strip() for line in fileinput.input()]

passwords = [{}]
for line in lines:
    if line == '':
        passwords.append({})
    for code in line.split():
        key, value = code.split(':')
        passwords[len(passwords)-1][key] = value

required = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']


def valid_required(fields):
    return all([r in fields for r in required])


def valid_hgt(hgt):
    if re.fullmatch('(\\d+)(cm|in)', hgt):
        value, unit = re.findall('(\\d+)(cm|in)', hgt)[0]
        return (unit == 'cm' and 150 <= int(value) <= 193
                or unit == 'in' and 59 <= int(value) <= 76)
    return False


def valid_hcl(v):
    return re.fullmatch('#[0-9a-f]{6}', v)


def valid_ecl(v):
    return re.fullmatch('amb|blu|brn|gry|grn|hzl|oth', v)


def valid_pid(v):
    return re.fullmatch('\\d{9}', v)


def valid_num(v, mi, ma):
    return re.fullmatch('\\d+', v) and mi <= int(v) <= ma


def valid_password(password):
    return bool(valid_required(password)
                and valid_num(password['byr'], 1920, 2002)
                and valid_num(password['iyr'], 2010, 2020)
                and valid_num(password['eyr'], 2020, 2030)
                and valid_hgt(password['hgt'])
                and valid_hcl(password['hcl'])
                and valid_ecl(password['ecl'])
                and valid_pid(password['pid']))


p1 = sum([valid_required(p) for p in passwords])
p2 = sum([valid_password(p) for p in passwords])

print(p1, p2)
