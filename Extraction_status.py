# STEP-2-
#2-1 必要な情報のみを抜き出す
#2-2 カンマ区切りにして.csv化(上書きモード)
#2-3 指定したファイル名で上書き保存

# * + * + * + * + * + * + * + * + * + * +

import sys # sysモジュール読み込み
import glob # globモジュール読み込み
import os # osモジュール読み込み
import codecs # codecsモジュールの読み込み
# sys.stdout = codecs.getwriter('utf_8')(sys.stdout)

# 機能β実装関数extractionの宣言＊＋＊＋＊＋＊＋＊＋＊＋＊＋＊
def extraction(read_xml_dir, write_csv_dir):
    print(read_xml_dir)
    print(write_csv_dir)
    os.chdir(read_xml_dir) # 読み込み先に移動
    path_list_β = glob.glob('**/*.xml', recursive=True) # 拡張子xmlの絶対パスを網羅、リストに格納

    list_max_β = len(path_list_β) # 抽出するxmlファイルの総数を取得
    count_β = 0 # 変換終了変数の初期化
    print("機能β[抽出]残り" + str(list_max_β))
    print("-*-*-*-*-*-operation-β-_start-*-*-*-*-*-\n")

    for xx in path_list_β:
        fromdir_β = read_xml_dir + '//' + xx # 抽出対象絶対パス
        print("抽出対象：：" + fromdir_β)
        xx_name = os.path.basename(fromdir_β) # 抽出対象ファイル名前取得
        todir_β
# 単体テスト用コード＊＋＊＋＊＋＊＋＊＋＊＋＊
drive =  r"C:\Users\T15015\PycharmProjects\test_area\β_test\β_drive" # テスト用参照先
save = r"C:\Users\T15015\PycharmProjects\test_area\β_test\β_save" # テスト用保存先
extraction(drive, save) # テスト用実行ファイル

# * + * + * + * + * + * + * + * + * + * +
