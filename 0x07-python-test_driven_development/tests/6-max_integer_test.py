#!/usr/bin/python3
"""Unittest for the max_integer module
"""

import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMax(unittest.TestCase):
    '''A class for testing maxinteger method'''

    def test_max_at_end(self):
        '''Testing max when at end of a list'''

        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_max_at_begining(self):
        '''Testing max when at begining of a list'''

        self.assertEqual(max_integer([4, 2, 3, 1]), 4)

    def test_max_with_negative(self):
        '''Testing max when with negative'''

        self.assertEqual(max_integer([1, 2, -6, 4]), 4)
    
    def test_max_at_middle(self):
        '''Testing max at middle'''

        self.assertEqual(max_integer([1, 4, 3, 2]), 4)

    def test_max_with_only_negative(self):
        '''Testing max in a negative list'''

        self.assertEqual(max_integer([-1, -2, -6, -4]), -1)

    def test_max_with_one_element_list(self):
        '''Testing max in a one element list'''

        self.assertEqual(max_integer([8]), 8)

    def test_max_with_empty_list(self):
        '''Testing max in an empty list'''

        self.assertEqual(max_integer([]), None)

if __name__=='__main__':
    unittest.main()
