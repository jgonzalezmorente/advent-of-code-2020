with open('input.txt') as input_file:
    input = [int(n.strip()) for n in input_file]


# Primera parte
print('==================== PRIMERA PARTE ====================')

def is_sum_of(n, list):

    list.sort()
    i = 0
    j = len(list) - 1

    while (i < j):
        if (list[i] + list[j] == n):
            return list[i], list[j]
        elif (list[i] + list[j] < n):
            i+=1
        else:
            j-=1
    
    return None


preamble_length = 25
i = 0
j = preamble_length

for n in input[preamble_length:]:
    if not is_sum_of(n, input[i:j].copy()):
        break
    i+=1
    j+=1

print(n)


# Segunda parte
print('==================== SEGUNDA PARTE ====================')

def search_subset(liminf):
    s = 0
    for limsup in range(liminf + 2, input.index(n)):
        if not s:
            s = sum(input[liminf:limsup])
        else:
            s+= input[limsup - 1]
        if s == n:
            return input[liminf:limsup]
    return []

for liminf in range(len(input)-1):
    subset = search_subset(liminf)
    if subset:
        break

print(min(subset) + max(subset))




        
