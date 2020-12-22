from copy import copy
from tqdm import tqdm

class Cube(object):

    def __init__(self, x, y, z=0, active=False):

        self.x = x
        self.y = y
        self.z = z        

        self.active = active

    def is_neighbors(self, cube):

        return True if (self.x in [cube.x - 1, cube.x, cube.x + 1]
                        and self.y in [cube.y - 1, cube.y, cube.y + 1]
                        and self.z in [cube.z - 1, cube.z, cube.z + 1]                  
                        and self != cube) else False


    def __eq__(self, other):
        return self.x == other.x and self.y == other.y and self.z == other.z 

    def __ne__(self, other):
        return not self.__eq__(other)
    
    def __str__(self):
        return f'({self.x}, {self.y}, {self.z}, {self.active})'

    def __hash__(self):
        return self.x*100 + self.y*10 + self.z
   



class ConwayCubes(object):

    def __init__(self):
        self.cubes = []
        self.last_added_cubes = []
        self._iter = [(x,y,z) for x in range(-1, 2) for y in range(-1, 2) for z in range(-1, 2)]

    def add(self, cube):
        self.cubes.append(cube)
    
    def add_neighbors(self):
        if not self.last_added_cubes:
            self.last_added_cubes = self.cubes
        
        new_cubes = []
        for cube in self.last_added_cubes: #tqdm(self.last_added_cubes, ncols=100):
            neighbors = map(lambda d: Cube(cube.x + d[0], cube.y + d[1], cube.z + d[2]), self._iter)
            #new_cubes.extend(filter(lambda n: not n in new_cubes and not n in self.cubes, neighbors))
            new_cubes.extend(neighbors)
        
        new_cubes = filter(lambda n: not n in self.cubes, set(new_cubes))
        self.cubes.extend(new_cubes)
        self.last_added_cubes = list(new_cubes)

    def get_num_active_neighbors(self, cube, cubes):
        num_active = 0
        for c in  cubes:
            if c.active and cube.is_neighbors(c):
                num_active+=1
        return num_active
        #return len([c for c in cubes if cube.is_neighbors(c) and c.active])

    def run_cycle(self):
        cubes_ = [copy(cube) for cube in self.cubes if cube.active]

        self.add_neighbors()        
        
        for cube in self.cubes:
            num_active = self.get_num_active_neighbors(cube, cubes_)
            
            if cube.active and not num_active in [2, 3]:
                cube.active = False

            elif not cube.active and num_active == 3:
                cube.active = True
    
    def get_num_actives(self):
        return len([c for c in self.cubes if c.active])




class Cube4D(object):

    def __init__(self, x, y, z=0, w=0, active=False):

        self.x = x
        self.y = y
        self.z = z
        self.w = w

        self.active = active

    def is_neighbors(self, cube):

        return True if (self.x in [cube.x - 1, cube.x, cube.x + 1]
                        and self.y in [cube.y - 1, cube.y, cube.y + 1]
                        and self.z in [cube.z - 1, cube.z, cube.z + 1]
                        and self.w in [cube.w - 1, cube.w, cube.w + 1]
                        and self != cube) else False


    def __eq__(self, other):
        return self.x == other.x and self.y == other.y and self.z == other.z and self.w == other.w 

    def __ne__(self, other):
        return not self.__eq__(other)
    
    def __str__(self):
        return f'({self.x}, {self.y}, {self.z}, {self.w} {self.active})'

    def __hash__(self):
        return 1000*self.x + 100*self.y + 10*self.z + self.w
   



class ConwayCubes4D(object):

    def __init__(self):
        self.cubes = []
        self.last_added_cubes = []
        self._iter = [(x, y, z, w) for x in range(-1, 2) for y in range(-1, 2) for z in range(-1, 2) for w in range(-1, 2)]

    def add(self, cube):
        self.cubes.append(cube)
    
    def add_neighbors(self, cube=None):
        if not self.last_added_cubes:
            self.last_added_cubes = self.cubes
        
        new_cubes = []
        for cube in self.last_added_cubes:
            neighbors = map(lambda d: Cube4D(cube.x + d[0], cube.y + d[1], cube.z + d[2], cube.w + d[3]), self._iter)            
            new_cubes.extend(neighbors)
        
        new_cubes = filter(lambda n: not n in self.cubes, set(new_cubes))            
        
        self.cubes.extend(new_cubes)
        self.last_added_cubes = list(new_cubes)


    def get_num_active_neighbors(self, cube, cubes):
        num_active = 0
        for c in  cubes:
            if c.active and cube.is_neighbors(c):
                num_active+=1
        return num_active
        #return len([c for c in cubes if cube.is_neighbors(c) and c.active])

    def run_cycle(self):
        cubes_ = [copy(cube) for cube in self.cubes if cube.active]

        self.add_neighbors()        
        
        for cube in self.cubes:
            num_active = self.get_num_active_neighbors(cube, cubes_)
            
            if cube.active and not num_active in [2, 3]:
                cube.active = False

            elif not cube.active and num_active == 3:
                cube.active = True
    
    def get_num_actives(self):
        return len([c for c in self.cubes if c.active])


with open('input.txt') as input_file:
    inputs = [list(i.strip()) for i in input_file]


conway_cubes = ConwayCubes()

for i, row in enumerate(inputs):
    for j, col in enumerate(row):        
        conway_cubes.add(Cube(j, i, 0) if col == '.' else Cube(j, i, 0, True))


for _ in tqdm(range(6), ncols=100):
    conway_cubes.run_cycle()

print('Parte 1:', conway_cubes.get_num_actives())


conway_cubes4D = ConwayCubes4D()

for i, row in enumerate(inputs):
    for j, col in enumerate(row):        
        conway_cubes4D.add(Cube4D(j, i, 0, 0) if col == '.' else Cube4D(j, i, 0, 0, True))


for _ in tqdm(range(6), ncols=100):
    conway_cubes4D.run_cycle()

print('Parte 2:', conway_cubes4D.get_num_actives())