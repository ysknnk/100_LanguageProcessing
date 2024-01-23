# 2024年1月17日
"""
与えられたシーケンス（文字列やリストなど）からn-gramを作る関数を作成せよ．
この関数を用い，”I am an NLPer”という文から単語bi-gram，文字bi-gramを得よ．
"""


def n_gram_str(n, s):
    val = []
    for i in range(len(s) - n + 1):
        val.append(s[i:i + n])
    return val


def n_gram_list(n, s):
    s = s.split(' ')
    val = []
    for i in range(len(s) - n + 1):
        val.append(s[i:i + n])
    return val


s = 'I am an NLPer'
print(n_gram_str(2, s))
print(n_gram_list(2, s))

print(n_gram_str(3, s))
print(n_gram_list(3, s))
