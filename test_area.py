# cd …　パス移動。cd .. で一つ上に移動
#                 cd []で[]に移動
# tree … ディレクトリ構造を出力、/fオプションでファイル名も出力
# push rejectedの時は、ctr + push を押す。



drive =  r"C:\Users\T15015\PycharmProjects\test_area\β_test\β_drive"

text = "I am boned my sord"

# find :: 検索対象の文字列.find(検索する文字列)
# 見つかった場合は文字列の開始位置を返す
# 見つからなかった場合は-1を返す
index = text.find("sord")
if index != -1:
    print ("found at," + str(index))
else:
    print "not found"
