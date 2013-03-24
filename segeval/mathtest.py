'''
Tests some math related utility functions.

.. moduleauthor:: Chris Fournier <chris.m.fournier@gmail.com>
'''
import unittest
from decimal import Decimal
from .math import mean, std, var, stderr


class TestMath(unittest.TestCase):
    '''
    Math utlity function tests.
    '''
    #pylint: disable=R0904,C0103
    
    def test_mean(self):
        '''
        Tests population mean.
        '''
        self.assertEqual(5, mean([2, 4, 4, 4, 5, 5, 7, 9]))
    
    def test_std(self):
        '''
        Tests population standard deviation.
        '''
        self.assertEqual(2, std([2, 4, 4, 4, 5, 5, 7, 9]))
    
    def test_var(self):
        '''
        Tests population variance.
        '''
        self.assertEqual(4, var([2, 4, 4, 4, 5, 5, 7, 9]))
    
    def test_stderr(self):
        '''
        Tests population standard error of the mean.
        '''
        self.assertEqual(Decimal('0.7071067811865475244008443622'),
                         stderr([2, 4, 4, 4, 5, 5, 7, 9]))
        
