import unittest
from knightMove_schroders import generateSequence
from knightMove_schroders import knight

class Testing(unittest.TestCase):
    def test_generateSequence_length_one(self):
        
        actual = generateSequence('1',1,2) 
        expected = 1
        self.assertEqual(actual,expected)
        
    def test_generateSequence_length_two(self):
        actual = generateSequence('A',2,2)
        expected = 2
        self.assertEqual(actual,expected)  
    def test_generateSequence_length_two_vowelsAllowed_zero(self):
        actual = generateSequence('A',2,0)
        expected = 0
        self.assertEqual(actual,expected)      
    def test_generateSequence_length_three_vowelsAllowed_one(self):
        actual = generateSequence('A',3,1)
        expected = 5
        self.assertEqual(actual,expected)     
    def test_generateSequence_length_one_whole_sequence(self):
        actual =0
        for i in knight.keys():
            actual += generateSequence(i,1,2)
        expected = 18
        self.assertEqual(actual,expected) 
    def test_generateSequence_length_two_whole_sequence(self):
        actual =0
        for i in knight.keys():
            actual += generateSequence(i,2,2)
        expected = 60
        self.assertEqual(actual,expected) 
    def test_generateSequence_length_three_whole_sequence(self):
        actual =0
        for i in knight.keys():
            actual += generateSequence(i,3,2)
        expected = 214
        self.assertEqual(actual,expected)
    def test_generateSequence_length_one_whole_sequence(self):
        actual =0
        for i in knight.keys():
            actual += generateSequence(i,4,2)
        expected = 732
        self.assertEqual(actual,expected)                  
if __name__ == '__main__':
    unittest.main()              