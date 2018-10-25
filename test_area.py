# cd …　パス移動。cd .. で一つ上に移動
#                 cd []で[]に移動
# tree … ディレクトリ構造を出力、/fオプションでファイル名も出力
# push rejectedの時は、ctr + push を押す。



list_max = [0,0.153445,0.3065754,0.46545,0.60456,0.75456,0.9564,1]
max_max = len(list_max)
count = 0

print("残り" + str(max_max))

for x in list_max:
    now = x
    print(now)
    # print(str(count) + "/" + str(max_max) + "変換終了")
    progress = now *100
    print(str(round(progress,1)) + "%完了")
