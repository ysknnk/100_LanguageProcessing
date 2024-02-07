# 2024年2月7日
"""
テンプレートの内容を利用し，国旗画像のURLを取得せよ．（ヒント: MediaWiki APIのimageinfoを呼び出して，ファイル参照をURLに変換すればよい）
"""

import json
import pandas as pd
import re
import requests


df = pd.read_json(
    '3_RegularExpression/29_GetImage/jawiki-country.json.gz', lines=True)

uk = df.query('title=="イギリス"')['text'].values[0]

ans = {}

for index, i in enumerate(uk.split('\n')):
    pattern = re.compile('^\|(.*)\s=\s*(.*)')
    template = pattern.search(i)
    if template:
        ans[template.group(1)] = template.group(2)


image_name = ans['国旗画像'].replace(' ', '_')
url = 'https://commons.wikimedia.org/w/api.php?action=query&titles=File:' + \
    image_name + '&prop=imageinfo&iiprop=url&format=json'
res = requests.get(url).text
image_url = json.loads(
    res)['query']['pages']['127049491']['imageinfo'][0]['url']

print(image_url)
