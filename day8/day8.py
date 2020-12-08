from copy import deepcopy

# Primera parte
print('==================== PRIMERA PARTE ====================')

    
with open('input.txt') as input:

    program = []
    for i in input:            
        instruction = i.strip().split()
        instruction[1] = int(instruction[1])
        instruction.append(False)
        program.append(instruction)
    

def run_program(program, pointer=0, accumulator=0):
    if pointer < len(program):
        instruction = program[pointer]
    else:
        return (accumulator, pointer)

    if instruction[-1]:
        return (accumulator, pointer)
    
    instruction[-1] = True

    if instruction[0] == 'nop':        
        return run_program(program, pointer + 1, accumulator)

    elif instruction[0] == 'acc':
        return run_program(program, pointer + 1, accumulator + instruction[1])

    elif instruction[0] == 'jmp':
        return run_program(program, pointer + instruction[1], accumulator)


print(run_program(deepcopy(program)))

# Segunda parte
print('==================== SEGUNDA PARTE ====================')

for i, p in enumerate(program):

    if (p[0] == 'nop' or p[0] == 'jmp'):
        program_ = deepcopy(program)

        if program_[i][0] == 'nop':            
            program_[i][0] = 'jmp'

        elif program_[i][0] == 'jmp':
            program_[i][0] = 'nop'
        
        accumulator, pointer = run_program(program_)
        if pointer == len(program):
            break

print(accumulator)

        



    


    



        
        