import csv
import psycopg2
import os
from pathlib import Path


##データベースへアクセス###
host = "localhost"
port = "5432"###ポート番号
dbname = "postgres"###データベース名
user = "postgres"###ユーザ
password = "postgres"###パスワード
conText = "host={} port={} dbname={} user={} password={}"
conText = conText.format(host,port,dbname,user,password)
connection = psycopg2.connect(conText)
connection.get_backend_pid()
cur = connection.cursor()


###ルートパスの定義###
root = 'C:\\Users\\junki\\test\\4'###ここをユーザ入力から###


###ファイルの検索、読み込み###
###ファイルに対する処理定義###
def db(csv_file):
    with open(csv_file,newline = '')as f:#csv_fileとして受け取ったファイルパスを使ってcsvファイルをfという名前で開く
        read = csv.reader(f)#1行ずつ読む
        for row in read:#任意の列をレコードごとにDBへ書き込み
            #代理人マスター
            clm = "INSERT INTO agent_master (agent_ident_number,agent_ident_name) VALUES ('{}','{}')"#テーブル名の指定と、カラム名で列を指定する。文字列がデータの場合はプレースホルダを単一引用符でくくる
            clm = clm.format(str(row[28]),str(row[29]))#csvファイルのデータのうちどの列を指定するか
            ###書き込み完了処理###
            cur.execute(clm)
            connection.commit()

            #出願人マスター
            clm = "INSERT INTO applicant_master (applicant_ident_number,applicant_ident_name,applicant_ident_address) VALUES('{}','{}','{}')"
            clm = clm.format(str(row[10]),str(row[11]),str(row[12]))
            ###書き込み完了処理###
            cur.execute(clm)
            connection.commit()

            #IIP2002~2017出願テーブル
            clm = "INSERT INTO iip_ap (ap_ida,ap_adate) VALUES('{}','{}')"
            clm = clm.format(str(row[5]),str(row[3]))
            ###書き込み完了処理###
            cur.execute(clm)
            connection.commit()

            #IIP2002~2017出願人テーブル
            clm = "INSERT INTO iip_applicant (applicant_ida,applicant_name,applicant_idname) VALUES('{}','{}','{}')"
            clm = clm.format(str(row[5]),str(row[11]),str(row[12]))
            ###書き込み完了処理###
            cur.execute(clm)
            connection.commit()

            #IIP2002~2017引用テーブル
            #インサート無し

            #IIP2002~2017権利者テーブル
            clm = "INSERT INTO hr (hr_ida) VALUES('{}')"
            clm = clm.format(str(row[5]))
            ###書き込み完了処理###
            cur.execute(clm)
            connection.commit()

            #IIP2002~2017発明者テーブル
            clm = "INSERT INTO iip_inventor (inventor_ida,inventor_name,inventor_address) VALUES('{}','{}','{}')"
            clm = clm.format(str(row[5]),str(row[40]),str(row[41]))
            ###書き込み完了処理###
            cur.execute(clm)
            connection.commit()

            #発明者マスター
            clm = "INSERT INTO inventer_master (inventer_name,inventer_address) VALUES('{}','{}')"
            clm = clm.format(str(row[40]),str(row[41]))
            ###書き込み完了処理###
            cur.execute(clm)
            connection.commit()

            #公開特許公報代理人マスター
            clm = "INSERT INTO pupa_agent_master (agent_number,agent_name) VALUES('{}','{}')"
            clm = clm.format(str(row[28]),str(row[29]))
            ###書き込み完了処理###
            cur.execute(clm)
            connection.commit()

            #公開特許公報出願人マスター
            clm = "INSERT INTO pupa_applicant_master (applicant_number,applicant_name,applicant_address) VALUES('{}','{}','{}')"
            clm = clm.format(str(row[10]),str(row[11]),str(row[12]))
            ###書き込み完了処理###
            cur.execute(clm)
            connection.commit()

            #公開特許公報出願テーブル
            clm = "INSERT INTO pupa_applicant_table VALUES('{}','{}','{}','{}','{}','{}',{},{},'{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}')"
            clm = clm.format(str(row[0]),str(row[1]),str(row[3]),str(row[5]),str(row[6]),str(row[7]),str(row[8]),str(row[9]),str(row[10]),str(row[13]),str(row[16]),str(row[19]),str(row[22]),str(row[25]),str(row[28]),str(row[30]),str(row[32]),str(row[34]),str(row[36]),str(row[38]),str(row[40]),str(row[41]),str(row[42]),str(row[43]),str(row[44]),str(row[45]),str(row[46]),str(row[47]),str(row[48]),str(row[49]),str(row[50]),str(row[51]))
            ###書き込み完了処理###
            cur.execute(clm)
            connection.commit()

            #公開特許公報公開テーブル
            clm = "INSERT INTO pupa_publication_table VALUES('{}','{}','{}')"
            clm = clm.format(str(row[5]),str(row[4]),str(row[2]))
            ###書き込み完了処理###
            cur.execute(clm)
            connection.commit()

            #トランザクションテーブル
            clm = "INSERT INTO transaction_table (issung_country,gazette_type,application_number,filing_date,invention_name,applicant_ident_number,agent_ident_number,inventer_name,inventer_address,claim_number,all_pages) VALUES('{}','{}','{}','{}','{}','{}','{}','{}','{}',{},{})"
            clm = clm.format(str(row[0]),str(row[1]),str(row[5]),str(row[3]),str(row[6]),str(row[10]),str(row[29]),str(row[40]),str(row[41]),str(row[8]),str(row[9]))
            ###書き込み完了処理###
            cur.execute(clm)
            connection.commit()



###ファイルを探して開く定義###
def Finder(path):
    global file#fileという関数はグローバル関数であることを宣言する(エラー回避)
    if os.path.isdir(path):#指定したディレクトリにフォルダがあるかどうか
        files = os.listdir(path)
        for file in files:
            Finder(path + "\\" + file)
            print(a+path)
    else:#パスがディレクトリではなかった＝ファイルである
        if path[-4:] == '.csv':
            db(path)


###ファイル検索スタート###
Finder(root)


###カーソルの終了###
cur.close()
connection.close()
