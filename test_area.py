# cd …　パス移動。cd .. で一つ上に移動
#                 cd []で[]に移動
# tree … ディレクトリ構造を出力、/fオプションでファイル名も出力



list_max = [23,45,67,89,98]
max_max = len(list_max)
count = 0

print("残り" + str(max_max))

for x in list_max:
    now = x
    print(now)
    count = count + 1
    print(str(count) + "/" + str(max_max) + "変換終了")
