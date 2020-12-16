#%%
class Game(object):

    def __init__(self, initial_turns):
        self.initial_turns = initial_turns
        self.turns = []        
        self.turn_number = 0
        self.initial_length = len(initial_turns)        

    def next(self):
        if self.turn_number < self.initial_length:
            self.turns.insert(0, self.initial_turns[self.turn_number])
        elif (self.turns[0] in self.turns[1:]):
            last_index = self.turns[1:].index(self.turns[0])
            self.turns.insert(0, last_index + 1)
        else:
            self.turns.insert(0, 0)
        
        self.turn_number+=1
        return self.turn_number, self.turns[0]
    
    def get_turn(self, number):
        while (self.turn_number != number):
            self.next()

            if (self.turn_number % 5000 == 0):
                print(f'{int(100*self.turn_number/number)}%')

        return self.turns[0]

game = Game([20, 9, 11, 0, 1, 2])
game.get_turn(30000)


# %%

class Game2(object):

    def __init__(self, initial_turns):        
        self.elements = {}        
        #self.turn_number = len(initial_turns) 
        l = len(initial_turns) 
        self.turn_number =0
        for i, t in enumerate(initial_turns):
            if i < l - 1:
                self.elements[t] = l - i - 1
            else:
                self.last = t

    def next(self):
        d = self.elements.get(self.last, None)
        if d == None:
            d = 0
        else:
            d+=self.turn_number

        self.elements[self.last] = -self.turn_number
        self.last = d
        # for k in self.elements:
        #     self.elements[k]+=1
        self.turn_number+=1
        return self.last
    
    def get_turn(self, number):
        while (self.turn_number != number):
            self.next()

            if (self.turn_number % 5000 == 0):
                print(f'{int(100*self.turn_number/number)}%')

        return self.last

game2 = Game2([0,3,6])
print(game2.next())
print(game2.next())
print(game2.next())
print(game2.next())
#game2.get_turn(2020 + 4)
    
# %%
