# cd …　パス移動。cd .. で一つ上に移動
#                 cd []で[]に移動
# tree … ディレクトリ構造を出力、/fオプションでファイル名も出力
# push rejectedの時は、ctr + push を押す。
# -*- coding: utf-8 -*-
import sys # sysモジュール読み込み
import glob # globモジュール読み込み
import os # osモジュール読み込み
import codecs # codecsモジュールの読み込み
from xml.etree import ElementTree
import xml.etree.ElementTree as ET
# sys.stdout = codecs.getwriter('utf_8')(sys.stdout)

drive =  r"C:\Users\T15015\PycharmProjects\test_area\test_area"
write_csv_dir = r"C:\Users\T15015\PycharmProjects\test_area\test_area\save"

os.chdir(drive) # 読み込み先に移動

x = '2017201111.xml'
tree = ElementTree.parse(x)
root = tree.getroot()
print(root.findall('.//country'))
print(root.findall('.//kind'))
print(root.findall('.//date'))
print(root.findall('.//'))
print(root.findall('.//'))
print(root.findall('.//'))
print(root.findall('.//'))
print(root.findall('.//'))
print(root.findall('.//'))
print(root.findall('.//'))
print(root.findall('.//'))
#tree = ElementTree.parse(x)
#root = tree.getroot()
#print(root.findtext('kind'))
