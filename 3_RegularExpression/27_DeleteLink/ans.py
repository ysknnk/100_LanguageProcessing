# 2024年2月6日
"""
26の処理に加えて，テンプレートの値からMediaWikiの内部リンクマークアップを除去し，テキストに変換せよ（参考: マークアップ早見表）．
"""

import pandas as pd
import pprint
import re

df = pd.read_json(
    '3_RegularExpression/26_DeleteEmphasis/jawiki-country.json.gz', lines=True)

uk = df.query('title=="イギリス"')['text'].values[0]

ans = {}

for index, i in enumerate(uk.split('\n')):
    pattern = re.compile('^\|(.*)\s=\s*(.*)')

    # compile便利
    sub_pattern = re.compile('\[\[(.+\||)(.+?)\]\]')
    template = pattern.search(i.replace("'''", ''))
    if template:
        ans[template.group(1)] = sub_pattern.sub(r'\2', template.group(2))

pprint.pprint(ans)
