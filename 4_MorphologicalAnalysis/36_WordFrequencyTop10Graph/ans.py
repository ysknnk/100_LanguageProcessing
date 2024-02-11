# 2024年2月11日
"""
出現頻度が高い10語とその出現頻度をグラフ（例えば棒グラフなど）で表示せよ．
"""

# これ入れないと日本語文字化けします。
import japanize_matplotlib

import re

from matplotlib import pyplot
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

top_10_frequent_words = [x for x in sorted(word_frequency.items(),
                                           key=lambda y: y[1],
                                           reverse=True)][:10]

# 降順で並べ替えた後に昇順で並べ替えるの美しくないですね。
x, y = zip(*sorted(top_10_frequent_words, key=lambda x: x[1]))
pyplot.bar(x, y)
pyplot.show()
