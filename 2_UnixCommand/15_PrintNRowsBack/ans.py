# 2024年1月27日
"""
自然数Nをコマンドライン引数などの手段で受け取り，入力のうち末尾のN行だけを表示せよ．確認にはtailコマンドを用いよ．
"""

import sys

# コマンドライン引数を取得
row_count = int(sys.argv[1])

with open('2_UnixCommand/15_PrintNRowsBack/popular-names.txt', 'r') as f:
    f_lines = f.read().splitlines()
    for i in reversed(range(1, row_count + 1)):
        print(f_lines[i * -1].replace('\n', ''))


"""
# python
python3 2_UnixCommand/15_PrintNRowsBack/ans.py 12
Harper  F       10582   2018
Evelyn  F       10376   2018
Liam    M       19837   2018
Noah    M       18267   2018
William M       14516   2018
James   M       13525   2018
Oliver  M       13389   2018
Benjamin        M       13381   2018
Elijah  M       12886   2018
Lucas   M       12585   2018
Mason   M       12435   2018
Logan   M       12352   2018

# linuxコマンド
tail -12 2_UnixCommand/15_PrintNRowsBack/popular-names.txt 
Harper  F       10582   2018
Evelyn  F       10376   2018
Liam    M       19837   2018
Noah    M       18267   2018
William M       14516   2018
James   M       13525   2018
Oliver  M       13389   2018
Benjamin        M       13381   2018
Elijah  M       12886   2018
Lucas   M       12585   2018
Mason   M       12435   2018
Logan   M       12352   2018
"""
