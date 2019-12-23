import os,sys,tkinter,time, csv,psycopg2 # os,sys,tkinterモジュール読み込み
import tkinter as tk
import tkinter.ttk as ttk
from tkinter import * # tkinter全ロード
from tkinter import filedialog # filedialogモジュール読み込み
from tkinter import messagebox # messageboxモジュール読み込み
from tkinter.constants import *

import pandas as pd

from All_Function import Function_A, Function_B, Function_C # 各機能を読み込み
from All_Function import Function_A_dash # 追加機能読み込み
# from Setsuna import db, Finder# 各機能を読み込み

from pathlib import Path
import pathlib
import glob

from time import *
import random

# [宣言部]
list_csv = [] # リストの初期化
progress = 0 # 変数の宣言、カウント０
progresss = 0
###関数定義###

#
def changePage(page):
    # Pageを上位層にする
    page.tkraise()


# rootフレームの設定
root = tk.Tk()
root.title("アプリケーション2019")
root.geometry("600x250")


# ノートブック
nb = ttk.Notebook(width=200, height=200)

# タブの作成
tab1 = tk.Frame(nb)
tab2 = tk.Frame(nb)
tab3 = tk.Frame(nb)
nb.add(tab1, text='DVDからDB', padding=3)
nb.add(tab2, text='CSVからDB', padding=3)
nb.add(tab3, text='Setsuna(DVDからCSV)', padding=3)
nb.pack(expand=1, fill='both')

##########dvdから##########


now = 0
jenecount = 0

#参照ボタン
def ask_folder1_re():
    """ 参照ボタンの動作
    """
    path1_re = filedialog.askdirectory()
    folder_path1_re.set(path1_re)


#保存先ボタン関数
def ask_folder1_sa():
    """ 保存ボタンの動作
    """
    path1_sa = filedialog.askdirectory()
    folder_path1_sa.set(path1_sa)

