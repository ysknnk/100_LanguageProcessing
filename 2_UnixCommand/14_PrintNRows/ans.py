# 2024年1月27日
"""
自然数Nをコマンドライン引数などの手段で受け取り，入力のうち先頭のN行だけを表示せよ．確認にはheadコマンドを用いよ．
"""

import sys

# コマンドライン引数を取得
row_count = int(sys.argv[1])

f = list(open('2_UnixCommand/14_PrintNRows/popular-names.txt', 'r'))

for i in range(row_count):
    print(f[i].replace('\n', ''))


"""
nnkysk@KITA-9:/mnt/c/Users/nnkg4/pythonProjects/100_LanguageProcessing$ python3 2_UnixCommand/14_PrintNRows/ans.py 12
Mary    F       7065    1880
Anna    F       2604    1880
Emma    F       2003    1880
Elizabeth       F       1939    1880
Minnie  F       1746    1880
Margaret        F       1578    1880
Ida     F       1472    1880
Alice   F       1414    1880
Bertha  F       1320    1880
Sarah   F       1288    1880
John    M       9655    1880
William M       9532    1880

nnkysk@KITA-9:/mnt/c/Users/nnkg4/pythonProjects/100_LanguageProcessing$ head -12 2_UnixCommand/14_PrintNRows/popular-names.txt 
Mary    F       7065    1880
Anna    F       2604    1880
Emma    F       2003    1880
Elizabeth       F       1939    1880
Minnie  F       1746    1880
Margaret        F       1578    1880
Ida     F       1472    1880
Alice   F       1414    1880
Bertha  F       1320    1880
Sarah   F       1288    1880
John    M       9655    1880
William M       9532    1880
"""
