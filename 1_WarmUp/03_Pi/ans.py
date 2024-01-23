# 2024年1月16日
"""
“Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics.”という文を単語に分解し，
各単語の（アルファベットの）文字数を先頭から出現順に並べたリストを作成せよ．
"""

osake = 'Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics.'

osake_l = osake.split(' ')
tmp_l = []
for i in osake_l:
    tmp_l.append(str(len(i)))

ans = ''.join(tmp_l)
print(ans)
