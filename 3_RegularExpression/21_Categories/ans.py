# 2024年2月1日
"""
記事中でカテゴリ名を宣言している行を抽出せよ．
"""

import pandas as pd

df = pd.read_json(
    '3_RegularExpression/21_categories/jawiki-country.json.gz', lines=True)

uk = df.query('title=="イギリス"')['text'].values[0]

ans = []

for i in uk.split('\n'):
    if '[[Category:' in i:
        ans.append(i)

print(ans)

# これはちょっとヒント見た。
# イギリスについての本文だけでいいのね。
# 20の問題を読み違えていました。
