# 2024年2月1日
"""
記事中に含まれるセクション名とそのレベル（例えば”== セクション名 ==”なら1）を表示せよ．
"""

import pandas as pd
import re

df = pd.read_json(
    '3_RegularExpression/23_SectionLevel/jawiki-country.json.gz', lines=True)

uk = df.query('title=="イギリス"')['text'].values[0]

ans = []

for i in uk.split('\n'):
    # 行頭が=かつそれが2個以上連続していて、行末も同じ条件を満たしているものを抽出
    # 行頭の連続した=と、そのあとに続く文字列(セクション名)はそれぞれグループ化しておく
    pattern = '(^==+)(.[^=]*)==+'
    section = re.search(pattern, i)
    if section:
        print('========================')
        # セクションレベルは行頭の=の数-1でよさそう
        print(
            f'セクション名:{section.group(2)}\nセクションレベル:{len(section.group(1)) - 1}'
        )