def st_bt_clicked():
    reference = r"" + folder_path1_re.get() + ""#参照
    save      = r"" + folder_path1_sa.get() + ""#保存

    show_state.configure(text= "DVDを読み込み中") # 進捗割合テキストに演算結果を代入
    show_state.update() # 進捗割合テキストを更新

    #セツナメイン処理
    complete_file = 0 # 変数の初期化
    list_max = 0 # 変数の初期化
    path_list = [] # リストの初期化
    pdf_max = 0

    # xmlアドレス抽出部
    path_list, list_max = Function_A(reference) # 対象ドライブからxmlファイルの絶対パスを再帰的検索する関数。リストと総数を返す。
    show_state.configure(text= "[抽出]PDFを抽出中") # 進捗割合テキストに演算結果を代入
    show_state.update() # 進捗割合テキストを更新
    Function_A_dash(reference,save)

    show_state.configure(text= "[抽出・変換]XMLとCSVを作成中") # 進捗割合テキストに演算結果を代入
    show_state.update() # 進捗割合テキストを更新

    # print("総数：：" + str(list_max)) # テスト用コード
    # エンコード&情報抽出、進捗割合変数演算部
    while complete_file <= list_max - 1: # list_max以下であればループ
        ope_file = path_list[complete_file] # 次の演算予定のファイルアドレスが格納されているリスト番号を読み出し
        absolute = Function_B(reference, ope_file, save) # [変換]
        Function_C(save, absolute) # [抽出]
        complete_file = complete_file + 1 # カウントアップ
        progres1 = round((complete_file / list_max) * 100, 1) # 再演算
        # print(str(progress) + "%完了") # テスト用コード
        progres_bar1.configure(value = progres1) # プログレスバーに演算結果を代入
        show_progres1.configure(text= (str(progres1) + "%完了")) # 進捗割合テキストに演算結果を代入
        progres_bar1.update() # プログレスバーを更新
        show_progres1.update() # 進捗割合テキストを更新

    show_state.configure(text= "[書き出し]CSVをデータベースへ書き出し中") # 進捗割合テキストに演算結果を代入
    show_state.update() # 進捗割合テキストを更新

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

    sss = r"" + folder_path1_sa.get() + ""# 参照先ディレクトリの絶対パス

    root = Path(sss)

    file_list = root.glob('**/*.csv')
    print(file_list)#ジェネレータ

    ###リスト個数検索
    jenecount = 1
    # file_list_2 = root.glob('**/*.csv')
    # for v in file_list_2:
    #     global jenecount
    #     jenecount = jenecount + 1#ファイル数をカウントする

    for path2 in file_list:###forでファイルをリストから1つずつ選択
        print(path2)

        with open(path2,newline = '')as f:#csv_fileとして受け取ったファイルパスを使ってcsvファイルをfという名前で開く
            read = csv.reader(f)#1行ずつ読む
            for row in read:#任意の列をレコードごとにDBへ書き込み

                #代理人マスター
                ##テーブル名の指定と、カラム名で列を指定する。文字列がデータの場合はプレースホルダを単一引用符でくくる
                #conflictで主キーの重複を上書きする処理で重複回避
                #代理人がいない場合に"Null"がデータベースに1件レコードして作成されてしまいます。
                #setsu.exeで"Null"に関する修正する時に注意
                clm = "INSERT INTO agent_master (agent_ident_number,agent_ident_name) VALUES ('{}','{}') on conflict(agent_ident_number) do update set agent_ident_number = '{}'"
                clm = clm.format(str(row[28]),str(row[29]),str(row[28]))#csvファイルのデータのうちどの列を指定するか
                ###書き込み完了処理###
                cur.execute(clm)
                connection.commit()

                #出願人マスター
                clm = "INSERT INTO applicant_master (applicant_ident_number,applicant_ident_name,applicant_ident_address) VALUES('{}','{}','{}') ON CONFLICT(applicant_ident_number) DO UPDATE SET applicant_ident_number = '{}'"
                clm = clm.format(str(row[10]),str(row[11]),str(row[12]),str(row[10]))
                ###書き込み完了処理###
                cur.execute(clm)
                connection.commit()

                #IIP2002~2017出願テーブル
                clm = "INSERT INTO iip_ap (ap_ida,ap_adate) VALUES('{}','{}') ON CONFLICT(ap_ida) DO UPDATE SET ap_ida = '{}'"
                clm = clm.format(str(row[5]),str(row[3]),str(row[5]))
                ###書き込み完了処理##
                cur.execute(clm)
                connection.commit()

                #IIP2002~2017出願人テーブル
                clm = "INSERT INTO iip_applicant (applicant_ida,applicant_name,applicant_address) VALUES('{}','{}','{}')"
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
                clm = "INSERT INTO inventer_master (inventer_name,inventer_address) VALUES('{}','{}') ON CONFLICT(inventer_name,inventer_address) DO UPDATE SET inventer_address = EXCLUDED.inventer_address"
                clm = clm.format(str(row[40]),str(row[41]))
                ###書き込み完了処理###
                cur.execute(clm)
                connection.commit()

                #公開特許公報代理人マスター
                clm = "INSERT INTO pupa_agent_master (agent_number,agent_name) VALUES('{}','{}') ON CONFLICT(agent_number) DO UPDATE SET agent_number = '{}'"
                clm = clm.format(str(row[28]),str(row[29]),str(row[28]))
                ###書き込み完了処理###
                cur.execute(clm)
                connection.commit()

                #公開特許公報出願人マスター
                clm = "INSERT INTO pupa_applicant_master (applicant_number,applicant_name,applicant_address) VALUES('{}','{}','{}') ON CONFLICT(applicant_number) DO UPDATE SET applicant_number = '{}'"
                clm = clm.format(str(row[10]),str(row[11]),str(row[12]),str(row[10]))
                ###書き込み完了処理###
                cur.execute(clm)
                connection.commit()

                #公開特許公報出願テーブル
                clm = "INSERT INTO pupa_application_table VALUES('{}','{}','{}','{}','{}','{}',{},'{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}')"
                escape = str(row[8])
                if escape == "None":
                    escape = "NULL"
                clm = clm.format(str(row[0]),str(row[1]),str(row[3]),str(row[5]),str(row[6]),str(row[7]),escape,str(row[9]),str(row[10]),str(row[13]),str(row[16]),str(row[19]),str(row[22]),str(row[25]),str(row[28]),str(row[30]),str(row[32]),str(row[34]),str(row[36]),str(row[38]),str(row[40]),str(row[41]),str(row[42]),str(row[43]),str(row[44]),str(row[45]),str(row[46]),str(row[47]),str(row[48]),str(row[49]),str(row[50]),str(row[51]))
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
                escape = str(row[8])
                if escape == "None":
                    escape = "NULL"
                clm = clm.format(str(row[0]),str(row[1]),str(row[5]),str(row[3]),str(row[6]),str(row[10]),str(row[28]),str(row[40]),str(row[41]),escape,str(row[9]))
                ###書き込み完了処理###
                cur.execute(clm)
                connection.commit()#csvを開いてDBへインサートする

        global now
        now = now+1
        global progres2
        progres2 = round((now / jenecount) * 100, 1) # 再演算
        progres_bar2.configure(value=progres2)
        show_progres2.configure(text= (str(progres2) + "%完了")) # 進捗割合テキストに演算結果を代入
        progres2_bar.update() # プログレスバーを更新
        show_progres2.update() # 進捗割合テキストを更新

    cur.close()
    connection.close()
    zz = "終了"
    print(zz)
    show_state.configure(text= "完了") # 進捗割合テキストに演算結果を代入
    show_state.update() # 進捗割合テキストを更新

