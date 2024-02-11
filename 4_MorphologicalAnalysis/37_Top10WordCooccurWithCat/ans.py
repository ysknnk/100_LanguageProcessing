# 2024年2月13日
"""
「猫」とよく共起する（共起頻度が高い）10語とその出現頻度をグラフ（例えば棒グラフなど）で表示せよ．
"""

# これ入れないと日本語文字化けします。
import japanize_matplotlib

from matplotlib import pyplot
from pprint import pprint

tmp_l = []
neko_map_l = []

# 前提条件の「1文を形態素（マッピング型）のリストとして表現せよ．」
# をやっていなかったことがここで判明しました。ここから直します。
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


word_frequency = {}
for sentence in neko_map_l:
    if any([i['surface'] == '猫' for i in sentence]):
        for neko_map_ in sentence:
            pos = neko_map_['pos']
            surface = neko_map_['surface']
            if pos in ['特殊', '助詞', '助動詞'] or surface == '猫':
                continue
            else:
                # 既出の単語だったらdictのval(カウント)をインクリメント
                if surface in word_frequency:
                    word_frequency[surface] += 1
                # 新出の単語だったらdictに追加
                else:
                    word_frequency[surface] = 1

top_10_frequent_words = [x for x in sorted(word_frequency.items(),
                                           key=lambda y: y[1],
                                           reverse=True)][:10]

# 降順で並べ替えた後に昇順で並べ替えるの美しくないですね。
x, y = zip(*sorted(top_10_frequent_words, key=lambda x: x[1]))
pyplot.bar(x, y)
pyplot.show()
