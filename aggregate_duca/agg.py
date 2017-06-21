# !/usr/bin/env python
from Levenshtein import jaro_winkler
import sys

def split_music(data):
    """
    区切り文字で分割して曲ごとに値を返す.
    １位から３位までを別の配列に分解する.
    """
    list1 = []
    list2 = []
    list3 = []
    with open(data, encoding='utf-8') as f:
        for row in f:
            columns = row.rstrip().split(',')
            list1.append(columns[0])
            list2.append(columns[1])
            list3.append(columns[2])
    return [list1, list2, list3]


def aggregate(name):
    """
    リストを作成してカウントしていく。
    途中で表記ゆれのチェックを入れる
    """
    count = {}
    # すでに曲名がある場合は加算。
    for val in name:
        if val in count.keys():
            count[val] += 1
        else:
            count[val] = 1
    return count

   # for k, v in count.items():
   #     print(k + ': ' + str(v))

def main():
    """曲名集計スクリプト"""
    # 曲名をファイルから呼び出す
    argvs = sys.argv
    # 区切り文字","ごとに上位3曲をリストに分割する
    duca_list1, duca_list2, duca_list3 = split_music(argvs[1])

    # 区切り文字ごとに1つずつ取り出して集計する
    #duca_list1 = ['恋をしよーよ', '観覧車', '仇花', 'タイムマシン']
    #duca_list2 = ['恋をしよーよ', '観覧車', '仇花', 'タイムマシン']
    #duca_list3 = ['恋をしよーよ', '観覧車', '仇花', 'タイムマシン']
    # 1位から３位までの曲をそれぞれ集計する
    count_duca1 = aggregate(duca_list1)
    count_duca2 = aggregate(duca_list2)
    count_duca3 = aggregate(duca_list3)
    # 既存のDuca曲のリストと集計結果を紐付けて0.85より高いものを合計していく

    # その際に「観覧車」「恋をしようよ」のように厄介な曲は別途合計する

    # それぞれをファイルに出力する

if __name__ == '__main__':
    main()
