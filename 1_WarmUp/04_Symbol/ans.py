# 2024年1月16日
"""
“Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can.”という文を単語に分解し，
1, 5, 6, 7, 8, 9, 15, 16, 19番目の単語は先頭の1文字，それ以外の単語は先頭の2文字を取り出し，
取り出した文字列から単語の位置（先頭から何番目の単語か）への連想配列（辞書型もしくはマップ型）を作成せよ．
"""

sentence = 'Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can.'
first_letters = [1, 5, 6, 7, 8, 9, 15, 16, 19]
sentence_l = sentence.split(' ')
symbol = ''
ans = {}

for index_, i in enumerate(sentence_l):
    if index_ + 1 in first_letters:
        symbol = i[:1]
    else:
        symbol = i[:2]

    ans[symbol] = index_

print(ans)

# 解答見たけどHは1、Heは2......ってなってるな。
# 俺のは0から始まってる。これ俺の負け？
