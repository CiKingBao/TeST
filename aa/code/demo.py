# encoding=utf-8

import os
import glob
import math
import pickle
import datetime
import sys
import re

import pandas as pd
import numpy as np
import jieba

reload(sys)
sys.setdefaultencoding('utf-8')


# -------------------------------------------------
def read_corpus_file(fn):
    lines = []

    f = open(fn, 'r')

    for line in f:
        t = ""
        try:
            t = line.decode("UTF-8")
        except:
            print
            "charactor code error UTF-8"
        if t == "":
            try:
                t = line.decode("GBK")
            except:
                print
                "charactor code error GBK"
        s = t.strip()
        lines.append(s)

    return lines


# -------------------------------------------------
def clean_line_hanzi(line):
    line = re.sub('[\r\n\t]', '', line)
    line = re.sub('\d+', '', line)
    line = re.sub('[A-Za-z]+', '', line)

    return line


# -------------------------------------------------
def filter_words(words):
    new_words = []

    for w in words:
        x = w.strip()
        x = ''.join(re.findall(u'[\u4e00-\u9fff]+', x))
        if len(x) < 2 or len(x) > 8:
            continue
        new_words.append(x)

    return new_words


# -------------------------------------------------
lines = read_corpus_file("../data/keyword.txt")
lines = [clean_line_hanzi(x) for x in lines]

words = []
for line in lines:
    s = line
    s = s.replace(u"关键词", " ")

    s = s.replace(u"：", " ")
    s = s.replace(u":", " ")

    s = s.replace(u"；", " ")
    s = s.replace(u";", " ")

    s = s.replace(u"，", " ")
    # s = s.replace(u","," ")

    s = s.replace(u"　", " ")

    w = s.split(" ")
    words.extend(filter_words(w))

words = list(words)
df1 = pd.DataFrame(words)
df1.to_csv("./demo.txt" , index=False, header=None)

print("OK!")
