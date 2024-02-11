# 2024年2月13日
"""
単語の出現頻度のヒストグラムを描け．ただし，横軸は出現頻度を表し，1から単語の出現頻度の最大値までの線形目盛とする．
縦軸はx軸で示される出現頻度となった単語の異なり数（種類数）である．
"""

import collections
# これ入れないと日本語文字化けします。
import japanize_matplotlib

from matplotlib import pyplot
from pprint import pprint

tmp_l = []
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
        tmp_l.append(neko_map)

        if surface == '。':
            neko_map_l.append(tmp_l)
            tmp_l = []


words = []
for sentence in neko_map_l:
    for neko_map_ in sentence:
        words.append(neko_map_['surface'])

# 単語の出現頻度
hindo = collections.Counter(words)

# 出現頻度の多い順で、出現頻度のみのlistを作成
hindohindo = [i[1] for i in hindo.most_common()]

# 順位のリストを取得
x = list(range(1, len(hindohindo) + 1))

y = hindohindo
pyplot.plot(x, y)

ax = pyplot.gca()
ax.set_yscale('log')
ax.set_xscale('log')

pyplot.show()
