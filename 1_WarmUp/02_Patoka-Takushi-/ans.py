# 2024年1月16日
"""
「パトカー」＋「タクシー」の文字を先頭から交互に連結して文字列「パタトクカシーー」を得よ．
"""

# パトカーがpatokaじゃないこともタクシーがtakushiじゃないこともわかってる！！！
patoka = 'パトカー'
takushi = 'タクシー'
ans = ''

# マジックナンバー
# len(patoka)だとtakushiに失礼だしlen(takushi)だとpatokaに失礼だからね。
for i in range(4):
    ans += patoka[i] + takushi[i]

print(ans)
