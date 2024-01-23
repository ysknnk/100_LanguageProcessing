# 2024年1月22日
"""
行数をカウントせよ．確認にはwcコマンドを用いよ．
"""

f = open('2_UnixCommand/10_Rows/popular-names.txt', 'r')

print(len(list(f)))

# wc -l 2_UnixCommand/popular-names.txt
# 2780 2_UnixCommand/popular-names.txt
