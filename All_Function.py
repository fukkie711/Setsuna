# [ファイル名]Funton.py
# [モジュール数]3
# [カテゴリ]critical
# [概要]
# [機能].xmlの抽出、UTF-8へのエンコード、情報の検索&抽出、

# [Editor log]
# 19/01/10 コメント編集

import sys # sysモジュール読み込み
import glob # globモジュール読み込み
import os # osモジュール読み込み
import codecs # codecsモジュールの読み込み
import csv # csvモジュール読み込み
from tkinter import * # *モジュール読み
#from tkinter import ttk # ttkモジュール読み込み
#from tkinter import filedialog # filedialogモジュール読み込み
#from tkinter import messagebox # messageboxモジュール読み込み
from xml.etree.ElementTree import *
# sys.stdout = codecs.getwriter('utf_8')(sys.stdout)

def create_xml_list(xxx):
    # [機能]複製
    # 指定されたディレクトリ以下から再帰的に.xmlを指定ディレクトリに複製する
    drive = xxx # 引数xxx（＝参照ディレクトリ絶対パスのrow文字列）を変数driveに代入
    os.chdir(drive) # カレントディレクトリをdriveに移動
    path_list = glob.glob('**/*.xml', recursive=True) # 拡張子.xmlを網羅,リスト(path_list)に格納
    list_max = len(path_list) # 変換するxmlファイルの総数を取得
    return path_list, list_max # リスト[path_list]と総数list_maxを返す

def Function_A(drive, drive_add, save_add): # 参照ディレクトリ絶対パス、操作XMLファイル名、保存ディレクトリ絶対パス
    # [機能]変換
    # EUC-JPで記述されたＸＭＬファイルをUTF-8にエンコード、保存先ディレクトリに書き出す
    fromdir = drive + '\\' + drive_add # 変数fromdir::参照ディレクトリ絶対パス
    y = os.path.basename(fromdir) # 変数y::操作対象のファイル名取得
    todir = save_add + '\\' + y # 変数todir::保存先ディレクトリの絶対パス
    verEUC = codecs.open(fromdir, 'r', encoding='euc-jp') # 元ファイルを読み込み
    verUTF8 = open(todir, 'w', encoding='utf-8') # UTFでの新ファイルを新規作成
    for row in verEUC: # 元ファイルから１行ずつ読みだして,
        row = row.replace('<?xml version="1.0" encoding="EUC-JP"?>', '') # 一行目(宣言文)を検索、成功で空白に置換
        verUTF8.write(row) # コピー先新ファイルに書き出す
    verEUC.close() # verEUCを閉じる
    verUTF8.close() # verUTF8を閉じる
    return todir # 保存先ディレクトリ絶対パスを返す

