from Levenshtein import jaro_winkler

#def split_name(array):
#    """区切り文字で分割して曲ごとに値を返す.
#    """



def aggregate(name):
    """リストを作成してカウントしていく。
        途中で表記ゆれのチェックを入れる
    """
    count = {}

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

    # 区切り文字ごとに1つずつ取り出して集計する
    duca_list = ['恋をしよーよ', '観覧車', '仇花', 'タイムマシン']
    aggregate(duca_list)
    # 既存のDuca曲のリストと集計結果を紐付けて0.85より高いものを合計していく
    # その際に「観覧車」「恋をしようよ」のように厄介な曲は別途合計する


if __name__ == '__main__':
    main()
