
# %%
print('==================== PRIMERA PARTE ====================')

with open('input.txt') as input_file:
    reference_time = int(input_file.readline())
    bus_ids = [ int(id) for id in input_file.readline().split(',') if id != 'x']

bus_departures = map(lambda id: (reference_time - ( reference_time % id ) + id, id), bus_ids)
earliest = min(bus_departures, key=lambda bd: bd[0])

print((earliest[0] - reference_time) * earliest[1])

# %%

print('==================== SEGUNDA PARTE ====================')

with open('input.txt') as input_file:
    reference_time = int(input_file.readline())

    bus_ids = []
    acc = 0
    for id in input_file.readline().split(','):        
        if id != 'x':            
            bus_ids.append([int(id), 1, acc])            
        else:
            bus_ids[-1][1]+=1
        acc+=1
 
#%%
def is_solution(timestamp, ec_lim=None):
    for index, bus_id in enumerate(bus_ids):
        if index == ec_lim:
            break
        if not (timestamp + bus_id[-1]) % bus_id[0] == 0:
            return False        
    return True

idmax = max(bus_ids, key=lambda id: id[0])

n= int((100000000000000 + idmax[-1])/idmax[0]) #100000000000000
s = idmax[0]*n - idmax[-1]
while(not is_solution(s, 6)):
    s+=idmax[0]
print(s)

# %%
from operator import mul
from functools import reduce

m = reduce(mul, [id[0] for id in bus_ids][:6])
# %%
while(not is_solution(s)):
    s+=m
print(s)
# %%
