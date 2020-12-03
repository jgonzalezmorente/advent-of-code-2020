from operator import mul
from functools import reduce

class CycleList(object):
    
    def __init__(self, list_base):

        self.list_base = tuple(list_base)
        self.long_base = len(list_base)
    
    def get(self, index):
        
        index = index % self.long_base
        return self.list_base[index]


def get_num_trees(area, right=3, down=1):
    num_trees = 0
    
    y_pointer = x_pointer = 0
    while (y_pointer < len(area)):
        if (x_pointer % right == 0):            
            if (area[y_pointer].get(x_pointer) == '#'):
                num_trees += 1
            y_pointer += down
        x_pointer += 1
    
    return num_trees



if __name__ == '__main__':

    with open('input.txt') as input:
        area = tuple([CycleList(p.strip()) for p in input])
        

    # Primera parte
    print('==================== PRIMERA PARTE ====================')

    print(get_num_trees(area))


    # Primera parte
    print('==================== SEGUNDA PARTE ====================')

    slopes = [(1,1), (3,1), (5,1), (7,1), (1,2)]

    print(reduce(mul, (map(lambda s: get_num_trees(area, s[0], s[1]), slopes))))