#ボタン
folder_path1_re = tkinter.StringVar()
folder_label1_re = ttk.Label(tab1, text="フォルダ指定")
folder_box1_re = ttk.Entry(tab1, width=50, textvariable=folder_path1_re)
folder_btn1_re = ttk.Button(tab1, text="参照", command=ask_folder1_re)
folder_path1_sa = tkinter.StringVar()
save_label1_sa = ttk.Label(tab1, text="フォルダ指定")
save_box1_sa = ttk.Entry(tab1, width=50, textvariable=folder_path1_sa)
save_btn1_sa = ttk.Button(tab1, text="保存", command=ask_folder1_sa)
app_btn1 = ttk.Button(tab1, text="実行" ,width = 30,command=st_bt_clicked)
folder_label1_re.grid(column=0, row=3, pady=10)
folder_box1_re.grid(column=1, row=3, sticky=tkinter.EW, padx=5)
folder_btn1_re.grid(column=2, row=3)
save_label1_sa.grid(column=0, row=4, pady=10)
save_box1_sa.grid(column=1, row=4, sticky=tkinter.EW, padx=5)
save_btn1_sa.grid(column=2, row=4)
app_btn1.place(x=380, y=180)

#ラベル(処理ステータス表示)
show_state = ttk.Label(tab1, foreground='#faf0e6', background='#778899')
show_state.place(x=450, y=150)


# [Front]プログレスバー(determinate_mode)
progres_bar1 = ttk.Progressbar(tab1,  orient=HORIZONTAL, length=300, mode='determinate')
progres_bar1.configure(maximum=100, value = progress) # 定義
progres_bar1.grid(column=1, row=5, sticky=(N,E,S,W), pady=10, ipadx=10) # 配置指定

# 進捗割合ラベル
showL = ttk.Label(tab1,text = "抽出+変換")
showL.place(x=0,y=88)
showL2 = ttk.Label(tab1,text = "書き出し")
showL2.place(x=0,y=130)
show_progres1 = ttk.Label(tab1, text="0%完了")
show_progres1.place(x=390, y=88)

#進捗率
progres_bar2 = ttk.Progressbar(tab1,  orient=HORIZONTAL, length=300, mode='determinate')
progres_bar2.configure(maximum=100, value = progresss)#演算結果代入
progres_bar2.grid(column=1, row=6, sticky=(N,E,S,W), pady=10, ipadx=10) # 配置指定

# 進捗割合ラベル(画面上に表示する)
show_progres2 =ttk.Label(tab1, text="0%完了")
show_progres2.place(x=390, y=130)



##タブ2

#########CSVをフォルダから探して#########
def ask_folder2():
    """ 参照ボタンの動作
    """
    path2 = filedialog.askdirectory()
    folder_path2.set(path2)
    #print(path2)
    return path2


