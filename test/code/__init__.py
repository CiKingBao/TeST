
import gensim
import numpy as np
model = gensim.models.word2vec.Word2Vec.load('../data/word_2_vector.model')
import pandas as pd
import jieba
import pickle as pkl
import sys
def buildWordVector(imdb_w2v,text, size):
    vec = np.zeros(size).reshape((1, size))
    count = 0.
    #print text
    for word in text.split():
        #print word
        try:
            vec += imdb_w2v[word].reshape((1, size))
            count += 1.
        except KeyError:
            print(word)
            continue
    if count != 0:
        vec /= count
    return vec
def find_dian_word():
    pkl_file = open('../data/new_words.pkl', 'rb')
    preprocessed_word_lists = pkl.load(pkl_file)
    word = []
    count = 0
    tmpt = []
    ci =['电','网','磁','流','感','源','揽','频','耦',
         '热','压','场','量','信','圈','耗','能','建',
         '机','燃','控','负','巡','阻','匝','线','度',
         '势','经','缘','贮','波','气','障','操','微',
         '谐','联','监','光','趋']
    for ele in preprocessed_word_lists:
        count = count + 1
        for each in ele:
            if '电' in each:
                word.append(each)
        sys.stdout.write('generated:{0}/total:{1}\r'.format(count, 950018))
        sys.stdout.flush()
    new_word = []
    for i in word:
        ss = '/'.join(jieba.cut_for_search(i, HMM=False))
        ss = ss.split('/')
        for eve in ss:
            for ele in ci:
                if ele in eve and len(eve)>=2:
                    new_word.append(eve)
            else:
                continue
    df = pd.DataFrame()
    df[''] = list(set(new_word))
    df.to_csv('9-27-one_2.csv',encoding='utf-8',index=False)
    print(len(set(new_word)))
    return new_word


if __name__=='__main__':

    # x_vecs = np.concatenate([buildWordVector(model,z, 200) for z in x])
    # x_vecs = scale(x_vecs)
    # relevent_word = []
    # with open('../data/high_relevant_word_dict.txt','r',encoding='utf-8') as f1:
    #     for line in f1.readlines():
    #         relevent_word.append(line.strip())
    # new_word = list(set(find_dian_word()))
    # word = []
    # count = 0
    # for i in new_word:
    #     count = count + 1
    #     sys.stdout.write('generated:{0}/total:{1}\r'.format(count, len(new_word)))
    #     sys.stdout.flush()
    #     try:
    #         for each in model.most_similar(i,topn=20):
    #             word.append(each[0])
    #     except:
    #         print('one error')
    #
    # print(model.most_similar('电网',topn=20))


    # writerCSV = pd.DataFrame()
    # writerCSV[''] = list(set(word))
    # writerCSV.to_csv('../data/aa.csv', encoding='utf-8',index=False)
    #print(model.most_similar('电网', topn=20))
    # ss = '/'.join(jieba.cut_for_search('固定电容器组', HMM=False))
    # print(ss.split('/'))

    #l = find_dian_word()
    data = pd.read_csv('../data/sogou_0_10000.csv',encoding='utf-8')
    #print(list(data['电压']))
    ori_data = list(data['电压'])
    word = []
    for i in ori_data:
        ss = '/'.join(jieba.cut_for_search(i, HMM=False))
        print(ss.split('/'))
        for each in ss.split('/'):
            if len(each)>=2:
                word.append(each)
    # print(word)
    # print(len(set(word)))
    new_word = []
    for eve in word:
        if eve not in ori_data:
            new_word.append(eve)
    print(new_word)
    print(len(set(new_word)))
    w = []
    for ele in ori_data:
        if len(ele)<5:
            w.append(ele)
    print(len(w))
    w = list(set(w+new_word))
    print(len(w))

    writerCSV = pd.DataFrame()
    writerCSV['电压'] = list(set(w))
    writerCSV.to_csv('../data/ww.csv', encoding='utf-8',index=False)
