# 2024年2月8日
"""
動詞の基本形をすべて抽出せよ．
"""

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
verb_set = set()
for neko_map_ in neko_map_l:
    if neko_map_['pos'] == '動詞':
        verb_set.add(neko_map_['base'])

print(verb_set)
