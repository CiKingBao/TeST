# encoding=utf-8

import pandas as pd
import start_game
import jieba
import pickle  as pkl
from itertools import chain
import numpy as np
import re
import sys

def tf_idf_find_word():
    pkl_file = open('../data/doc_vectors.pkl', 'rb')
    doc_csr = pkl.load(pkl_file)

    pkl_file = open('../data/idx_2_word.pkl', 'rb')
    idx_2_word = pkl.load(pkl_file)

    #feature_dict = {v: k for k, v in doc_csr.vocabulary_.items()}  # index -> feature_name
    top_n_matrix = np.argsort(-doc_csr.todense())[:, :5]  # top tf-idf words for each row
    df = pd.DataFrame(np.vectorize(idx_2_word.get)(top_n_matrix))  # convert matrix to df
    df.to_csv("../data/keywords.csv", header=False, encoding='utf-8',index=False)


def _remove_urls(s):
    #print('s:',s)
    return re.sub(r"http\S+", "", s)

def _replace_long_white_spaces(s):
    return re.sub(r"\s+", " ", s)

def _remove_punctuations(s):
    return re.sub(r"\W+", " ", s)

def _remove_html_tags(s):
    return re.sub(r"<[/\w]*>", "", s)


def clean_text(text):
    text = text.strip()
    text = _remove_urls(text)
    text = _remove_html_tags(text)
    text = _replace_long_white_spaces(text)
    return text

def read_stopwords():
    stop_words = []
    with open('../data/chineseStopWords.txt','r') as f:
        for line in f.readlines():
            stop_words.append(line.strip())
    return stop_words


def _remove_useless_words(wl, stop_words):

    wl = [w for w in wl if w not in stop_words]
    wl = [''.join(re.findall(u'[\u4e00-\u9fff]+',w)) for w in wl if re.match(r"[-.%+\d]+", w) is None]
    wl = [each for each in wl if each!='']
    return wl

def clean_data(line):
    stop_words = read_stopwords()
    line = clean_text(line)
    text = _remove_punctuations(line)
    # text = [''.join(re.findall(u'[\u4e00-\u9fff]+',text))][0]
    split_word = '/'.join(jieba.cut_for_search(text, HMM=True))
    words = split_word.split('/')
    words = _remove_useless_words(words, stop_words)
    return  words

def jieba_split_word():

    jieba_spilt_words_list = []
    count = 0
    with open('../data/electric_data.txt', 'r',encoding='utf-8') as f:
        for line in f.readlines():
            count = count + 1
            words = clean_data(line)
            jieba_spilt_words_list.append(words)
            sys.stdout.write('generated:{0}/total:{1}\r'.format(count, 950018))
            sys.stdout.flush()
    return jieba_spilt_words_list

def intersecte():

    # pkl_file = open('../data/preprocessed_word_lists.pkl', 'rb')
    # preprocessed_word_lists = pkl.load(pkl_file)
    # preprocessed_word_lists = list(chain(*preprocessed_word_lists))
    jieba_spilt_words_list = jieba_split_word()
    with open('../data/jieba_split_words.pkl','wb') as output:
        pkl.dump(jieba_spilt_words_list,output)
    data = pd.read_csv('../data/15w.csv')
    w15w_word = data['ci']

    # file_pkl = open('../data/jieba_split_words.pkl','rb')
    # jieba_spilt_words_list = pkl.load(file_pkl)
    # jieba_spilt_words_list = list(chain(*jieba_spilt_words_list))
    # set_jieba_spilt_words_list = set()
    # for i in jieba_spilt_words_list:
    #     set_jieba_spilt_words_list.add(i)
    # difference_set_word = []
    # count = 0
    # for each in w15w_word:
    #     count = count + 1
    #     if each in set_jieba_spilt_words_list:
    #         difference_set_word.append(each)
    #     sys.stdout.write('generated:{0}/total:{1}\r'.format(count, 150000))
    #     sys.stdout.flush()
    # print('/n',len(difference_set_word))
    # return difference_set_word



if __name__ =='__main__':


    # k = ' '.join(word)
    # p = []
    # p.append(k)
    # doc_vectors, word_2_idx, idx_2_word = start_game.train_tfidf_vectorizer(p)
    #intersecte(w15w_word)
    print('done')

    # ss  = [''.join(re.findall(u'[\u4e00-\u9fff]+','根据1000kV特高压交流输电工程线路(南荆段)的结构参数(同前述)，按式(12)−式(15)可以推算出操作过电压等值风速条件下'
    #                                             '悬垂串风偏后的水平位移[21-23]：ssv0h=νγvk(12)22dscsH0.625sinαμνθ=Fdl(13)djdj0.'
    #                                             '5arctan()0.5FFGGφ+=+(14)sinφ=lL(15)式中：0v 为基准高度为10m的基本风速，m/s；'))]
    #
    # print(ss)
    # file_pkl = open('../data/jieba_split_words.pkl','rb')
    # jieba_spilt_words_list = pkl.load(file_pkl)
    # print(jieba_spilt_words_list[:100])


