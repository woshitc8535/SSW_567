# -*- coding: utf-8 -*-
"""
Updated Jan 21, 2018
The primary goal of this file is to demonstrate a simple unittest implementation

@author: jrr
@author: rk
"""

import unittest

from Triangle import classifyTriangle


# This code implements the unit test functionality
# https://docs.python.org/3/library/unittest.html has a nice description of the framework

class TestTriangles(unittest.TestCase):
    # define multiple sets of tests as functions with names that begin
    def testNotATriangle(self):
        self.assertEqual(classifyTriangle(2, 1, 1), 'NotATriangle', '2,1,1 can not be a triangle')

    def testRightTriangleA(self):
        self.assertEqual(classifyTriangle(3, 4, 5), 'Right', '3,4,5 is a Right triangle')

    def testRightTriangleB(self):
        self.assertEqual(classifyTriangle(5, 3, 4), 'Right', '5,3,4 is a Right triangle')

    def testEquilateralTriangles(self):
        self.assertEqual(classifyTriangle(1, 1, 1), 'Equilateral', '1,1,1 should be equilateral')

    def testScaleneTriangles(self):
        self.assertEqual(classifyTriangle(5, 6, 7), 'Scalene', '5,6,7 should be Scalene')

    def testInvalidInputTriangles(self):
        self.assertEqual(classifyTriangle(0, 0, 0), 'InvalidInput')
        self.assertEqual(classifyTriangle(201, 2, 200), 'InvalidInput')
        self.assertEqual(classifyTriangle(-1, -1, -1), 'InvalidInput')

    def testInvalidInputAlphabetTriangles(self):
        self.assertEqual(classifyTriangle('a','b','c'),'InvalidInput')


if __name__ == '__main__':
    print('Running unit tests')
    unittest.main(verbosity=2)
