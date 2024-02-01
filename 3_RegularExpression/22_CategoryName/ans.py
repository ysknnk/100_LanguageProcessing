# 2024年2月1日
"""
記事のカテゴリ名を（行単位ではなく名前で）抽出せよ．
"""

import pandas as pd
import re

df = pd.read_json(
    '3_RegularExpression/22_CategoryName/jawiki-country.json.gz', lines=True)

uk = df.query('title=="イギリス"')['text'].values[0]

ans = []

for i in uk.split('\n'):
    # 最初
    # if '[[Category:' in i:
    # でCategoryの行かどうか判定してたんだけど、よく考えたらいらないことがわかったので修正

    # 例えば'[[Category:イギリス|*]]'において
    # '\[\[Category:' → '[[Category:'
    # '(.[^\| | ^\]]*)' → 'イギリス'(というか'[[Category:')に続く'|'と']'以外の文字列
    # 最初'(\w+)'にしたんだけど'1801年に成立した国家・領域'の中黒でも切られちゃうからやめた
    pattern = '\[\[Category:(.[^\| | ^\]]*)'
    category_name = re.search(pattern, i)
    if category_name:
        ans.append(category_name.group(1))

print(ans)
