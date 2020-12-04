
import re 

def convert_passport(passport):
    result = {}

    for d in passport.split():
        kv = d.split(':')
        result[kv[0]] = kv[1]

    return result

def is_num_valid(num, min, max):
    try:
        num_ = int(num)
        if (num_ < min or num_ > max):
            return False
        return True
    except:
        return False


def is_valid(p):
    if set({'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'}).issubset(set(p.keys())):
        # byr
        if not is_num_valid(p['byr'], 1920, 2002):
            return False
        
        # iyr
        if not is_num_valid(p['iyr'], 2010, 2020):
            return False

        #ey4
        if not is_num_valid(p['eyr'], 2020, 2030):
            return False

        #'hgt
        if p['hgt'][-2:] == 'cm':
            if not is_num_valid(p['hgt'][:-2], 150, 193):
                return False
        
        elif p['hgt'][-2:] == 'in':
            if not is_num_valid(p['hgt'][:-2], 59, 76):
                return False
        else:
            return False
        
        #hcl
        pattern = re.compile(r'#[0-9, a-f]{6}')
        if not pattern.match(p['hcl']):
            return False
        
        #ecl
        if not p['ecl'] in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
            return False
        
        #pid
        if not p['pid'].isnumeric() or len(p['pid']) != 9:
            return False
        
        return True
    else:
        return False


if __name__ == '__main__':


    with open('input.txt') as input:
        passports = []
        passport = ''
        for p in input:
            if p[0] == '\n':
                passports.append(convert_passport(passport))
                passport = ''
            else:
                passport += (' ' + p.strip())
        passports.append(convert_passport(passport))



    # Primera parte
    print('==================== PRIMERA PARTE ====================')

    print(sum(map(is_valid, passports)))



    # Primera parte
    print('==================== SEGUNDA PARTE ====================')
