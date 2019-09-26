from pathlib import Path
import csv
import os

downloads = Path(str(Path.home()) + r"\Downloads") #Cドライブのユーザーフォルダ内のデフォルトのダウンロードフォルダにcsvファイルがあれば動く
csv_list = list(downloads.glob("*.csv"))

csv_file = open(csv_list.pop(),'r')


a_list = [[]] 
for row in csv.reader(csv_file):
    for col in row:
        row[i]

        print(row[6:10:12])
#     a_list.append(row[6]) #row内は0がA列、1がB列の順番
#     a_list.append(row[10])
#     a_list.append(row[11])
#
# print(a_list)

#listに取得したデータを書き込む指定
a_text = ""
for a in a_list:
    a_text += a


#没案a_data = a_text.splitlines()

#繋がった文字列を区切る
#print(a_text.splitlines(True)) #改行をキーにして文字列をカンマ区切りにする


#ここからpyファイルと同じディレクトリにtxtファイルを新規or上書きする構文
a_file = open('csv_test.csv','w') #ファイル名と第2引数(書き込みは(w)
a_file.writelines(a_text)   #文字列記載、ファイル内容に変数を指定
a_file.close() #決まり文句





#デスクトップのパス習得が出来ない、また今度
##desktop = os.getenv("HOMEDRIVE") + os.getenv("HOMEPATH") + "\\Desktop"
##a_file = open(Path(desktop + "\\testcsv.txt"),"w")
##a_file.writelines(a_text)
##a_file.close()
