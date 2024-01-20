# 2024年1月20日
"""
与えられた文字列の各文字を，以下の仕様で変換する関数cipherを実装せよ．

英小文字ならば(219 - 文字コード)の文字に置換
その他の文字はそのまま出力
この関数を用い，英語のメッセージを暗号化・復号化せよ．
"""


def cipher(s):
    val = ''
    for i in s:
        if i.islower():
            # 219 - 文字コード
            i = chr(219 - ord(i))
        val += i
    return val


print(cipher('Apple'))
# 複合も同じ関数でいける
print(cipher(cipher('Apple')))
