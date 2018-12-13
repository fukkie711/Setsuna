import sys # sysモジュール読み込み
import glob # globモジュール読み込み
import os # osモジュール読み込み
import codecs # codecsモジュールの読み込み
from tkinter import * # *モジュール読み
from tkinter import ttk # ttkモジュール読み込み
from tkinter import filedialog # filedialogモジュール読み込み
from tkinter import messagebox # messageboxモジュール読み込み
from Function import create_xml_list

sss = r"C:\Users\T15015\PycharmProjects\test_area\test_area"
list_max = 0
path_list =[]
list_max, path_list = create_xml_list(sss)
print(list_max)
print(path_list)
