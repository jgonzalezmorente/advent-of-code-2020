from copy import deepcopy

with open('input.txt') as input_file:
    input = [list(i.strip()) for i in input_file]

def transform_seat_assignments(number_adjacent_seats, rows=len(input), columns=len(input[0]), occupied_seats=0, lim_occupied_seats=4):    
    
    seat_map = deepcopy(input)

    change_occurs = False
    new_occupied_seats = 0
    for i in range(rows):
        for j in range(columns):
            if input[i][j] == 'L':
                if number_adjacent_seats(i, j, seat_map) == 0:
                    input[i][j] = '#'
                    change_occurs = True
            elif input[i][j] == '#':
                new_occupied_seats+=1
                if number_adjacent_seats(i, j, seat_map) >= lim_occupied_seats:
                    input[i][j] = 'L'
                    change_occurs = True
    
    if change_occurs:
        return transform_seat_assignments(number_adjacent_seats, rows, columns, new_occupied_seats, lim_occupied_seats)
    else:
        return new_occupied_seats
   

# Primera parte
print('==================== PRIMERA PARTE ====================')


def number_adjacent_seats(i, j, seat_map, status='#'):

    result = 0    
    
    try:
        if seat_map[i][j-1] == status and j>=1:
            result+=1
    except:
        pass
            
    try:
        if seat_map[i][j+1] == status:
            result+=1
    except:
        pass

    try:            
        if seat_map[i-1][j] == status and i>=1:
            result+= 1
    except:
        pass

    try:        
        if seat_map[i+1][j] == status:
            result+=1
    except:
        pass

    try:
        if seat_map[i-1][j-1] == status and i>=1 and j>=1:
            result+=1
    except:
        pass
    
    try:
        if seat_map[i-1][j+1] == status and i>=1:
            result+=1
    except:
        pass
    
    try:            
        if seat_map[i+1][j-1] == status and j>=1:
            result+=1
    except:
        pass
            
    try:
        if seat_map[i+1][j+1] == status:
            result+=1
    except:
        pass
    
    return result
            
            
print(transform_seat_assignments(number_adjacent_seats, lim_occupied_seats=4))


# Segunda parte
print('==================== SEGUNDA PARTE ====================')


with open('input.txt') as input_file:
    input = [list(i.strip()) for i in input_file]

def number_adjacent_seats_2(i, j, seat_map, status='#'):
    result = 0    
    
    try:
        k=1
        while (seat_map[i][j-k]=='.' and j>=k):
            k+=1
        if seat_map[i][j-k] == status and j>=k:
            result+=1
    except:
        pass
            
    try:
        k=1
        while (seat_map[i][j+k]=='.'):
            k+=1
        if seat_map[i][j+k] == status:
            result+=1
    except:
        pass

    try:
        k=1
        while (seat_map[i-k][j]=='.' and i>=k):
            k+=1
        if seat_map[i-k][j] == status and i>=k:
            result+= 1
    except:
        pass

    try:        
        k=1
        while (seat_map[i+k][j]=='.'):
            k+=1
        if seat_map[i+k][j] == status:
            result+=1
    except:
        pass

    try:
        k=1
        while (seat_map[i-k][j-k]=='.' and i>=k and j>=k):
            k+=1
        if seat_map[i-k][j-k] == status and i>=k and j>=k:
            result+=1
    except:
        pass
    
    try:
        k=1
        while (seat_map[i-k][j+k]=='.' and i>=k):
            k+=1
        if seat_map[i-k][j+k] == status and i>=k:
            result+=1
    except:
        pass
    
    try:
        k=1
        while (seat_map[i+k][j-k]=='.' and j>=k):
            k+=1
        if seat_map[i+k][j-k] == status and j>=k:
            result+=1
    except:
        pass
            
    try:
        k=1
        while (seat_map[i+k][j+k]=='.'):
            k+=1
        if seat_map[i+k][j+k] == status:
            result+=1
    except:
        pass
    
    return result    

print(transform_seat_assignments(number_adjacent_seats_2, lim_occupied_seats=5))
