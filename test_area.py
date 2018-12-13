# -*- coding: utf-8 -*-
import sys # sysモジュール読み込み
import glob # globモジュール読み込み
import os # osモジュール読み込み
import codecs # codecsモジュールの読み込み
from xml.etree.ElementTree import *
# sys.stdout AA codecs.getwriter('utf_8')(sys.stdout)

drive =  r"C:\Users\T15015\PycharmProjects\test_area\test_area\save"
write_csv_dir = r"C:\Users\T15015\PycharmProjects\test_area\test_area\save"

os.chdir(drive) # 読み込み先に移動

x = '2017200451.xml'
tree = parse(x)
#tree = tree.replace("=", "AA")
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
print("11-2．出願人名称２：：" + str(elem.findtext('.//parties/jp:applicants-agents-article/jp:applicants-agents[@sequence="2"]/applicant[@sequence="2"]/addressbook[@lang="ja"]/name', namespaces={'jp':'http://www.jpo.go.jp'})))
print("12-2．出願人居所２：：" + str(elem.findtext('.//parties/jp:applicants-agents-article/jp:applicants-agents[@sequence="2"]/applicant[@sequence="2"]/addressbook[@lang="ja"]/address/text', namespaces={'jp':'http://www.jpo.go.jp'})))
print("11-3．出願人名称３：：" + str(elem.findtext('.//parties/jp:applicants-agents-article/jp:applicants-agents[@sequence="3"]/applicant[@sequence="3"]/addressbook[@lang="ja"]/name', namespaces={'jp':'http://www.jpo.go.jp'})))
print("12-3．出願人居所３：：" + str(elem.findtext('.//parties/jp:applicants-agents-article/jp:applicants-agents[@sequence="3"]/applicant[@sequence="3"]/addressbook[@lang="ja"]/address/text', namespaces={'jp':'http://www.jpo.go.jp'})))
print("11-4．出願人名称４：：" + str(elem.findtext('.//parties/jp:applicants-agents-article/jp:applicants-agents[@sequence="4"]/applicant[@sequence="4"]/addressbook[@lang="ja"]/name', namespaces={'jp':'http://www.jpo.go.jp'})))
print("12-4．出願人居所４：：" + str(elem.findtext('.//parties/jp:applicants-agents-article/jp:applicants-agents[@sequence="4"]/applicant[@sequence="4"]/addressbook[@lang="ja"]/address/text', namespaces={'jp':'http://www.jpo.go.jp'})))
print("11-5．出願人名称５：：" + str(elem.findtext('')))
print("12-5．出願人居所５：：" + str(elem.findtext('.//parties/jp:applicants-agents-article/jp:applicants-agents[@sequence="5"]/applicant[@sequence="5"]/addressbook[@lang="ja"]/address/text', namespaces={'jp':'http://www.jpo.go.jp'})))
print("11-6．出願人名称６：：" + str(elem.findtext('')))
print("12-6．出願人居所６：：" + str(elem.findtext('')))
print("11-7．出願人名称７：：" + str(elem.findtext('')))
print("12-7．出願人居所７：：" + str(elem.findtext('')))

# 発行国：：publication-reference / document-id / country
# 公報種別：：publication-reference / document-id / kind
# 公開日：：publication-reference / document-id / date
# 出願日：：application-reference / document-id / date
# 公開番号：：publication-reference / document-id / doc-number
# 出願番号：：application-reference / document-id / doc-number
# 発明の名称：：invention-title
# 国際特許分類：：classification-ipc / edition/ / main-clsf
# 請求項の数：：number-of-claims
# 全頁数：：jp:total-pages
# 出願人名称：：parties / jp:applicants-agents-article / jp:applicants-agents / applicant sequence / addressbook / name
# 出願人居所：：parties / jp:applicants-agents-article / jp:applicants-agents / applicant sequence / addressbook / address / text
# 出願人識別番号：：parties / jp:applicants-agents-article / jp:applicants-agents / applicant sequence / addressbook / registered-number
# 発明者名称：：parties / inventors / inventor sequenceAA"1" / addressbook / name
# 発明者居所：：parties / inventors / inventor sequenceAA"1" / addressbook / name
# 代理人名称：：parties / jp:applicants-agents-article / jp:applicants-agents / agent / addressbook / name
# 代理人識別番号：：parties / jp:applicants-agents-article / jp:applicants-agents / agent / addressbook / registerd-number
