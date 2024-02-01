# 2024年2月1日
"""
記事のカテゴリ名を（行単位ではなく名前で）抽出せよ．
"""

import pandas as pd
import re

df = pd.read_json(
    '3_RegularExpression/21_categories/jawiki-country.json.gz', lines=True)

uk = df.query('title=="イギリス"')['text'].values[0]

ans = []

for i in uk.split('\n'):
    if '[[Category:' in i:
        # 例えば'[[Category:イギリス|*]]'において
        # '\[\[\w+:' → '[[Category:'
        # '(.[^\| | ^\]]*)' → 'イギリス'(というか'[[Category:')に続く'|'と']'以外の文字列
        # 最初'(\w+)'にしたんだけど'1801年に成立した国家・領域'の中黒でも切られちゃうからやめた
        pattern = '\[\[\w+:(.[^\| | ^\]]*)'
        print(re.search(pattern, i).group(1))
        ans.append(re.search(pattern, i))
