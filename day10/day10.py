with open('d:\\advent-of-code-2020\\day10\\input.txt') as input_file:
    input = [int(n.strip()) for n in input_file]


# Primera parte
print('==================== PRIMERA PARTE ====================')


input.sort()
input.insert(0,0)
input.append(input[-1] + 3)
input = tuple(input)

dif1 = dif3 = 0
for i in range(len(input) - 1):
    dif = input[i+1] - input[i]
    if dif == 1:
        dif1+=1
    elif dif == 3:
        dif3+=1

print(dif1 * dif3)


# Segunda parte
print('==================== SEGUNDA PARTE ====================')

L = len(input)

from functools import lru_cache

import time

@lru_cache()
def generate_ways(index=0, acc_ways=0):    
    if index == L - 1:        
        return acc_ways + 1
    
    acc_ways_new = acc_ways
    for i in range(index + 1, min(L, index + 4)):            
        if (input[i] - input[index]) <= 3:
            acc_ways_new += generate_ways(i, acc_ways)
        else:
            break
    return acc_ways_new

start_time = time.time()
print(generate_ways())
end_time = time.time()
print( end_time - start_time )


