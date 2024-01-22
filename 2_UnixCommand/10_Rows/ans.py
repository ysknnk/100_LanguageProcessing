# 2024年1月22日
"""
行数をカウントせよ．確認にはwcコマンドを用いよ．
"""

f = open('2_UnixCommand/popular-names.txt', 'r')

print(len(list(f)))


# powershellなので・・・
# PS C:\Users\nnkg4\pythonProjects\100_LanguageProcessing> (cat .\2_UnixCommand\popular-names.txt).Length
# 2780

# ↑の後にちゃんとlinuxコマンド使えるようにしました・・・
# 詳しくは  100_LanguageProcessing/2_UnixCommand/10_Rows/README.md
# wc -l 2_UnixCommand/popular-names.txt
# 2780 2_UnixCommand/popular-names.txt
