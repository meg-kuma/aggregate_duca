import unittest

from agg import aggregate, split_music

class TestAggregate(unittest.TestCase):
    def test_aggregate(self):
        kyoku_list = ['恋をしよーよ', '観覧車', '仇花', 'タイムマシン']
        #kyoku_list = ['恋をしよーよ']
        actual = aggregate(kyoku_list) 
        self.assertEqual(actual, {'恋をしよーよ': 1, 'タイムマシン': 1, '観覧車': 1, '仇花': 1})
        #self.assertEqual(actual, {'恋をしよーよ': 1})

    def test_aggregate2(self):
        kyoku_list = ['恋をしよーよ', '観覧車', 'タイムマシン', '仇花', 'タイムマシン']
        actual = aggregate(kyoku_list) 
        self.assertEqual(actual, {'恋をしよーよ': 1, 'タイムマシン': 2, '観覧車': 1, '仇花': 1})

    def test_aggregate_0(self):
        kyoku_list = []
        actual = aggregate(kyoku_list) 
        self.assertEqual(actual, {})

class TestSplitMusic(unittest.TestCase):
    def test_split_music(self):
        actual1, actual2, actual3 = split_music('test_data.txt')
        self.assertEqual(actual1, ['アマオト', 'アマオト', 'ラムネ'])
        self.assertEqual(actual2, ['Platonic syndrome', 'ロケット☆ライド', 'ロケット☆ライド'])
        self.assertEqual(actual3, ['二人色', '観覧車', "Welcom☆Berry's"])