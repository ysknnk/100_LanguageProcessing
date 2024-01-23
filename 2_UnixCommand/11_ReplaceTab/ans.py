# 2024年1月23日
"""
タブ1文字につきスペース1文字に置換せよ．確認にはsedコマンド，trコマンド，もしくはexpandコマンドを用いよ．
"""

f = open('2_UnixCommand/11_ReplaceTab/popular-names.txt', 'r')
fw = open('2_UnixCommand/11_ReplaceTab/popular-names_space.txt', 'w')

for i in f:
    fw.write(i.replace('\t', ' '))


# pandas使うとシュッと書けるっぽい
# import pandas as pd

# df = pd.read_csv('2_UnixCommand/11_ReplaceTab/popular-names.txt', sep='\t', header=None)
# df.to_csv('2_UnixCommand/11_ReplaceTab/popular-names_space.txt', sep=' ', index=False, header=None)
