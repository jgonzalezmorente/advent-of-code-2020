#%%
with open('input.txt') as input_file:
    actions = []
    for i in input_file:
        action = i.strip()
        actions.append((action[0], int(action[1:])))

#%%

# Primera parte
print('==================== PRIMERA PARTE ====================')

direction = (1, 0)
position = (0, 0)

for action in actions:
    if action[0] == 'N':
        position = (position[0], position[1] + action[1])

    elif action[0] == 'S':
        position = (position[0], position[1] - action[1])

    elif action[0] == 'W':
        position = (position[0] - action[1], position[1])

    elif action[0] == 'E':
        position = (position[0] + action[1], position[1])

    elif action[0] == 'L':
        rotations = (action[1] // 90) % 4
        for _ in range(rotations):            
            direction = (-direction[1], direction[0])
    
    elif action[0] == 'R':
        rotations = (action[1] // 90) % 4
        for _ in range(rotations):
            direction = (direction[1], -direction[0])
    
    elif action[0] == 'F':
        position = (position[0] + action[1] * direction[0], position[1] + action[1] * direction[1])
    
manhattan = abs(position[0]) + abs(position[1])
print(manhattan)

# %%
print('==================== SEGUNDA PARTE ====================')

waypoint = (10, 1)
position = (0, 0)

for action in actions:
    if action[0] == 'N':
        waypoint = (waypoint[0], waypoint[1] + action[1])

    elif action[0] == 'S':
        waypoint = (waypoint[0], waypoint[1] - action[1])

    elif action[0] == 'W':
        waypoint = (waypoint[0] - action[1], waypoint[1])

    elif action[0] == 'E':
        waypoint = (waypoint[0] + action[1], waypoint[1])

    elif action[0] == 'L':
        rotations = (action[1] // 90) % 4
        for _ in range(rotations):            
            waypoint = (-waypoint[1], waypoint[0])
    
    elif action[0] == 'R':
        rotations = (action[1] // 90) % 4
        for _ in range(rotations):
            waypoint = (waypoint[1], -waypoint[0])
    
    elif action[0] == 'F':        
        position = (position[0] + action[1] * waypoint[0], position[1] + action[1] * waypoint[1])
    
manhattan = abs(position[0]) + abs(position[1])
print(manhattan)
# %%
