# 2024年2月7日
"""
形態素解析結果（neko.txt.mecab）を読み込むプログラムを実装せよ．
ただし，各形態素は表層形（surface），基本形（base），品詞（pos），品詞細分類1（pos1）をキーとするマッピング型に格納し，1文を形態素（マッピング型）のリストとして表現せよ．
第4章の残りの問題では，ここで作ったプログラムを活用せよ．
"""

import MeCab
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
    pprint(neko_map_l)
