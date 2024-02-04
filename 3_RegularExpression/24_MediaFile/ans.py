# 2024年2月4日
"""
記事から参照されているメディアファイルをすべて抜き出せ．
"""

import pandas as pd
import re

df = pd.read_json(
    '3_RegularExpression/24_MediaFile/jawiki-country.json.gz', lines=True)

uk = df.query('title=="イギリス"')['text'].values[0]

ans = []

for i in uk.split('\n'):
    pattern = '\[\[ファイル:(.[^\|]*)'
    media_file = re.search(pattern, i)
    if media_file:
        print(media_file.group(1))
