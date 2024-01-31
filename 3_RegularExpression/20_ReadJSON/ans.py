# 2024年1月29日、2024年1月31日
"""
Wikipedia記事のJSONファイルを読み込み，「イギリス」に関する記事本文を表示せよ．問題21-29では，ここで抽出した記事本文に対して実行せよ．
"""

import gzip
import json
import pandas as pd
import pprint

# ↓でやろうとしたらValueError: Trailing dataが出てしまったので、read_json部分だけ答え見ました。すみません。
# df_gzip = pd.read_json(
#     '3_RegularExpression/20_ReadJson/jawiki-country.json.gz', compression='infer')

df = pd.read_json(
    '3_RegularExpression/20_ReadJson/jawiki-country.json.gz', lines=True)

# イギリスの本文を取得
# でもこれはちょっと変みたい
print(df[df['title'] == 'イギリス']['text'].to_string())

# 本当はこうらしい
# print(df.query('title=="イギリス"')['text'].values[0])

# pandasめっちゃ便利そうだったのでこの章から使い始めることにしました
# ただ全然使い方わからん
