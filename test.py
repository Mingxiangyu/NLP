import codecs
import re

import jieba

file_chinese_one = codecs.open('cut_zh_wiki.txt',"a+",'utf-8')
#file_chinese_two = codecs.open('cut_zh_wiki_01.txt',"a+",'utf-8')
stopwordslist = [line.strip() for line in open('stopwords.txt',encoding='utf-8').readlines()] #创建停用词列表


for line in open("chinese_corpus/zh_wiki_00",'r',encoding='utf-8'):
    for i in re.sub('[a-zA-Z0-9]', '', line).split(' '):
        if i != '':
            data = list(jieba.cut(i, cut_all = False))
            readline = ' '.join(data) + '\n'
            file_chinese_one.write(readline)

file_chinese_one.close()
#去除停用词

for line in open("zh_wiki","r",encoding='utf-8'):
    for i in re.sub('[a-zA-Z0-9]','',line).split(' '):
        if i != '':
            data = list(jieba.cut(i,cut_all=False))
            outstr = ''
            for word in data:
                if word not in stopwordslist:
                    if word != '\t':
                        outstr += word
                        outstr += " "
            file_chinese_one.write(outstr + '\n')

file_chinese_one.close()