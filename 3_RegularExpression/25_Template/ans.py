# 2024年2月4日
"""
記事中に含まれる「基礎情報」テンプレートのフィールド名と値を抽出し，辞書オブジェクトとして格納せよ．
"""

import pandas as pd
import pprint
import re


df = pd.read_json(
    '3_RegularExpression/25_Template/jawiki-country.json.gz', lines=True)

uk = df.query('title=="イギリス"')['text'].values[0]

ans = {}

for index, i in enumerate(uk.split('\n')):
    pattern = '^\|(.*)\s=\s*(.*)'
    template = re.search(pattern, i)
    if template:
        ans[template.group(1)] = template.group(2)

pprint.pprint(ans)
