import unittest

class BinaryPartition(object):

    def __init__(self, code):

        self.code = code
        self.inf = 0
        self.sup = 2 ** len(code) - 1
                
    def split(self, location):

        if (location == 'F' or location == 'L'):
            self.sup -= (self.sup - self.inf + 1) // 2
        elif (location == 'B' or location == 'R'):
            self.inf += (self.sup - self.inf + 1) // 2
    
    def reduce(self):
        for l in self.code:
            self.split(l)

def seat_id(code, num_rows=7):

    bp_x = BinaryPartition(code[:num_rows])
    bp_x.reduce()

    bp_y = BinaryPartition(code[num_rows:])
    bp_y.reduce()

    return (bp_x.inf * 8 + bp_y.sup)

class TestSeatId(unittest.TestCase):

    def test_sample1(self):
        self.assertEqual(seat_id('FBFBBFFRLR'), 357)

    def test_sample2(self):
        self.assertEqual(seat_id('FFFBBBFRRR'), 119)

    def test_sample3(self):
        self.assertEqual(seat_id('BBFFBBFRLL'), 820)

if __name__ == '__main__':
    
    with open('input.txt') as input:
        boarding_passes = [bp.strip() for bp in input]

    # Primera parte
    print('==================== PRIMERA PARTE ====================')
    
    # unittest.main()

    seat_ids = list(map(seat_id, boarding_passes))
    seat_ids.sort()


    #print(max(seat_ids))
        
    print(seat_ids[-1])

    # Segunda parte
    print('==================== SEGUNDA PARTE ====================')

    first_id = seat_ids[0]
    for i, v in enumerate(seat_ids):
        if (i + first_id != v):
            print(i + first_id)
            break
