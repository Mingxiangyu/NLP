# encoding:utf8
import math
from heapq import nlargest
from itertools import product, count

import jieba


# cut_sentences()函数：将一篇文章分割成一个个句子
def cut_sentences(sentence):
    # 以。！？.为结束符，对文章进行分割
    puns = frozenset(u"'。")  # 返回一个冻结的集合
    tmp = []
    for ch in sentence:
        tmp.append(ch)  # 逐字遍历文章并添加到tmp中
        if puns.__contains__(ch):  # 如果遇到句子结束符
            yield ''.join(tmp)  # 将结束符拼接到tmp，并返回
            tmp = []
    yield ''.join(tmp)


# create_stopwords()函数：创建停用词列表
def create_stopwords():
    stop_list = [line.strip() for line in
                 open("../../Chinese_stopword.txt", 'r', encoding='utf-8').readlines()]  # 去除首尾空格，创建停用词列表
    return stop_list


# compute_similarity_by_avg(word_list1,word_list2)函数：使用TextRank算法中计算相似度的方法得出两个向量之间的相似度
def compute_similarity_by_avg(word_list1, word_list2):
    # 两个向量之间的相似度
    words = list(set(word_list1 + word_list2))
    vector1 = [float(word_list1.count(word)) for word in words]
    vector2 = [float(word_list2.count(word)) for word in words]
    vector3 = [vector1[x] * vector2[x] for x in range(len(vector1))]
    vector4 = [1 for num in vector3 if num > 0.]
    co_occur_num = sum(vector4)
    if abs(co_occur_num) <= 1e-12:
        return 0.
    denominator = math.log(float(len(word_list1))) + math.log(float(len(word_list2)))  # 分母
    if abs(denominator) < 1e-12:
        return 0.
    return co_occur_num / denominator


# calculate_score(weight_graph,scores,i)函数：使用TextRank算法的公式计算句子分数
def calculate_score(weight_graph, scores, i):
    # 句子权重计算
    length = len(weight_graph)
    d = 0.85
    added_score = 0.0
    for j in range(length):
        fraction = 0.0
        denominator = 0.0
        # 计算分子
        fraction = weight_graph[j][i] * scores[j]
        # 计算分母
        for k in range(length):
            denominator += weight_graph[j][k]
            if denominator == 0:
                denominator = 1
        added_score += fraction / denominator
    # 计算最终分数
    weighted_score = (1 - d) + d * added_score
    return weighted_score


# weight_sentences_rank(weight_graph)函数：迭代计算句子的分数，直至趋于稳定
def weight_sentences_rank(weight_graph):
    # 句子排序
    # 初始分数设置为0.5
    scores = [0.5 for _ in range(len(weight_graph))]
    old_scores = [0.0 for _ in range(len(weight_graph))]
    # 开始迭代
    while different(scores, old_scores):
        for i in range(len(weight_graph)):
            old_scores[i] = scores[i]
        for i in range(len(weight_graph)):
            scores[i] = calculate_score(weight_graph, scores, i)
    return scores


# def different(scores,old_scores)函数：当句子分数前后相差不到0.0001时迭代结束
def different(scores, old_scores):
    # 判断前后分数有无变化
    flag = False
    for i in range(len(scores)):
        if math.fabs(scores[i] - old_scores[i]) >= 0.0001:
            flag = True
            break
    return flag


# filter_model(sents,model)函数：过滤掉文章中的停用词
def filter_model(sents):
    # 过滤停用词
    stopwords = create_stopwords() + ['。', ' ', '.']
    _sents = []
    for sentence in sents:
        for word in sentence:
            if word in stopwords:
                sentence.remove(word)
        if sentence:
            _sents.append(sentence)
    return _sents


# create_graph(word_sent)函数：建图函数
def create_graph(word_sent):
    # 传入句子链表  返回句子之间相似度的图
    num = len(word_sent[0])
    board = [[0.0 for _ in range(num)] for _ in range(num)]
    for i, j in product(range(num), repeat=2):
        if i != j:
            compute_similarity = compute_similarity_by_avg(word_sent[0][i], word_sent[0][j])
            board[i][j] = compute_similarity
    return board


# summarize(text,n)函数：主函数
def summarize(text, n):
    tokens = cut_sentences(text)
    sentences = []
    sents = []
    for sent in tokens:
        sentences.append(sent)
        sents.append([word for word in jieba.cut(sent) if word])
    # sents = filter_model(sents,model)
    sents = filter_model(sents)
    graph = create_graph(sents)
    scores = weight_sentences_rank(graph)
    sent_selected = nlargest(n, zip(scores, count()))
    sent_index = []
    for i in range(n):
        sent_index.append(sent_selected[i][1])
    return [sentences[i] for i in sent_index]
