# import modules & set up logging
#!/bin/bash
# -*-coding=utf-8-*-
import logging
import os
#!/bin/bash
# -*-coding=utf-8-*-
import jieba
import re
from gensim.models import word2vec
import multiprocessing
import gensim
from gensim.models import word2vec
coding = 'utf-8'
source_corpus_text = 'source.txt'
size = 100
window = 5
min_count = 1
workers = multiprocessing.cpu_count()
    
train_corpus_text = '31.txt'
model_text = 'w2v_size_{0}.model'.format(size)

sentences = word2vec.LineSentence(train_corpus_text)
model = word2vec.Word2Vec(sentences=sentences, size=size, window=window, min_count=min_count, workers=workers,hs=1,sg=1)
model.save(model_text)
model = gensim.models.Word2Vec.load(model_text)
similar_words = model.most_similar('老师')
# for word in similar_words:
#     print(word[0], word[1])
print(similar_words[0][1],similar_words[0][0])




# logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
# def funcA():
#     sentences = word2vec.LineSentence('./2.txt')
#
#     model = word2vec.Word2Vec(sentences,sg=1, hs=1,min_count=1,window=4,size=100, model_text = 'w2v_size_{0}.model'.format(size))
#     print(model.wv.similarity('老师', '班主任'))
#     req_count = 5
#     list1= []
#     list2 = []
#     for key in model.wv.similar_by_word('老师', topn =10):
# 	    if len(key[0])==2:
#             # req_count -= 1
# 		    list1.append(key[0])
# 		    list2.append(key[1])
#     return(list1,list2)

# if __name__ == '__main__':
#     # funcA()
#     # list1, list2 = funcA()
#     # print(list1)
