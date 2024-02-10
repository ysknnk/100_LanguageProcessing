# 2024年2月10日
"""
名詞の連接（連続して出現する名詞）を最長一致で抽出せよ．
"""

import re
from pprint import pprint

neko_map_l = []


# 違う名詞に当たるまで再帰呼び出し
def is_same_noun(l, index, noun, count=0):
    if l[index + 1]['surface'] == noun:
        count += 1
    else:
        return count

    return is_same_noun(l, index + 1, noun, count)


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
continuous_noun_dict = {}
for index, neko_map_ in enumerate(neko_map_l):
    noun = neko_map_['surface']
    if neko_map_['pos'] == '名詞':
        count = is_same_noun(neko_map_l, index, noun)

    # 連続して出現する名詞かつ
    # 新規or既存のものより長く連続しているものをdictに追加or更新
    # {'名詞': 出現回数}のdict
    if count != 0:
        if noun not in continuous_noun_dict or \
                continuous_noun_dict[noun] < count:
            continuous_noun_dict[noun] = count + 1

print([x * y for x, y in continuous_noun_dict.items()])
