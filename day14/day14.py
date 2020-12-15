#%%
import re

def expand_to_bits(number, bits=36):
    return ('{:0' + str(bits) + 'd}').format(int(bin(number)[2:]))

def apply_mask(number, mask):
    binary_number = list(expand_to_bits(number, bits=len(mask)))
    for index, d_mask in enumerate(mask):
        if d_mask != 'X':
            binary_number[index] = d_mask
    
    return int(''.join(binary_number), 2)

def generate_combinations(n, acc=[]):
    if n == 0:
        return acc
    elif not acc:
        new_acc = [['0'], ['1']]
    else: 
        new_acc = []         
        for e in acc:            
            new_acc.append(e[:] + ['0'])
            new_acc.append(e[:] + ['1'])

    return generate_combinations(n-1, new_acc)

def apply_mask2(number, mask):
    binary_number = expand_to_bits(number, bits=len(mask))
    binary_float = list(map(lambda x: x[1] if x[0] == '0' else x[0], zip(mask, binary_number)))
    num_xs = len([x for x in binary_float if x == 'X'])
    combinations = generate_combinations(num_xs)

    result = []
    for c in combinations:
        binary_float_c = binary_float.copy()        
        n = 0
        for index, digit in enumerate(binary_float_c):
            if digit == 'X':
                binary_float_c[index] = c[n]
                n+=1        
        result.append(int(''.join(binary_float_c), 2))
    
    return result
   

#%% 
mask_pattern = re.compile(r'^mask ?= ?.*$')
memory_pattern = re.compile(r'^mem\[\d+\] ?= ?\d+')

mask_memory = []
with open('input.txt') as input_file:
    for line in input_file:
        line = line.strip()
        if mask_pattern.match(line):            
            mask_memory.append({
                'mask': line.split('=')[1].strip(),
                'memory': []
            })
        elif memory_pattern.match(line):
            mem = list(map(lambda x: x.strip(), line.split('=')))
            value = int(mem[1])

            span = re.search(r'\d+]$', mem[0].strip()).span()                      
            key = mem[0][span[0]: span[1] - 1]

            mask_memory[-1]['memory'].append((key, value))
                        
#%%
print('==================== PRIMERA PARTE ====================')

memory = {}
for m in mask_memory:
    for pos in m['memory']:
        memory[pos[0]] = apply_mask(pos[1], m['mask'])

print(sum(memory.values()))

# %%
print('==================== SEGUNDA PARTE ====================')

memory = {}
for m in mask_memory:
    for pos in m['memory']:
        keys = apply_mask2(int(pos[0]), m['mask'])
        for k in keys:
            memory[k] = pos[1]


print(sum(memory.values()))
# %%
