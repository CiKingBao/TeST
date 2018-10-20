import pandas as pd
import re
import find_word
import sys
import pickle as pkl
from itertools import chain
def read_wiki_data():
    wiki_data = []
    count =0
    with open('../data/wiki_sentence_list.txt', 'r',encoding='utf-8') as f:
        for line in f.readlines():
            count = count +1
            wiki_data.append(line)
            sys.stdout.write('generated:{0}/total:{1}\r'.format(count, 838152))
            sys.stdout.flush()
    with open('../data/wiki_data.pkl','wb') as output:
        pkl.dump(wiki_data,output)
    #wiki_data = list(chain(*wiki_data))[0]
    return wiki_data

def filter_begin(wiki_data,difference_set_word,num):
    ww = []
    count = 0
    for each in difference_set_word:
        count = count + 1
        flag = 0
        for wiki in wiki_data:
            if num == 1:
                if wiki.find(each) >= 0:
                    flag = 1
                    break
            elif num == -1:
                #print(wiki)
                if each.find(wiki) >= 0:
                    flag = 1
                    break
        if flag == 0:
            ww.append(each)
        sys.stdout.write('generated:{0}/total:{1}\r'.format(count, 19114))
        sys.stdout.flush()

    return ww

if __name__ == '__main__':
    print('1')
    # wiki_data = read_wiki_data()
    # print('read wiki data done')
    # difference_set_word = find_word.intersecte()
    #
    # print('read difference word done')
    #
    # ww = filter_begin(wiki_data,difference_set_word,1)
    # print(len(ww))
    # writerCSV = pd.DataFrame()
    # writerCSV[''] = ww
    # writerCSV.to_csv('../data/ww.csv',header= False,encoding='utf-8',index=False)

    # stop_words = find_word.read_stopwords()
    # data = pd.read_csv('../data/pp_filter.csv')
    # w15w_word = list(data['电压'])
    # ww = filter_begin(stop_words, w15w_word, -1)
   # ww = filter_begin(wiki_data, ww, 1)
    # # filtered_word = [i for i in w15w_word if i not in ww]
    # # print('ww',len(set(ww)))
    # # print('filtered_word',len(set(filtered_word)))
    # writerCSV = pd.DataFrame()
    # writerCSV[''] = ww
    # writerCSV.to_csv('../data/sogou_0_10000_filter_stopwords.csv',header= False,encoding='utf-8',index=False)

    # data = pd.read_csv('../data/mark2_dealed.csv')
    # content = list(data['content'])
    # words = []
    # count = 0
    # for i in content:
    #     count = count +1
    #     words.append(find_word.clean_data(i))
    #     sys.stdout.write('generated:{0}/total:{1}\r'.format(count, 30000))
    #     sys.stdout.flush()
    # with open('../data/market2_word.pkl','wb') as output:
    #     pkl.dump(words,output)

    # data = pd.read_csv('../data/4w_baidu_data_filter_words.csv')
    # w15w_word = list(data['电机'])
    # w = []
    # for i in w15w_word:
    #     if len(i) ==4:
    #         w.append(i)
    # print(len(w))
    # w = [i for i in w if '电' in i]
    # ww = filter_begin(stop_words, w, -1)
    # writerCSV = pd.DataFrame()
    # writerCSV[''] = w
    # writerCSV.to_csv('../data/word_filter_stopword_len=4=电.csv',header= False,encoding='utf-8',index=False)

