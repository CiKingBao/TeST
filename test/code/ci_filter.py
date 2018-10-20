import pandas as pd
import re
import word_filter
import sys
import pickle as pkl
from itertools import chain
path = 'C:/Users/cyb/Downloads/词库/专业扩充词库/金山打字通2003专业词库/'

def read_stopwords(path_name):
    stop_words = []
    with open(path_name,'r',encoding='utf-8') as f:
        for line in f.readlines():
            if line =='':
                print(99)
                continue
            print(line)
            stop_words.append(line.strip())
    return stop_words

if __name__ == '__main__':

    # file_name = ['地理CN.TXT','化学CN.TXT','建筑CN.TXT','农学CN.TXT','数学CN.txt','心理学CN.txt','医学CN.TXT','物理CN.txt']
    # # ci = ['污','秽','切','藻','盲','新','云','硬']
    # data = pd.read_csv('../data/409836_full_229_gai.csv')
    # submit_words = list(data['电压'])

    # clean_words = []
    # filtered_word = []
    # for i in submit_words:
    #     for each in ci :
    #         if each in i:
    #             filtered_word.append(i)
    # print(filtered_word)
    # print(len(filtered_word))
    #stop_words = []
    # for i in file_name:
    #     stop_words.extend(read_stopwords(path+i))
    # # ww = word_filter.filter_begin(stop_words, submit_words, -1)
    # stop_words = set(stop_words)
    # ww = [i for i in submit_words if not i in stop_words]
    # # print('ppp')
    # # print(stop_words)
    # # print(len(stop_words))
    # print(ww)
    # print(len(submit_words))
    # print(len(ww))

    # stop_words = read_stopwords('../data/ele_words.txt')
    # print(stop_words)
    # writerCSV = pd.DataFrame()
    # writerCSV['电压'] = list(set(submit_words))[:10001]
    # writerCSV.to_csv('../data/add_new_word.csv',header= False,encoding='utf-8',index=False)
    # print(len(set(submit_words[:10001])))

    data = pd.read_csv('../data/electric_corpus.csv')
    content = list(data['content'])
    df = pd.read_csv('../data/409836_full_229_gai.csv')
    submit_words = list(df['电压'])
    word = []
    count =0
    for i  in submit_words[10000:20000]:
        count = count +1
        for each in content:
            if  i in str(each) :
                word.append(i)
                break
        sys.stdout.write('generated:{0}/total:{1}\r'.format(count, 10000))
        sys.stdout.flush()
    print(len(word))
    stop_words =  word_filter.read_stopwords()
    ww = word_filter.filter_begin(stop_words, word, -1)
    writerCSV = pd.DataFrame()
    writerCSV['电压'] =  ww
    writerCSV.to_csv('../data/zheng_filter_stop_words_10000_20000.csv',header= False,encoding='utf-8',index=False)
    #print(len(set(submit_words[:10001])))
