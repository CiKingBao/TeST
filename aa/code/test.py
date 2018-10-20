#coding:utf-8
import numpy as np

def combine_word(preprocessed_word_lists,num):
    new_word = []
    index = 0
    while index < len(preprocessed_word_lists):
        temp = []
        for i in preprocessed_word_lists[index:index + num]:
            temp.extend(i)
        new_word.append(temp)
        index = index + num
    return new_word

if __name__ =='__main__':
    # X_test = ['没有 你 的 地方 都是 他乡', '没有 你 的 旅行 都是 流浪']
    # print(type(X_test[1]))
    l = [[2,1,3],[42,1,45],[134,34,21]]
    l = np.array(l)
    print(list(l[1]).index(max(l[1])))