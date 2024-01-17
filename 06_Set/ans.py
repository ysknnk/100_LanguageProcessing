# 2024年1月17日
"""
“paraparaparadise”と”paragraph”に含まれる文字bi-gramの集合を，それぞれ, XとYとして求め，XとYの和集合，積集合，差集合を求めよ．
さらに，’se’というbi-gramがXおよびYに含まれるかどうかを調べよ
"""


def n_gram_str(n, s):
    val = []
    for i in range(len(s) - n + 1):
        val.append(s[i:i + n])
    return val


def get_product_set(a, b):
    val = a + b
    return_val = set()
    for i in val:
        if val.count(i) >= 2:
            return_val.add(i)
    return return_val


val_1 = 'paraparaparadise'
val_2 = 'paragraph'

x = n_gram_str(2, val_1)
y = n_gram_str(2, val_2)

print(x, y)

# 和集合
print(set(x + y))

# 積集合
print(get_product_set(x, y))

# 差集合
print(set(x) - set(y))

# 'se'があるかどうか
print('yes' if 'se' in x else 'no')
print('yes' if 'se' in y else 'no')

# ==================================
# あとから調べたら↓が正解みたい
# 和集合
print(set(x) | set(y))

# 積集合
print(set(x) & set(y))

# 差集合は同じだった
print(set(x) - set(y))

# そして'se'のチェックに関しては問題を勘違いしていた
# 俺のやつだと集合関係ないしそりゃそうか
# ↓が答え
print('se' in (set(x) & set(y)))
