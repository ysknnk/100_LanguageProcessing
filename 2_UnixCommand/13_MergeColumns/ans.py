# 2024年1月27日
"""
12で作ったcol1.txtとcol2.txtを結合し，元のファイルの1列目と2列目をタブ区切りで並べたテキストファイルを作成せよ．
確認にはpasteコマンドを用いよ．
"""

col1 = list(open('2_UnixCommand/13_MergeColumns/col1.txt', 'r'))
col2 = list(open('2_UnixCommand/13_MergeColumns/col2.txt', 'r'))
merged_file = open('2_UnixCommand/13_MergeColumns/merged_file.txt', 'w')

for i in range(len(col1)):
    merged_file.write(col1[i].replace('\n', '') + '\t' +
                      col2[i].replace('\n', '') + '\n')


"""
merged_file.txt(先頭15行のみ)
Mary	F
Anna	F
Emma	F
Elizabeth	F
Minnie	F
Margaret	F
Ida	F
Alice	F
Bertha	F
Sarah	F
John	M
William	M
James	M
Charles	M
George	M

pasteコマンド
nnkysk@KITA-9:/mnt/c/Users/nnkg4/pythonProjects/100_LanguageProcessing$ paste 2_UnixCommand/13_MergeColumns/col1.txt 2_UnixCommand/13_MergeColumns/col2.txt | head -15
Mary    F
Anna    F
Emma    F
Elizabeth       F
Minnie  F
Margaret        F
Ida     F
Alice   F
Bertha  F
Sarah   F
John    M
William M
James   M
Charles M
George  M
"""
