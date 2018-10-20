#coding:utf-8
import pandas as pd
import  numpy as np
import re
import sys
import pickle as pkl
from itertools import chain
from sklearn.feature_extraction.text import TfidfVectorizer
import random
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.feature_extraction.text import CountVectorizer

from gensim.models import word2vec

def read_data():
    pkl_file = open('../data/preprocessed_word_lists.pkl', 'rb')
    preprocessed_word_lists = pkl.load(pkl_file)
    name = remove_name('../data/name.txt')
    family_name = remove_name('../data/family_name.txt')

    s = []
    count = 0
    for each in preprocessed_word_lists:
        count = count +1
        u = []
        for i in each:
            if len(i) >=2  and i not in name.keys():
                for eve in family_name.keys():
                    if eve not in i:
                        u.append(i)
        s.append(u)
        sys.stdout.write('generated:{0}/total:{1}\r'.format(count, 950018))
        sys.stdout.flush()
    return s

def remove_name(path):
    name = {}
    index = 0
    with open(path,'r',encoding='utf-8') as f1:
        for line in f1.readlines():
            name[line.strip()] = index
            index = index + 1
    return name

def compute_count(preprocessed_word_lists):
    word_dic_count = {}
    count = 0
    for each in preprocessed_word_lists:
        for i in each:
            if i in word_dic_count.keys():
                word_dic_count[i] = word_dic_count[i] + 1
            else:
                word_dic_count[i] = 1
            count = count + 1
            sys.stdout.write('generated:{0}/total:{1}\r'.format(count, 950018))
            sys.stdout.flush()
    #print(word_dic_count)
    with open('../data/word_dic_count.pkl', 'wb') as output:
        pkl.dump(word_dic_count, output)
    return word_dic_count

def read_relevent_word():
    relevent_word = []
    with open('../data/relevant_word_dict.txt','r',encoding='utf-8') as f:
        for line in f.readlines():
            relevent_word.append(line.strip())
    with open('../data/high_relevant_word_dict.txt','r',encoding='utf-8') as f1:
        for line in f1.readlines():
            relevent_word.append(line.strip())
    return set(relevent_word)

def find_word(word_dic_count,relevent_word):
    word = []
    h_word = []
    count = 0
    for each in word_dic_count:
        count = count + 1
        if '电' in each[0]:
            word.append(each[0])
            word_dic_count.remove(each)
        sys.stdout.write('generated:{0}/total:{1}\r'.format(count, 950018))
        sys.stdout.flush()
    count = 0
    # for each in word_dic_count:
    #     count = count + 1
    #     if each[0] in relevent_word:
    #         word.append(each[0])
    #     sys.stdout.write('generated:{0}/total:{1}\r'.format(count, 950018))
    #     sys.stdout.flush()
    #word = list(chain(word_dic_count,word))

    with open('../data/word.pkl', 'wb') as output:
        pkl.dump(word, output)
    pkl_file = open('../data/word.pkl', 'rb')
    word = list(set(pkl.load(pkl_file)))
    test = pd.DataFrame(word)
    #test['word'] = word
    test.to_csv('../data/word.csv',encoding='utf-8',index=False)

def train_tfidf_vectorizer(preprocessed_word_lists):
    # train tfidf vectorizer

    tfidf = TfidfVectorizer()
    tfidf_vectorizer = tfidf.fit(preprocessed_word_lists) # 提取的向量
    doc_vectors = tfidf_vectorizer.transform(preprocessed_word_lists)
    # with open('../data/doc_vectors.pkl', 'wb') as output:
    #     pkl.dump(doc_vectors, output)

    word_2_idx = tfidf_vectorizer.vocabulary_ #?
    idx_2_word = {v: k for k, v in word_2_idx.items()} #?
    # with open('../data/idx_2_word.pkl', 'wb') as output:
    #     pkl.dump(idx_2_word, output)
    return  doc_vectors ,word_2_idx, idx_2_word

