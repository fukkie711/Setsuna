# 参照元フォルダ（下の階層も含む）からXMLファイルを探し
# そのXMLファイルの文字コードをUTF-８に変換しながら
# 保存先フォルダにコピー

# STEP-1-
# 参照ドライブ(変数from)下の拡張子.xmlをコピー
# *** UTF-8への変換 ***
# 参照先(変数to)にペースト

# STEP-2-
# 必要な情報のみを抜き出す
# カンマ区切りにして.csv化
# 指定したファイル名で上書き保存

FOLDER = r'C:\Users\T15015'
import subprocess
subprocess.Popen(['explorer', FOLDER])
