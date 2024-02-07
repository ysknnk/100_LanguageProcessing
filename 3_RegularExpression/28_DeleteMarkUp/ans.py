# 2024年2月7日
"""
27の処理に加えて，テンプレートの値からMediaWikiマークアップを可能な限り除去し，国の基本情報を整形せよ．
"""

import pandas as pd
import pprint
import re

df = pd.read_json(
    '3_RegularExpression/28_DeleteMarkUp/jawiki-country.json.gz', lines=True)

uk = df.query('title=="イギリス"')['text'].values[0]

ans = {}

for index, i in enumerate(uk.split('\n')):
    pattern = re.compile('^\|(.*)\s=\s*(.*)')
    template = pattern.search(i)
    if template:
        ans[template.group(1)] = template.group(2)

for k, v in ans.items():
    # compile便利

    pattern_0 = re.compile("'+")
    pattern_1 = re.compile('\[\[(.+\||)(.+?)\]\]')
    pattern_2 = re.compile('\[\[ファイル:(.*)')
    pattern_3 = re.compile('<.+?>')
    pattern_4 = re.compile('{{.*}}')
    v = pattern_0.sub('', v)
    v = pattern_1.sub(r'\2', v)
    v = pattern_2.sub(r'\1', v)
    v = pattern_3.sub('', v)
    v = pattern_4.sub('', v)

    ans[k] = v

pprint.pprint(ans)

# 全然きれいじゃない気がするけどもう限界。疲れ果てた。
# いつかまた時間があった時に正規表現全部やりなおす(かもしれない)