now = 0
jenecount = 0
file_list = []
def app_btn2_clicked():

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

    sss = r"" + folder_path2.get() + ""# 参照先ディレクトリの絶対パス

    root = Path(sss)

    file_list = root.glob('**/*.csv')
    print(file_list)#ジェネレータ


    file_list_2 = root.glob('**/*.csv')###ファイル個数カウント
    for v in file_list_2:
        global jenecount
        jenecount = jenecount + 1#ファイル数をカウントする

    for path2 in file_list:###forでファイルをリストから1つずつ選択
        print(path2)
        with open(path2,newline = '')as f:#csv_fileとして受け取ったファイルパスを使ってcsvファイルをfという名前で開く
            read = csv.reader(f)#1行ずつ読む
            for row in read:#任意の列をレコードごとにDBへ書き込み

                #代理人マスター
                ##テーブル名の指定と、カラム名で列を指定する。文字列がデータの場合はプレースホルダを単一引用符でくくる
                #conflictで主キーの重複を上書きする処理で重複回避
                #代理人がいない場合に"Null"がデータベースに1件レコードして作成されてしまいます。
                #setsu.exeで"Null"に関する修正する時に注意
                clm = "INSERT INTO agent_master (agent_ident_number,agent_ident_name) VALUES ('{}','{}') on conflict(agent_ident_number) do update set agent_ident_number = '{}'"
                clm = clm.format(str(row[28]),str(row[29]),str(row[28]))#csvファイルのデータのうちどの列を指定するか
                ###書き込み完了処理###
                cur.execute(clm)
                connection.commit()

                #出願人マスター
                clm = "INSERT INTO applicant_master (applicant_ident_number,applicant_ident_name,applicant_ident_address) VALUES('{}','{}','{}') ON CONFLICT(applicant_ident_number) DO UPDATE SET applicant_ident_number = '{}'"
                clm = clm.format(str(row[10]),str(row[11]),str(row[12]),str(row[10]))
                ###書き込み完了処理###
                cur.execute(clm)
                connection.commit()

                #IIP2002~2017出願テーブル
                clm = "INSERT INTO iip_ap (ap_ida,ap_adate) VALUES('{}','{}') ON CONFLICT(ap_ida) DO UPDATE SET ap_ida = '{}'"
                clm = clm.format(str(row[5]),str(row[3]),str(row[5]))
                ###書き込み完了処理##
                cur.execute(clm)
                connection.commit()

                #IIP2002~2017出願人テーブル
                clm = "INSERT INTO iip_applicant (applicant_ida,applicant_name,applicant_address) VALUES('{}','{}','{}')"
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
                clm = "INSERT INTO inventer_master (inventer_name,inventer_address) VALUES('{}','{}') ON CONFLICT(inventer_name,inventer_address) DO UPDATE SET inventer_address = EXCLUDED.inventer_address"
                clm = clm.format(str(row[40]),str(row[41]))
                ###書き込み完了処理###
                cur.execute(clm)
                connection.commit()

                #公開特許公報代理人マスター
                clm = "INSERT INTO pupa_agent_master (agent_number,agent_name) VALUES('{}','{}') ON CONFLICT(agent_number) DO UPDATE SET agent_number = '{}'"
                clm = clm.format(str(row[28]),str(row[29]),str(row[28]))
                ###書き込み完了処理###
                cur.execute(clm)
                connection.commit()

                #公開特許公報出願人マスター
                clm = "INSERT INTO pupa_applicant_master (applicant_number,applicant_name,applicant_address) VALUES('{}','{}','{}') ON CONFLICT(applicant_number) DO UPDATE SET applicant_number = '{}'"
                clm = clm.format(str(row[10]),str(row[11]),str(row[12]),str(row[10]))
                ###書き込み完了処理###
                cur.execute(clm)
                connection.commit()

                #公開特許公報出願テーブル
                clm = "INSERT INTO pupa_application_table VALUES('{}','{}','{}','{}','{}','{}',{},'{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}')"
                escape = str(row[8])
                if escape == "None":
                    escape = "NULL"
                clm = clm.format(str(row[0]),str(row[1]),str(row[3]),str(row[5]),str(row[6]),str(row[7]),escape,str(row[9]),str(row[10]),str(row[13]),str(row[16]),str(row[19]),str(row[22]),str(row[25]),str(row[28]),str(row[30]),str(row[32]),str(row[34]),str(row[36]),str(row[38]),str(row[40]),str(row[41]),str(row[42]),str(row[43]),str(row[44]),str(row[45]),str(row[46]),str(row[47]),str(row[48]),str(row[49]),str(row[50]),str(row[51]))
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
                escape = str(row[8])
                if escape == "None":
                    escape = "NULL"
                clm = clm.format(str(row[0]),str(row[1]),str(row[5]),str(row[3]),str(row[6]),str(row[10]),str(row[28]),str(row[40]),str(row[41]),escape,str(row[9]))
                ###書き込み完了処理###
                cur.execute(clm)
                connection.commit()#csvを開いてDBへインサートする

        global now
        now = now+1
        global progresss
        progresss = round((now / jenecount) * 100, 1) # 再演算
        progresss_bar.configure(value=progresss)
        showww.configure(text= (str(progresss) + "%完了")) # 進捗割合テキストに演算結果を代入
        progresss_bar.update() # プログレスバーを更新
        showww.update() # 進捗割合テキストを更新

    cur.close()
    connection.close()
    zz = "終了"
    print(zz)