# def train_tfidf_vectorizer(preprocessed_word_lists):
#     vectorizer = CountVectorizer()
#     cif = vectorizer.fit_transform(preprocessed_word_lists)
#     transformer = TfidfTransformer()
#     tfidf = transformer.fit_transform(cif )
#     word = vectorizer.get_feature_names()#得到所有切词以后的去重结果列表
#     word = np.array(word) #把词语列表转化为array数组形式
#     weight = tfidf.toarray()#将tf-idf矩阵抽取出来
#     word_index = np.argsort(-weight)
#     word = word[word_index]#把word数组按照tfidf从大到小排序
#     tags = []
#     for i in range(5000):
#         tags.append(word[0][i])
#     with open('../data/word.pkl', 'wb') as output:
#         pkl.dump(tags, output)

def combine_word(preprocessed_word_lists,num):
    new_word = []
    index = 0
    while index < len(preprocessed_word_lists):
        temp = []
        for i in preprocessed_word_lists[index:index + num]:
            temp.extend(i)
        new_word.append(temp)
        index = index + num
    sys.stdout.write('generated:{0}/total:{1}\r'.format(index, 950018))
    sys.stdout.flush()
    return new_word



def train_word2vec(preprocessed_word_lists):
    model = word2vec.Word2Vec(preprocessed_word_lists,
                     size=200, window=5, min_count=2, sg=1, workers=2)
    model.save('../data/word_2_vector.model')

if __name__ =='__main__':

    preprocessed_word_lists = read_data()
    random.shuffle(preprocessed_word_lists)
    print(preprocessed_word_lists[:10])
    preprocessed_word_lists = combine_word(preprocessed_word_lists,100)
    with open('../data/new_words.pkl', 'wb') as output:
        pkl.dump(preprocessed_word_lists, output)



    # pkl_file = open('../data/new_words.pkl', 'rb')
    # preprocessed_word_lists = pkl.load(pkl_file)
    # print(preprocessed_word_lists)

    # print(preprocessed_word_lists[:1])
    # words = []
    # for i in preprocessed_word_lists:
    #     words.append(' '.join(i))

    # train_word2vec(preprocessed_word_lists)
    # print('finshing')
    # length = [len(each) for each in preprocessed_word_lists]
    # word_dic_count = compute_count(preprocessed_word_lists)
    # pkl_file = open('../data/word_dic_count.pkl', 'rb')
    # word_dic_count = pkl.load(pkl_file)
    # word_dic_count = sorted(word_dic_count.items() ,key= lambda x:x[1],reverse=True)
    # #
    # # print(word_dic_count[:12])
    # relevent_word = read_relevent_word()
    # find_word(word_dic_count,relevent_word)

    # train_tfidf_vectorizer(words)
    # pkl_file = open('../data/doc_vectors.pkl', 'rb')
    # doc_csr = pkl.load(pkl_file)
    #
    # pkl_file = open('../data/idx_2_word.pkl', 'rb')
    # idx_2_word = pkl.load(pkl_file)
    # submit_word  =[]
    # weight = doc_csr.toarray()
    # for i in range(len(weight)):
    #     print(max(weight[i]))
    #     submit_word.append(idx_2_word[weight[i].index(max(weight))])



    # pkl_file = open('../data/sorted_words.pkl', 'rb')
    # sorted_words = list(set(pkl.load(pkl_file)))
    # print(len(set(sorted_words)))
    # sorted_words.reverse()
    # demo = []
    # for i in sorted_words:
    #     if '电' in i:
    #         demo.append(i)
    #         print(i)
    # print(len(demo))
    # # print(type(sorted_words))
    # writerCSV = pd.DataFrame()
    # writerCSV[''] = submit_word
    # writerCSV.to_csv('../data/11-27-reverse-dian.csv', encoding='utf-8',index=False)

