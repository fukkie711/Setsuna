
import sys # sysモジュール読み込み
import glob # globモジュール読み込み
import os # osモジュール読み込み
import codecs # codecsモジュールの読み込み
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
    dir_add = dir
    os.chdir(dir_add) # 読み込み先に移動
    target = os.path.basename(absolute)
    tree = parse(target)
    elem = tree.getroot()
    print("１．発行国　：：" + str(elem.findtext('.//publication-reference/document-id/country'))) # 発行国
    print("２．公報種別：：" + str(elem.findtext('.//publication-reference/document-id/kind'))) # 公報種別
    print("３．公開日　：：" + str(elem.findtext('.//publication-reference/document-id/date'))) # 公開日
    print("４．出願日　：：" + str(elem.findtext('.//application-reference/document-id/date'))) # 出願日
    print("５．公開番号：：" + str(elem.findtext('.//publication-reference/document-id/doc-number'))) # 公開番号
    print("６．出願番号：：" + str(elem.findtext('.//application-reference/document-id/doc-number'))) # 出願番号
    print("７．発明の名称：：" + str(elem.findtext('.//invention-title'))) # 発明の名称
    print("８．ＩＰＣ分類：：" + str(elem.findtext('.//classification-ipc/main-clsf'))) # 国際特許分類(IPC)
    print("９．請求項の数：：" + str(elem.findtext('.//number-of-claims'))) # 請求項の数
    print("10．全頁数　：：" + str(elem.findtext('.//jp:total-pages', namespaces={'jp':'http://www.jpo.go.jp'}))) # 全頁数
    print("11-1．出願人名称１：：" + str(elem.findtext('.//parties/jp:applicants-agents-article/jp:applicants-agents[@sequence="1"]/applicant[@sequence="1"]/addressbook[@lang="ja"]/name', namespaces={'jp':'http://www.jpo.go.jp'})))
    print("12-1．出願人居所１：：" + str(elem.findtext('.//parties/jp:applicants-agents-article/jp:applicants-agents[@sequence="1"]/applicant[@sequence="1"]/addressbook[@lang="ja"]/address/text', namespaces={'jp':'http://www.jpo.go.jp'})))
    print("13-1．出願人識別番号１：：" + str(elem.findtext('.//parties/jp:applicants-agents-article/jp:applicants-agents[@sequence="1"]/applicant[@sequence="1"]/addressbook[@lang="ja"]/registered-number', namespaces={'jp':'http://www.jpo.go.jp'})))
    print("11-2．出願人名称２：：" + str(elem.findtext('.//parties/jp:applicants-agents-article/jp:applicants-agents[@sequence="2"]/applicant[@sequence="2"]/addressbook[@lang="ja"]/name', namespaces={'jp':'http://www.jpo.go.jp'})))
    print("12-2．出願人居所２：：" + str(elem.findtext('.//parties/jp:applicants-agents-article/jp:applicants-agents[@sequence="2"]/applicant[@sequence="2"]/addressbook[@lang="ja"]/address/text', namespaces={'jp':'http://www.jpo.go.jp'})))
    print("13-2．出願人識別番号２：：" + str(elem.findtext('.//parties/jp:applicants-agents-article/jp:applicants-agents[@sequence="2"]/applicant[@sequence="2"]/addressbook[@lang="ja"]/registered-number', namespaces={'jp':'http://www.jpo.go.jp'})))
    print("11-3．出願人名称３：：" + str(elem.findtext('.//parties/jp:applicants-agents-article/jp:applicants-agents[@sequence="3"]/applicant[@sequence="3"]/addressbook[@lang="ja"]/name', namespaces={'jp':'http://www.jpo.go.jp'})))
    print("12-3．出願人居所３：：" + str(elem.findtext('.//parties/jp:applicants-agents-article/jp:applicants-agents[@sequence="3"]/applicant[@sequence="3"]/addressbook[@lang="ja"]/address/text', namespaces={'jp':'http://www.jpo.go.jp'})))
    print("13-3．出願人識別番号３：：" + str(elem.findtext('.//parties/jp:applicants-agents-article/jp:applicants-agents[@sequence="3"]/applicant[@sequence="3"]/addressbook[@lang="ja"]/registered-number', namespaces={'jp':'http://www.jpo.go.jp'})))
    print("11-4．出願人名称４：：" + str(elem.findtext('.//parties/jp:applicants-agents-article/jp:applicants-agents[@sequence="4"]/applicant[@sequence="4"]/addressbook[@lang="ja"]/name', namespaces={'jp':'http://www.jpo.go.jp'})))
    print("12-4．出願人居所４：：" + str(elem.findtext('.//parties/jp:applicants-agents-article/jp:applicants-agents[@sequence="4"]/applicant[@sequence="4"]/addressbook[@lang="ja"]/address/text', namespaces={'jp':'http://www.jpo.go.jp'})))
    print("13-4．出願人識別番号４：：" + str(elem.findtext('.//parties/jp:applicants-agents-article/jp:applicants-agents[@sequence="4"]/applicant[@sequence="4"]/addressbook[@lang="ja"]/registered-number', namespaces={'jp':'http://www.jpo.go.jp'})))
    print("11-5．出願人名称５：：" + str(elem.findtext('.//parties/jp:applicants-agents-article/jp:applicants-agents[@sequence="5"]/applicant[@sequence="5"]/addressbook[@lang="ja"]/name', namespaces={'jp':'http://www.jpo.go.jp'})))
    print("12-5．出願人居所５：：" + str(elem.findtext('.//parties/jp:applicants-agents-article/jp:applicants-agents[@sequence="5"]/applicant[@sequence="5"]/addressbook[@lang="ja"]/address/text', namespaces={'jp':'http://www.jpo.go.jp'})))
    print("13-5．出願人識別番号５：：" + str(elem.findtext('.//parties/jp:applicants-agents-article/jp:applicants-agents[@sequence="5"]/applicant[@sequence="5"]/addressbook[@lang="ja"]/registered-number', namespaces={'jp':'http://www.jpo.go.jp'})))
    print("11-6．出願人名称６：：" + str(elem.findtext('.//parties/jp:applicants-agents-article/jp:applicants-agents[@sequence="6"]/applicant[@sequence="6"]/addressbook[@lang="ja"]/name', namespaces={'jp':'http://www.jpo.go.jp'})))
    print("12-6．出願人居所６：：" + str(elem.findtext('.//parties/jp:applicants-agents-article/jp:applicants-agents[@sequence="6"]/applicant[@sequence="6"]/addressbook[@lang="ja"]/address/text', namespaces={'jp':'http://www.jpo.go.jp'})))
    print("13-6．出願人識別番号６：：" + str(elem.findtext('.//parties/jp:applicants-agents-article/jp:applicants-agents[@sequence="6"]/applicant[@sequence="6"]/addressbook[@lang="ja"]/registered-number', namespaces={'jp':'http://www.jpo.go.jp'})))
    print("14-1．発明者名称１：：" + str(elem.findtext('.//parties/inventors/inventor[@sequence="1"]/addressbook/name')))
    print("15-1．発明者居所１：：" + str(elem.findtext('.//parties/inventors/inventor[@sequence="1"]/addressbook/address/text')))
    print("14-2．発明者名称２：：" + str(elem.findtext('.//parties/inventors/inventor[@sequence="2"]/addressbook/name')))
    print("15-2．発明者居所２：：" + str(elem.findtext('.//parties/inventors/inventor[@sequence="2"]/addressbook/address/text')))
    print("14-3．発明者名称３：：" + str(elem.findtext('.//parties/inventors/inventor[@sequence="3"]/addressbook/name')))
    print("15-3．発明者居所３：：" + str(elem.findtext('.//parties/inventors/inventor[@sequence="3"]/addressbook/address/text')))
    print("14-4．発明者名称４：：" + str(elem.findtext('.//parties/inventors/inventor[@sequence="4"]/addressbook/name')))
    print("15-4．発明者居所４：：" + str(elem.findtext('.//parties/inventors/inventor[@sequence="4"]/addressbook/address/text')))
    print("14-5．発明者名称５：：" + str(elem.findtext('.//parties/inventors/inventor[@sequence="5"]/addressbook/name')))
    print("15-5．発明者居所５：：" + str(elem.findtext('.//parties/inventors/inventor[@sequence="5"]/addressbook/address/text')))
    print("14-6．発明者名称６：：" + str(elem.findtext('.//parties/inventors/inventor[@sequence="6"]/addressbook/name')))
    print("15-6．発明者居所６：：" + str(elem.findtext('.//parties/inventors/inventor[@sequence="6"]/addressbook/address/text')))
    print("16-1．代理人名称１：：" + str(elem.findtext('.//parties/jp:applicants-agents-article/jp:applicants-agents[@sequence="1"]/agent[@sequence="1"][@jp:kind="representative"]/addressbook/name', namespaces={'jp':'http://www.jpo.go.jp'})))
    print("17-1．代理人識別番号１：：" + str(elem.findtext('.//parties/jp:applicants-agents-article/jp:applicants-agents[@sequence="1"]/agent[@sequence="1"][@jp:kind="representative"]/addressbook/registered-number', namespaces={'jp':'http://www.jpo.go.jp'})))
    return
