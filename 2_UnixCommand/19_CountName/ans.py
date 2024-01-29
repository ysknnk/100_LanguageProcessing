# 2024年1月29日
"""
各行の1列目の文字列の出現頻度を求め，その高い順に並べて表示せよ．確認にはcut, uniq, sortコマンドを用いよ．
"""
import collections
import pprint

with open('2_UnixCommand/19_CountName/popular-names.txt', 'r') as f:
    tmp_l = []
    tmp_l_only_name = []

    for i in f:
        tmp_l.append(i.split('\t'))
        tmp_l_only_name.append(i.split('\t')[0])

    # 名前の出現頻度を取得
    # {'名前': '出現回数'}のdict
    tmp_l_counter = collections.Counter(tmp_l_only_name)

    # 出現回数をキーに並べ替え
    # ↓うまくいくと思ったのに同数出現しているとごちゃごちゃになる。
    # pprint.pprint(sorted(tmp_l, key=lambda x: int(tmp_l_counter[x[0]])))
    # 力技にします。
    # ...
    # と思ったけど第二ソートキーの存在を思い出したのでなんとかなりました。
    pprint.pprint(sorted(tmp_l, key=lambda x: (
        int(tmp_l_counter[x[0]]), x[0]), reverse=True))

"""
pandasだとこれだって。ふざけんな！！！
import pandas as pd

df = pd.read_csv('ch02/popular-names.txt', sep='\t', header=None)
print(df[0].value_counts())
"""
