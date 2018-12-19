
import sys # sysモジュール読み込み
import glob # globモジュール読み込み
import os # osモジュール読み込み
import codecs # codecsモジュールの読み込み
import csv
from tkinter import * # *モジュール読み
from tkinter import ttk # ttkモジュール読み込み
from tkinter import filedialog # filedialogモジュール読み込み
from tkinter import messagebox # messageboxモジュール読み込み
from xml.etree.ElementTree import *
# sys.stdout = codecs.getwriter('utf_8')(sys.stdout)

def create_xml_list(xxx): # create_xml_list関数：：
    drive = xxx
    os.chdir(drive) # カレントディレクトリを走査対象に移動
    path_list = glob.glob('**/*.xml', recursive=True) # 拡張子.xmlを網羅,リストに格納
    list_max = len(path_list) # 変換するxmlファイルの総数を取得
    return path_list, list_max # リスト[path_list]と総数list_maxを返す

def Function_A(drive, drive_add, save_add):
    fromdir = drive + '\\' + drive_add # 変数fromdir::操作対象絶対パス
    y = os.path.basename(fromdir) # 変数y::操作対象のファイル名取得
    todir = save_add + '\\' + y # 変数todir::保存先ディレクトリの絶対パス
    ff = codecs.open(fromdir, 'r', encoding='euc-jp') # 元ファイルを読み込み
    fout_utf = open(todir, 'w', encoding='utf-8') # UTFでの新ファイルを新規作成
    for row in ff: # 元ファイルから１行ずつ読みだして
        row = row.replace('<?xml version="1.0" encoding="EUC-JP"?>', '') # 一行目
        fout_utf.write(row) # コピー先新ファイルに書き出す
    ff.close() # ffを閉じる
    fout_utf.close() # fout_utfを閉じる
    return todir

def Function_B(dir, absolute):
    # 準備
    list_in = []
    csv_name = ""
    dir_add = dir
    os.chdir(dir_add) # 読み込み先に移動
    target = os.path.basename(absolute)
    tree = parse(target)
    elem = tree.getroot()
    judge_status = str(elem.findtext('.//publication-reference/document-id/kind'))
    print(judge_status)
    # * * *
    if judge_status == "公開特許公報(A)" or judge_status == "公表特許公報(A)": # 公開&公表を篩にかける # Trueで実行
        # csvファイル作成
        csv_name = str(elem.findtext('.//publication-reference/document-id/date'))
        kk = open(csv_name + "発行ディスク.csv", 'a') # なければ作る
        writer = csv.writer(kk, lineterminator='\n')
        # 格納
        print("１．発行国　：：" + str(elem.findtext('.//publication-reference/document-id/country'))) # 発行国
        list_in.append(str(elem.findtext('.//publication-reference/document-id/country'))) # 発行国
        print("２．公報種別：：" + str(elem.findtext('.//publication-reference/document-id/kind'))) # 公報種別
        list_in.append(str(elem.findtext('.//publication-reference/document-id/kind'))) # 公報種別
        print("３．公開日　：：" + str(elem.findtext('.//publication-reference/document-id/date'))) # 公開日
        list_in.append(str(elem.findtext('.//publication-reference/document-id/date'))) # 公開日
        print("４．出願日　：：" + str(elem.findtext('.//application-reference/document-id/date'))) # 出願日
        list_in.append(str(elem.findtext('.//application-reference/document-id/date'))) # 出願日
        print("５．公開番号：：" + str(elem.findtext('.//publication-reference/document-id/doc-number'))) # 公開番号
        list_in.append(str(elem.findtext('.//publication-reference/document-id/doc-number'))) # 公開番号
        print("６．出願番号：：" + str(elem.findtext('.//application-reference/document-id/doc-number'))) # 出願番号
        list_in.append(str(elem.findtext('.//application-reference/document-id/doc-number'))) # 出願番号
        print("７．発明の名称：：" + str(elem.findtext('.//invention-title'))) # 発明の名称
        list_in.append(str(elem.findtext('.//invention-title'))) # 発明の名称
        print("８．ＩＰＣ分類：：" + str(elem.findtext('.//classification-ipc/main-clsf'))) # 国際特許分類(IPC)
        list_in.append(str(elem.findtext('.//classification-ipc/main-clsf'))) # 国際特許分類(IPC)
        print("９．請求項の数：：" + str(elem.findtext('.//number-of-claims'))) # 請求項の数
        list_in.append(str(elem.findtext('.//number-of-claims'))) # 請求項の数
        print("10．全頁数　：：" + str(elem.findtext('.//jp:total-pages', namespaces={'jp':'http://www.jpo.go.jp'}))) # 全頁数
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
