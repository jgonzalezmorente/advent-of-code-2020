import unittest
from functools import reduce
from operator import concat, and_

def count_questions_group(group):
    return len(set(reduce(concat, group)))


def count_questions_group2(group):
    
    unique_questions = set(set(reduce(concat, group)))
    def is_all(c):
        return reduce(and_, map(lambda resp: c in resp, group))
   
    return sum(map(is_all, unique_questions))

class TestCountquestionsGroup(unittest.TestCase):

    def test_group1(self):
        self.assertEqual(count_questions_group(['abc']), 3)

    def test_group2(self):        
        self.assertEqual(count_questions_group(['a', 'b', 'c']), 3)

    def test_group3(self):
        self.assertEqual(count_questions_group(['ab', 'ac']), 3)

    def test_group4(self):
        self.assertEqual(count_questions_group(['a', 'a', 'a', 'a']), 1)

    def test_group5(self):
        self.assertEqual(count_questions_group(['b']), 1)


class TestCountquestionsGroup2(unittest.TestCase):

    def test_group1(self):
        self.assertEqual(count_questions_group2(['abc']), 3)

    def test_group2(self):        
        self.assertEqual(count_questions_group2(['a', 'b', 'c']), 0)

    def test_group3(self):
        self.assertEqual(count_questions_group2(['ab', 'ac']), 1)

    def test_group4(self):
        self.assertEqual(count_questions_group2(['a', 'a', 'a', 'a']), 1)

    def test_group5(self):
        self.assertEqual(count_questions_group2(['b']), 1)

if __name__ == '__main__':
    groups = []
    group = []
    with open('input.txt') as input:
        for q in input:
            if (q != '\n'):
                group.append(q.strip())
            elif (q == '\n'):
                groups.append(group)
                group = []    
    groups.append(group)

    # Primera parte
    print('==================== PRIMERA PARTE ====================')

    print(sum(map(count_questions_group, groups)))


    #unittest.main()
    


    # Segunda parte
    print('==================== SEGUNDA PARTE ====================')
    
    print(sum(map(count_questions_group2, groups)))
    
    #unittest.main()