#ボタン
folder_path2 = tkinter.StringVar()
folder_label2 = ttk.Label(tab2, text="フォルダ指定")
folder_box2 = ttk.Entry(tab2, width=50, textvariable=folder_path2)
folder_btn2 = ttk.Button(tab2, text="参照", command=ask_folder2)
app_btn2 = ttk.Button(tab2, text="実行",width = 30, command=app_btn2_clicked)
folder_label2.grid(column=0, row=3, pady=10)
folder_box2.grid(column=1, row=3, sticky=tkinter.EW, padx=5)
folder_btn2.grid(column=2, row=3)
app_btn2.place(x=380, y=180)
#app_btn2.grid(column=2, row=5)



#進捗率
progresss_bar = ttk.Progressbar(tab2,  orient=HORIZONTAL, length=300, mode='determinate')
progresss_bar.configure(maximum=100, value = progresss)#演算結果代入
progresss_bar.grid(column=1, row=4, sticky=(N,E,S,W), pady=10, ipadx=10) # 配置指定

# 進捗割合ラベル(画面上に表示する)
showww =ttk.Label(tab2, text="0%完了")
showww.place(x=390, y=50)





##タブ3

#########旧セツナ#########
def ask_folder3():
    """ 参照ボタンの動作
    """
    path3 = filedialog.askdirectory()
    folder_path3.set(path3)

#保存先ボタン関数
def ask_folder4():
    """ 保存ボタンの動作
    """
    path4 = filedialog.askdirectory()
    folder_path4.set(path4)

def st_bt_clicked():
    reference = r"" + folder_path3.get() + ""#参照
    save      = r"" + folder_path4.get() + ""#保存

    #セツナコピペ
    complete_file = 0 # 変数の初期化
    list_max = 0 # 変数の初期化
    path_list = [] # リストの初期化
    # xmlアドレス抽出部
    path_list, list_max = Function_A(reference) # 対象ドライブからxmlファイルの絶対パスを再帰的検索する関数。リストと総数を返す。
    Function_A_dash(reference,save)
    # print("総数：：" + str(list_max)) # テスト用コード
    # エンコード&情報抽出、進捗割合変数演算部
    while complete_file <= list_max - 1: # list_max以下であればループ
        ope_file = path_list[complete_file] # 次の演算予定のファイルアドレスが格納されているリスト番号を読み出し
        absolute = Function_B(reference, ope_file, save) # [変換]
        Function_C(save, absolute) # [抽出]
        complete_file = complete_file + 1 # カウントアップ
        progress = round((complete_file / list_max) * 100, 1) # 再演算
        # print(str(progress) + "%完了") # テスト用コード
        progress_bar.configure(value = progress) # プログレスバーに演算結果を代入
        show.configure(text= (str(progress) + "%完了")) # 進捗割合テキストに演算結果を代入
        progress_bar.update() # プログレスバーを更新
        show.update() # 進捗割合テキストを更新

#ボタン
folder_path3 = tkinter.StringVar()
folder_label3 = ttk.Label(tab3, text="フォルダ指定")
folder_box3 = ttk.Entry(tab3, width=50, textvariable=folder_path3)
folder_btn3 = ttk.Button(tab3, text="参照", command=ask_folder3)
folder_path4 = tkinter.StringVar()
save_label3 = ttk.Label(tab3, text="フォルダ指定")
save_box3 = ttk.Entry(tab3, width=50, textvariable=folder_path4)
save_btn3 = ttk.Button(tab3, text="保存", command=ask_folder4)
app_btn3 = ttk.Button(tab3, text="実行",width = 30, command=st_bt_clicked)
folder_label3.grid(column=0, row=3, pady=10)
folder_box3.grid(column=1, row=3, sticky=tkinter.EW, padx=5)
folder_btn3.grid(column=2, row=3)
save_label3.grid(column=0, row=4, pady=10)
save_box3.grid(column=1, row=4, sticky=tkinter.EW, padx=5)
save_btn3.grid(column=2, row=4)
app_btn3.place(x=380, y=180)
# [Front]プログレスバー(determinate_mode)
progress_bar = ttk.Progressbar(tab3, orient=HORIZONTAL, length=300, mode='determinate')
progress_bar.configure(maximum=100, value = progress) # 定義
progress_bar.grid(column=1, row=5, sticky=(N,E,S,W), pady=10, ipadx=10) # 配置指定

# 進捗割合ラベ

show =ttk.Label(tab3, text="0%完了")
show.place(x=390, y=90)


# if __name__ == '__main__':
root.mainloop()
