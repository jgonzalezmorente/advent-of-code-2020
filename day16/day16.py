from functools import reduce
from operator import mul

class TicketField(object):

    def __init__(self, name, intervals):
        self.name = name
        self.intervals = intervals

    def contains(self, number):
        for interval in self.intervals:
            if interval[0] <= number and number <= interval[1]:
                return True
        
        return False




with open('input.txt') as input_file:
    line = input_file.readline()

    # Parse ticket fields
    ticket_fields = []
    while (line != '\n'):
        line = line.strip()
        field_value = line.split(':')

        name = field_value[0]
        intervals = [tuple([int(x) for x in interval.strip().split('-')]) for interval in field_value[1].split('or')]
        ticket_fields.append(TicketField(name, intervals))

        line = input_file.readline()

    

    # Parse my ticket
    input_file.readline()
    my_ticket = list(map(int, input_file.readline().strip().split(',')))

    # Parse nearby tickets
    input_file.readline()
    input_file.readline()
    nearby_tickets = [list(map(int, line.strip().split(','))) for line in input_file]


def not_valid_for_any(number):
    return all(map(lambda ticket: not ticket.contains(number), ticket_fields))


print('==================== PRIMERA PARTE ====================')
print(sum(map(lambda nt: sum(filter(not_valid_for_any, nt)), nearby_tickets)))

print('==================== SEGUNDA PARTE ====================')

def get_set_fields(number):
    return set(map(lambda tf: tf.name, filter(lambda tf: tf.contains(number), ticket_fields)))

def nearby_tickets_to_columns():        
    return map(lambda i: map(lambda nt: nt[i], nearby_tickets), range(len(nearby_tickets[0])))


nearby_tickets = list(filter(lambda nt: all(map(lambda number: not not_valid_for_any(number), nt)), nearby_tickets))


nearby_tickets_columns = nearby_tickets_to_columns()


sets = list(map(lambda col: reduce(lambda s1, s2: s1.intersection(s2), map(get_set_fields, col)), nearby_tickets_columns))

def set_columns_fields(acc={}):

    element = None
    for i, set in enumerate(sets):
        if len(set) == 1:            
            element = set.pop()
            acc[element] = i
            break

    if not element:
        return acc
    else:
        for set in sets:
            set.discard(element)

        return set_columns_fields(acc)

columns_fields = set_columns_fields()

columns_fields_departure = dict(filter(lambda x: x[0].startswith('departure'), columns_fields.items()))

print(reduce(mul, map(lambda i: my_ticket[i], columns_fields_departure.values())))
