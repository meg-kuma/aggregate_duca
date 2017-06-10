import unittest

from agg import aggregate

class TestAggregate(unittest.TestCase):
    def test_aggregate(self):
        kyoku_list = ['恋をしよーよ', '観覧車', '仇花', 'タイムマシン']
        #kyoku_list = ['恋をしよーよ']
        actual = aggregate(kyoku_list) 
        self.assertEqual(actual, {'恋をしよーよ': 1, 'タイムマシン': 1, '観覧車': 1, '仇花': 1})
        #self.assertEqual(actual, {'恋をしよーよ': 1})