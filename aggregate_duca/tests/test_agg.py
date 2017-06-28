import tempfile
import unittest

from agg import aggregate, split_music, leven_music

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
        with tempfile.NamedTemporaryFile(mode='w') as f:
            f.write("""アマオト,Platonic syndrome,二人色
アマオト,ロケット☆ライド,観覧車
ラムネ,ロケット☆ライド,Welcome☆Berry's
""")
            f.flush()
            #actual1, actual2, actual3 = split_music('test_data1.txt')
            actual1, actual2, actual3 = split_music(f.name)
            self.assertEqual(actual1, ['アマオト', 'アマオト', 'ラムネ'])
            self.assertEqual(actual2, ['Platonic syndrome', 'ロケット☆ライド', 'ロケット☆ライド'])
            self.assertEqual(actual3, ['二人色', '観覧車', "Welcome☆Berry's"])


class TestLevenMusic(unittest.TestCase):
    def test_leven_music(self):
        music_list1 = {'こいをしよーよ': 1, 'ロケット☆ライド': 1, 'ロケットライド': 1, "Wlcome Berry's" :1, '観覧車': 1}
        acutual = leven_music(music_list1)
        self.assertEqual(acutual, {'恋をしよーよ': 1, 'ロケット☆ライド': 2, "Welcome☆Berry's": 1, '観覧車': 1})

    def test_leven_music_keisan(self):
        music_list1 = {'こいをしよーよ': 1, 'ロケット☆ライド': 3, 'ロケットライド': 1, "Wlcome Berry's": 1, '観覧車': 2}
        acutual = leven_music(music_list1)
        self.assertEqual(acutual, {'恋をしよーよ': 1, 'ロケット☆ライド': 4, "Welcome☆Berry's": 1, '観覧車': 2})

    def test_leven_music_zero(self):
        music_list1 = {'こいをしよーよ': 0, 'ロケット☆ライド': 0,  "Wlcome Berry's": 0, '観覧車': 0}
        acutual = leven_music(music_list1)
        self.assertEqual(acutual, {'恋をしよーよ': 0, 'ロケット☆ライド': 0, "Welcome☆Berry's": 0, '観覧車': 0})

    def test_leven_music_list_none(self):
        music_list1 = {'こいをしよーよ': 0, 'ロケット☆ライド': 0,  "Wlcome Berry's": 0, '観覧車': 0}
        acutual = leven_music(music_list1)
        self.assertEqual(acutual, {'恋をしよーよ': 0, 'ロケット☆ライド': 0, "Welcome☆Berry's": 0, '観覧車': 0})