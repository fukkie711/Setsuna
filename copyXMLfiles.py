# 参照元フォルダ（下の階層も含む）からXMLファイルを探し
# そのXMLファイルの文字コードをUTF-８に変換しながら
# 保存先フォルダにコピー

# STEP-1-
#1-1 参照ドライブ(変数target_path)下の拡張子.xmlをコピー
#1-2 *** UTF-8への変換 ***
#1-3 参照先(変数to)にペースト

import glob

path = r'C:\Users\T15015\PycharmProjects\PatentApp\patentApp\\*.py'
files = []

files = glob.glob(path)
print(files)


#import os
#path = 'target_path'
#xmls = []
#texts = []
#for x in os.listdir(path):
#    if os.path.isfile(path + x):
#        files.append(x)
#for y in files:
#    if(y[])
#directory = os.listdir('target_path')
#print(directory)

# STEP-2-
#2-1 必要な情報のみを抜き出す
#2-2 カンマ区切りにして.csv化
#2-3 指定したファイル名で上書き保存



# glob.glob('./*.xml')
# FOLDER = r'C:\Users\T15015'
# import subprocess
# subprocess.Popen(['explorer', FOLDER])
