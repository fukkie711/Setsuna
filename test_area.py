# cd …　パス移動。cd .. で一つ上に移動
#                 cd []で[]に移動
# tree … ディレクトリ構造を出力、/fオプションでファイル名も出力
# push rejectedの時は、ctr + push を押す。
# -*- coding: utf-8 -*-
import sys # sysモジュール読み込み
import glob # globモジュール読み込み
import os # osモジュール読み込み
import codecs # codecsモジュールの読み込み
from xml.etree.ElementTree import *
# sys.stdout = codecs.getwriter('utf_8')(sys.stdout)

drive =  r"C:\Users\T15015\PycharmProjects\test_area\β_test\β_drive"
write_csv_dir = r"C:\Users\T15015\PycharmProjects\test_area\test_area\save"

os.chdir(drive) # 読み込み先に移動

x = '2017200451.xml'
tree = parse(x)
elem = tree.getroot()
print(elem.findtext('.//publication-reference/document-id/country')) # 発行国
print(elem.findtext('.//publication-reference/document-id/kind')) # 公報種別
print(elem.findtext('.//publication-reference/document-id/date')) # 公開日
print(elem.findtext('.//publication-reference/document-id/doc-number')) # 公開番号
print(elem.findtext('.//application-reference/document-id/doc-number')) # 出願番号
print(elem.findtext('.//invention-title')) # 発明の名称
print(elem.findtext(r'.//classification-ipc/main-clsf')) # 国際特許分類(IPC)
print(elem.findtext('.//number-of-claims')) # 請求項の数
print(elem.findtext('.//:total-pages')) # 全頁数



# 発行国：：publication-reference / document-id / country
# 公報種別：：publication-reference / document-id / kind
# 公開日：：publication-reference / document-id / date
# 公開番号：：publication-reference / document-id / doc-number
# 出願番号：：application-reference / document-id / doc-number
# 発明の名称：：invention-title
# 国際特許分類：：classification-ipc / edition/ / main-clsf
# 請求項の数：：number-of-claims
# 全頁数：：jp:total-pages
# 出願人名称：：parties / jp:applicants-agents-article / jp:applicants-agents / applicant sequence / addressbook / name
# 出願人居所：：parties / jp:applicants-agents-article / jp:applicants-agents / applicant sequence / addressbook / address / text
# 出願人識別番号：：parties / jp:applicants-agents-article / jp:applicants-agents / applicant sequence / addressbook / registered-number
# 発明者名称：：parties / inventors / inventor sequence="1" / addressbook / name
# 発明者居所：：parties / inventors / inventor sequence="1" / addressbook / name
# 代理人名称：：parties / jp:applicants-agents-article / jp:applicants-agents / agent / addressbook / name
# 代理人識別番号：：parties / jp:applicants-agents-article / jp:applicants-agents / agent / addressbook / registerd-number
