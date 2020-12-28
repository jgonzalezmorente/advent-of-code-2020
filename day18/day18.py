
from functools import reduce
from operator import mul

def compute(expression):

    expression_list = [c for c in expression if c != ' ']
    if not '(' in expression_list:
        operations = []
        numbers = []
        for index, element in enumerate(expression_list):
            if (index % 2) == 1:
                operations.append(element)
            else:
                numbers.append(int(element))

        def fold(x, y):
            oper = operations.pop(0)
            if oper == '+':
                return x + y
            elif oper == '*':
                return x * y
        
        return reduce(fold, numbers)
    
    else:

        index_open = 0        

        for index, element in enumerate(expression_list):
            if element == '(':
                index_open = index

            if element == ')':
                break

        subexpression = expression_list[index_open + 1: index]
        new_expression = expression_list[:index_open] + [ compute(subexpression) ] 
        index += 1
        if (index < len(expression_list)):
            new_expression += expression_list[index:]
        
        return compute(new_expression)


def compute_p2(expression):

    expression_list = [c for c in expression if c != ' ']
    if not '(' in expression_list and not '+' in expression_list:        
        numbers = []
        for index, element in enumerate(expression_list):
            if (index % 2) == 0:
                numbers.append(int(element))
        return reduce(mul, numbers)

    elif not '(' in expression_list:

        for index, element in enumerate(expression_list):
            if element == '+':
                break
        
        new_expression = expression_list[:index-1] + [int(expression_list[index - 1]) + int(expression_list[index + 1])]
        if (index + 2 < len(expression_list)):
            new_expression += expression_list[index + 2:]
        return compute_p2(new_expression)

    else:

        index_open = 0        

        for index, element in enumerate(expression_list):
            if element == '(':
                index_open = index

            if element == ')':
                break

        subexpression = expression_list[index_open + 1: index]
        new_expression = expression_list[:index_open] + [ compute_p2(subexpression) ]
        index += 1
        if (index < len(expression_list)):
            new_expression += expression_list[index:]
        
        return compute_p2(new_expression)

with open('input.txt') as input_file:
    expressions = [e.strip() for e in input_file]


print('==================== PRIMERA PARTE ====================')

print(compute("2 * 3 + (4 * 5)"))
print(compute("5 + (8 * 3 + 9 + 3 * 4 * 3)"))
print(compute("5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))"))
print(compute("((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2"))

print('Parte 1:', sum(map(compute, expressions)))


print('==================== SEGUNDA PARTE ====================')

print(compute_p2("1 + 2 * 3 + 4 * 5 + 6"))
print(compute_p2("1 + (2 * 3) + (4 * (5 + 6))"))
print(compute_p2("2 * 3 + (4 * 5)"))
print(compute_p2("5 + (8 * 3 + 9 + 3 * 4 * 3)"))
print(compute_p2("5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))"))
print(compute_p2("((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2"))

print('Parte 2:', sum(map(compute_p2, expressions)))
