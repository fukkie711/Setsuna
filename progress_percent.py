import sys # sysモジュール読み込み
import glob # globモジュール読み込み
import os # osモジュール読み込み
import codecs # codecsモジュールの読み込み

# drive = r"C:\Users\T15015\PycharmProjects\test_area\test_area\save"
drive = x
print(drive)
# save = r"C:\Users\T15015\PycharmProjects\test_area\test_area\save"
save = y
print(save + "\n")

os.chdir(drive) # カレントディレクトリを走査対象に移動
path_list = glob.glob('**/*.xml', recursive=True) # 拡張子.xmlを網羅,リストに格納

list_max = len(path_list) # 変換するxmlファイルの総数を取得
count = 0 # 変換終了変数countの初期化

for i in list_max:
    count = count + 1 # カウントアップ
    progress = round((count / list_max) * 100, 1) # 変数progress:進捗割合 # ローカル変数
    print(str(progress) + "%完了") # 小数点第一位で切り捨て
    judge = 0 # 終了判断フラグ　１で終了 # ローカル変数
    return progress
