# 2024年2月10日
"""
文章中に出現する単語とその出現頻度を求め，出現頻度の高い順に並べよ．
"""

# 終わった後にほかの人のやつ見たら句読点とか除外してたので除外処理だけ追加しました。

import re
from pprint import pprint

neko_map_l = []

with open('4_MorphologicalAnalysis/neko.txt.mecab', 'r') as neko:
    for i in neko.readlines():
        neko_map = {}
        text_l = i.split('\t')
        # 改行のところきもいから飛ばす
        if text_l[0] in ['EOS\n', '\n']:
            continue
        surface = text_l[0]
        mor_l = text_l[1].split(',')
        neko_map['surface'] = surface
        neko_map['pos'] = mor_l[0]
        neko_map['pos1'] = mor_l[1]
        neko_map['base'] = mor_l[4]
        neko_map_l.append(neko_map)

# [{'base': '知る', 'pos': '動詞', 'pos1': '*', 'surface': '知ら'}, ...]
word_frequency = {}
for neko_map_ in neko_map_l:
    if neko_map_['pos'] == '特殊':
        continue
    word = neko_map_['surface']

    # 既出の単語だったらdictのval(カウント)をインクリメント
    if word in word_frequency:
        word_frequency[word] += 1
    # 新出の単語だったらdictに追加
    else:
        word_frequency[word] = 1

print([x[0] for x in sorted(word_frequency.items(),
                            key=lambda y: y[1],
                            reverse=True)])
