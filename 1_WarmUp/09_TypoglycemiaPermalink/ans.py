# 2024年1月20日
"""
スペースで区切られた単語列に対して，各単語の先頭と末尾の文字は残し，それ以外の文字の順序をランダムに並び替えるプログラムを作成せよ．
ただし，長さが４以下の単語は並び替えないこととする．
適当な英語の文（例えば”I couldn’t believe that I could actually understand what I was reading : the phenomenal power of the human mind .”）を与え，
その実行結果を確認せよ．
"""
import random


def typoglycemia_permalink(s):
    tmp_val = ''
    val = []
    s_l = s.split(' ')
    for i in s_l:
        if len(i) <= 4:
            val.append(i)
        else:
            # 最初と最後の文字以外を抽出
            tmp_val = i[1:len(s) - 1]
            # 最初の文字
            first_letter = i[0]
            # 最後の文字
            last_letter = i[-1]

            # tmp_valをランダムに並べ替えてfirst_letterとlast_letterで挟む
            val.append(
                first_letter + ''.join(random.sample(tmp_val, len(tmp_val))) + last_letter)

    return ' '.join(val)


s = "I couldn’t believe that I could actually understand what I was reading : the phenomenal power of the human mind ."
print(typoglycemia_permalink(s))
