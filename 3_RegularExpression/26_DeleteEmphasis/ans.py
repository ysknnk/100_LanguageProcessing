# 2024年2月5日
"""
25の処理時に，テンプレートの値からMediaWikiの強調マークアップ（弱い強調，強調，強い強調のすべて）を除去してテキストに変換せよ（参考: マークアップ早見表）．
"""

import pandas as pd
import pprint
import re

df = pd.read_json(
    '3_RegularExpression/26_DeleteEmphasis/jawiki-country.json.gz', lines=True)

uk = df.query('title=="イギリス"')['text'].values[0]

ans = {}

for index, i in enumerate(uk.split('\n')):
    pattern = '^\|(.*)\s=\s*(.*)'
    template = re.search(pattern, i.replace("'''", ''))
    if template:
        ans[template.group(1)] = template.group(2)

pprint.pprint(ans)
