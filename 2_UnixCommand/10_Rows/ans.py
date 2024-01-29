# 2024年1月22日
"""
行数をカウントせよ．確認にはwcコマンドを用いよ．
"""

with open('2_UnixCommand/10_Rows/popular-names.txt', 'r') as f:
    print(len(list(f)))

# wc -l 2_UnixCommand/popular-names.txt
# 2780 2_UnixCommand/popular-names.txt
