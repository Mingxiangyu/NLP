import logging

from gensim.models import word2vec

logging.basicConfig(format = '%(asctime)s : %(levelname)s : %(message)s',level=logging.INFO)
sentences_one = word2vec.LineSentence(u'./cut_zh_wiki.txt')
#sentences_two = word2vec.LineSentence(u'./cut_zh_wiki_01.txt')
model_one = word2vec.Word2Vec(sentences_one,size=200,window=10,min_count=64,sg=1,hs=1,iter=10,workers=25)
#model_two = word2vec.Word2Vec(sentences_two,size=200,window=10,min_count=64,sg=1,hs=1,iter=10,workers=25)
model_one.save(u'./train_test_x/word2vec2')
#model_one.wv.save_word2vec_format(u'./w2v',binary=False)
#model_two.save(u'./word2vec2')