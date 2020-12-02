
from collections import Counter
from operator import xor

def convertPassword(p):
    result = {}
    l = p.strip().split()
    result['min'] = int(l[0].split('-')[0])
    result['max'] = int(l[0].split('-')[1])
    result['char'] = l[1][:-1]
    result['password'] = l[2]
    return result

def isOk(p):
    counter = Counter(p['password'])[p['char']]
    return (counter >= p['min'] and counter <= p['max'])

def isOk2(p):
    try:
        i = p['min'] - 1
        j = p['max'] - 1
        return xor(p['password'][i] == p['char'], p['password'][j] == p['char'])
    except:
        return False

if __name__ == '__main__':

    with open('input.txt') as input:
        passwords = [convertPassword(p) for p in input]

    # Primera parte
    print('==================== PRIMERA PARTE ====================')


    
    passwordChecked = map(isOk, passwords)
    print(sum(passwordChecked))



    # Segunda parte
    print('==================== SEGUNDA PARTE ====================')


    passwordChecked = map(isOk2, passwords)
    print(sum(passwordChecked))
