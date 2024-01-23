# 2024年1月23日
"""
各行の1列目だけを抜き出したものをcol1.txtに，2列目だけを抜き出したものをcol2.txtとしてファイルに保存せよ．確認にはcutコマンドを用いよ．
"""

f = open('2_UnixCommand/12_Columns/popular-names.txt', 'r')
col1 = open('2_UnixCommand/12_Columns/col1.txt', 'w')
col2 = open('2_UnixCommand/12_Columns/col2.txt', 'w')

for i in f:
    ii = i.split('\t')
    col1.write(ii[0] + '\n')
    col2.write(ii[1] + '\n')

# これもpandas使うといいっぽいんだけど、pandasはpandas100本ノックで勉強したい。
