import  pandas as pd
import  pickle as pkl
from itertools import chain
def baidu_data_filter_word():

    pkl_file = open('../data/market2_word.pkl', 'rb')
    preprocessed_word_lists = pkl.load(pkl_file)
    preprocessed_word_lists = list(chain(*preprocessed_word_lists))
    sl = set()
    for i in list(set(preprocessed_word_lists)):
        sl.add(i)
    # print(preprocessed_word_lists)
    # print(len(set(preprocessed_word_lists)))

    data = pd.read_csv('../data/15w.csv')
    w15w_word = list(data['ci'])
    word = []
    for each in w15w_word:
        if each not in sl:
            word.append(each)
    print(len(word))
    # word = [i for i in word if len(]
    writerCSV = pd.DataFrame()
    writerCSV[''] = word
    writerCSV.to_csv('../data/all_baidu_data_filter_15w.csv', header=False, encoding='utf-8', index=False)


if __name__ =='__main__':
    data = pd.read_csv('../data/keywords_tfidf.csv')
    #w15w_word = list(data['脉冲'])

    # word = word.extend(list(data['数目']))
    w1 = list(data['数目'])
    w2 = list(data['极化'])
    w3 = list(data['铁构件'])
    w4 = list(data['测量'])
    w5 = list(data['系统'])
    word = list(chain(*[w1,w2,w3,w4,w5]))
    word = list(set(word))
    # print(len(set(word)))
    # print(len(word))
    # writerCSV = pd.DataFrame()
    # writerCSV[''] = list(set(word))
    # writerCSV.to_csv('../data/tfidf_words.csv', header=False, encoding='utf-8', index=False)

    data = pd.read_csv('../data/sogou_0_10000.csv')
    w15w_word = list(data['电压'])
    w15w_word = set(w15w_word)
    new_word = []
    for i in word:
        if i in w15w_word:
            new_word.append(i)
    print(len(new_word))
    writerCSV = pd.DataFrame()
    writerCSV[''] = new_word
    writerCSV.to_csv('../data/tfidf_sogou_0_10000_filter_word.csv', header=False, encoding='utf-8', index=False)

