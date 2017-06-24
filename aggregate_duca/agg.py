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

def leven_music(agg_musics):
    """
    jaro_winklerによって曲を表記ゆれを吸収していく
    """

    """
    music_lists = [
        'Ever Spiral','ラムネ','Blue Planet','Square of the moon','散歩日和',
        '雨のちキミと晴れ模様','アマオト','七色の空','星に想いを夜に願いを','ひとひら',
        'ありがとう','向日葵','Aozora','happiness','あした天気になあれ','アイの庭','夢遥か',
        '夜空','My song','12 Stories','Melody','蕾','青×春☆','甘い罠','Platonic syndrome',
        'Love letter','フタリ','No.51','カラフル','二人色','Revolution!','ISI','光の溢れるときには',
        '夢の通り道','コイノハナ','恋をしよーよ','手紙','アルビナ','Dear','たからもの','Snow wish',
        'With you','こころの種','Cafe','アリガト','Love Clover','クローバー','カラフルDiary',
        'Temptation (Duca Ver)','久遠の夢','たいせつなきみのために、ぼくにできるいちばんのこと',
        '僕らの日々','Only you','ADABANA -仇華-','終わりのはじまり','ニブルヘイム','祈りの虹',
        'いろんなカタチ','ツナグミライ','キミガスキ','キミの大きな手',"絶対Darli'n",'大好きだよ。',
        'シアワセ定義','愛しいキズナ','Brand-New World','Lie','風の唄','恋せよ！乙女',
        'Save the Tale',"Welcome☆Berry's",'また好きになる','赤い薔薇、銀色の月','COLD BUTTERFLY',
        'スターライン','ひとひら ゆらゆらり','幸せのオトシモノ','キミとなら','ボク恋','桜色の想い','Story',
        '君がいてくれたから','太陽とキミと',"Eden's healing",'タイムカプセル','ことば旅行','marry me?',
        'Wishing you','inertia world','My First Love','シアワセのハジマリ','Make a Wish',
        'しあわせの場所','ロケット☆ライド','シアワセsummer','Dreamer','叶えたい未来','Aria','キミとメロディ',
        'Moon Beams','Rainbow Color','恋の記憶','snow crystal','恋をしようよ Let it snow',
        'Jewel Days','メグルmerry-go-round','未来トラベリング','My Darling','想いのハーモニー','恋のAria',
        '0 ～zero～',"I'm in the side",'Nothing','恋想葬','約束','想い出のパズル','Passion',
        'アイオライト','恋するまでの時間','かさねた気持ち','eternal','雪の街 キミと','Confession Eve','雫',
        '記憶×ハジマリ','Chaser×Chaser','1/5 (ゴブンノイチ)','シアワセの理由','笑顔のレシピ','イロドリ',
        '灼熱 Heart Beat','be confidence','恋するletter','かさなるココロ','コイイロセカイ',
        'beloved story','優しい雨','キミと...','Hello,Future!','ナツコイ','あいのうた','Say to you',
        'Fate Line','キミのオト','eyes to eyes','キミへ贈るメロディー','End of the Line','Still',
        '君がいない明日','achromia','ネコイチ','Growing','内緒のホント','Blooming',
        '観覧車 ～あの日と、昨日と今日と明日と～','candy♥girl','Dribing story',
        'ラムネ (12 Stories ver)','ラムネ -strings arrange-','星に想いを夜に願いを Ending arrange ver',
        '夢遥か Piano Arrange Ver','カラフル (ロックバージョン)','二人色 (Jump out mix)',
        'フルスロットルHeart (cobalt green Remix)','光の溢れるときには (arrange ver)',
        'いろんなカタチ Piano Arrange Ver','ロケット☆ライド (AUG Remix)',
        'カラフルDiary Piano Arrange Ver','snow crystal ～Acoustic Arrange~',
        'また好きになる Piano Arrange Ver'
    ]
    """

    music_lists = ['ロケット☆ライド', '恋をしよーよ', "Welcome☆Berry's"]
    result = {}
    for music_name, count in agg_musics.items():
        for music_list_name in music_lists:
            if not music_list_name in result:
                result[music_list_name] = 0
            jalo = jaro_winkler(music_list_name, music_name)
            if jalo > 0.84:
                result[music_list_name] += int(count)
            else:
                continue

    return result



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
    leven_duca1 = leven_music(count_duca1)
    leven_duca2 = leven_music(count_duca2)
    leven_duca3 = leven_music(count_duca3)
    # その際に「観覧車」「恋をしようよ」のように厄介な曲は別途合計する

    # それぞれをファイルに出力する

if __name__ == '__main__':
    main()