def Function_B(dir, absolute):
    # 準備
    list_in = []
    csv_name = "" # CSVファイル名文字列準備
    dir_add = dir #
    os.chdir(dir_add) # 読み込み先に移動
    target = os.path.basename(absolute)
    tree = parse(target)
    elem = tree.getroot()
    judge_status = str(elem.findtext('.//publication-reference/document-id/kind'))
    # * * *
    if judge_status == "公開特許公報(A)" or judge_status == "公表特許公報(A)": # 公開&公表を篩にかける # Trueで実行
        # csvファイル作成
        csv_name = str(elem.findtext('.//publication-reference/document-id/date'))
        kk = open(csv_name + "発行ディスク.csv", 'a') # なければ作る
        writer = csv.writer(kk, lineterminator='\n')

        # 格納
        list_in.append(str(elem.findtext('.//publication-reference/document-id/country'))) # 発行国
        list_in.append(str(elem.findtext('.//publication-reference/document-id/kind'))) # 公報種別
        list_in.append(str(elem.findtext('.//publication-reference/document-id/date'))) # 公開日
        list_in.append(str(elem.findtext('.//application-reference/document-id/date'))) # 出願日
        list_in.append(str(elem.findtext('.//publication-reference/document-id/doc-number'))) # 公開番号
        list_in.append(str(elem.findtext('.//application-reference/document-id/doc-number'))) # 出願番号
        list_in.append(str(elem.findtext('.//invention-title'))) # 発明の名称
        list_in.append(str(elem.findtext('.//classification-ipc/main-clsf'))) # 国際特許分類(IPC)
        list_in.append(str(elem.findtext('.//number-of-claims'))) # 請求項の数
        list_in.append(str(elem.findtext('.//jp:total-pages', namespaces={'jp':'http://www.jpo.go.jp'}))) # 全頁数
        list_in.append(str(elem.findtext('.//parties/jp:applicants-agents-article/jp:applicants-agents[@sequence="1"]/applicant[@sequence="1"]/addressbook[@lang="ja"]/registered-number', namespaces={'jp':'http://www.jpo.go.jp'})))
        list_in.append(str(elem.findtext('.//parties/jp:applicants-agents-article/jp:applicants-agents[@sequence="1"]/applicant[@sequence="1"]/addressbook[@lang="ja"]/name', namespaces={'jp':'http://www.jpo.go.jp'})))
        list_in.append(str(elem.findtext('.//parties/jp:applicants-agents-article/jp:applicants-agents[@sequence="1"]/applicant[@sequence="1"]/addressbook[@lang="ja"]/address/text', namespaces={'jp':'http://www.jpo.go.jp'})))
        list_in.append(str(elem.findtext('.//parties/jp:applicants-agents-article/jp:applicants-agents[@sequence="2"]/applicant[@sequence="2"]/addressbook[@lang="ja"]/registered-number', namespaces={'jp':'http://www.jpo.go.jp'})))
        list_in.append(str(elem.findtext('.//parties/jp:applicants-agents-article/jp:applicants-agents[@sequence="2"]/applicant[@sequence="2"]/addressbook[@lang="ja"]/name', namespaces={'jp':'http://www.jpo.go.jp'})))
        list_in.append(str(elem.findtext('.//parties/jp:applicants-agents-article/jp:applicants-agents[@sequence="2"]/applicant[@sequence="2"]/addressbook[@lang="ja"]/address/text', namespaces={'jp':'http://www.jpo.go.jp'})))
        list_in.append(str(elem.findtext('.//parties/jp:applicants-agents-article/jp:applicants-agents[@sequence="3"]/applicant[@sequence="3"]/addressbook[@lang="ja"]/registered-number', namespaces={'jp':'http://www.jpo.go.jp'})))
        list_in.append(str(elem.findtext('.//parties/jp:applicants-agents-article/jp:applicants-agents[@sequence="3"]/applicant[@sequence="3"]/addressbook[@lang="ja"]/name', namespaces={'jp':'http://www.jpo.go.jp'})))
        list_in.append(str(elem.findtext('.//parties/jp:applicants-agents-article/jp:applicants-agents[@sequence="3"]/applicant[@sequence="3"]/addressbook[@lang="ja"]/address/text', namespaces={'jp':'http://www.jpo.go.jp'})))
        list_in.append(str(elem.findtext('.//parties/jp:applicants-agents-article/jp:applicants-agents[@sequence="4"]/applicant[@sequence="4"]/addressbook[@lang="ja"]/registered-number', namespaces={'jp':'http://www.jpo.go.jp'})))
        list_in.append(str(elem.findtext('.//parties/jp:applicants-agents-article/jp:applicants-agents[@sequence="4"]/applicant[@sequence="4"]/addressbook[@lang="ja"]/name', namespaces={'jp':'http://www.jpo.go.jp'})))
        list_in.append(str(elem.findtext('.//parties/jp:applicants-agents-article/jp:applicants-agents[@sequence="4"]/applicant[@sequence="4"]/addressbook[@lang="ja"]/address/text', namespaces={'jp':'http://www.jpo.go.jp'})))
        list_in.append(str(elem.findtext('.//parties/jp:applicants-agents-article/jp:applicants-agents[@sequence="5"]/applicant[@sequence="5"]/addressbook[@lang="ja"]/registered-number', namespaces={'jp':'http://www.jpo.go.jp'})))
        list_in.append(str(elem.findtext('.//parties/jp:applicants-agents-article/jp:applicants-agents[@sequence="5"]/applicant[@sequence="5"]/addressbook[@lang="ja"]/name', namespaces={'jp':'http://www.jpo.go.jp'})))
        list_in.append(str(elem.findtext('.//parties/jp:applicants-agents-article/jp:applicants-agents[@sequence="5"]/applicant[@sequence="5"]/addressbook[@lang="ja"]/address/text', namespaces={'jp':'http://www.jpo.go.jp'})))
        list_in.append(str(elem.findtext('.//parties/jp:applicants-agents-article/jp:applicants-agents[@sequence="6"]/applicant[@sequence="6"]/addressbook[@lang="ja"]/registered-number', namespaces={'jp':'http://www.jpo.go.jp'})))
        list_in.append(str(elem.findtext('.//parties/jp:applicants-agents-article/jp:applicants-agents[@sequence="6"]/applicant[@sequence="6"]/addressbook[@lang="ja"]/name', namespaces={'jp':'http://www.jpo.go.jp'})))
        list_in.append(str(elem.findtext('.//parties/jp:applicants-agents-article/jp:applicants-agents[@sequence="6"]/applicant[@sequence="6"]/addressbook[@lang="ja"]/address/text', namespaces={'jp':'http://www.jpo.go.jp'})))
        list_in.append(str(elem.findtext('.//parties/jp:applicants-agents-article/jp:applicants-agents[@sequence="1"]/agent[@sequence="1"][@jp:kind="representative"]/addressbook/registered-number', namespaces={'jp':'http://www.jpo.go.jp'})))
        list_in.append(str(elem.findtext('.//parties/jp:applicants-agents-article/jp:applicants-agents[@sequence="1"]/agent[@sequence="1"][@jp:kind="representative"]/addressbook/name', namespaces={'jp':'http://www.jpo.go.jp'})))
        list_in.append(str(elem.findtext('.//parties/jp:applicants-agents-article/jp:applicants-agents[@sequence="2"]/agent[@sequence="2"][@jp:kind="representative"]/addressbook/registered-number', namespaces={'jp':'http://www.jpo.go.jp'})))
        list_in.append(str(elem.findtext('.//parties/jp:applicants-agents-article/jp:applicants-agents[@sequence="2"]/agent[@sequence="2"][@jp:kind="representative"]/addressbook/name', namespaces={'jp':'http://www.jpo.go.jp'})))
        list_in.append(str(elem.findtext('.//parties/jp:applicants-agents-article/jp:applicants-agents[@sequence="3"]/agent[@sequence="3"][@jp:kind="representative"]/addressbook/registered-number', namespaces={'jp':'http://www.jpo.go.jp'})))
        list_in.append(str(elem.findtext('.//parties/jp:applicants-agents-article/jp:applicants-agents[@sequence="3"]/agent[@sequence="3"][@jp:kind="representative"]/addressbook/name', namespaces={'jp':'http://www.jpo.go.jp'})))
        list_in.append(str(elem.findtext('.//parties/jp:applicants-agents-article/jp:applicants-agents[@sequence="4"]/agent[@sequence="4"][@jp:kind="representative"]/addressbook/registered-number', namespaces={'jp':'http://www.jpo.go.jp'})))
        list_in.append(str(elem.findtext('.//parties/jp:applicants-agents-article/jp:applicants-agents[@sequence="4"]/agent[@sequence="4"][@jp:kind="representative"]/addressbook/name', namespaces={'jp':'http://www.jpo.go.jp'})))
        list_in.append(str(elem.findtext('.//parties/jp:applicants-agents-article/jp:applicants-agents[@sequence="5"]/agent[@sequence="5"][@jp:kind="representative"]/addressbook/registered-number', namespaces={'jp':'http://www.jpo.go.jp'})))
        list_in.append(str(elem.findtext('.//parties/jp:applicants-agents-article/jp:applicants-agents[@sequence="5"]/agent[@sequence="5"][@jp:kind="representative"]/addressbook/name', namespaces={'jp':'http://www.jpo.go.jp'})))
        list_in.append(str(elem.findtext('.//parties/jp:applicants-agents-article/jp:applicants-agents[@sequence="6"]/agent[@sequence="6"][@jp:kind="representative"]/addressbook/registered-number', namespaces={'jp':'http://www.jpo.go.jp'})))
        list_in.append(str(elem.findtext('.//parties/jp:applicants-agents-article/jp:applicants-agents[@sequence="6"]/agent[@sequence="6"][@jp:kind="representative"]/addressbook/name', namespaces={'jp':'http://www.jpo.go.jp'})))
        list_in.append(str(elem.findtext('.//parties/inventors/inventor[@sequence="1"]/addressbook/name')))
        list_in.append(str(elem.findtext('.//parties/inventors/inventor[@sequence="1"]/addressbook/address/text')))
        list_in.append(str(elem.findtext('.//parties/inventors/inventor[@sequence="2"]/addressbook/name')))
        list_in.append(str(elem.findtext('.//parties/inventors/inventor[@sequence="2"]/addressbook/address/text')))
        list_in.append(str(elem.findtext('.//parties/inventors/inventor[@sequence="3"]/addressbook/name')))
        list_in.append(str(elem.findtext('.//parties/inventors/inventor[@sequence="3"]/addressbook/address/text')))
        list_in.append(str(elem.findtext('.//parties/inventors/inventor[@sequence="4"]/addressbook/name')))
        list_in.append(str(elem.findtext('.//parties/inventors/inventor[@sequence="4"]/addressbook/address/text')))
        list_in.append(str(elem.findtext('.//parties/inventors/inventor[@sequence="5"]/addressbook/name')))
        list_in.append(str(elem.findtext('.//parties/inventors/inventor[@sequence="5"]/addressbook/address/text')))
        list_in.append(str(elem.findtext('.//parties/inventors/inventor[@sequence="6"]/addressbook/name')))
        list_in.append(str(elem.findtext('.//parties/inventors/inventor[@sequence="6"]/addressbook/address/text')))
        writer.writerow(list_in) # csvの書き出し
        kk.close()
    return
