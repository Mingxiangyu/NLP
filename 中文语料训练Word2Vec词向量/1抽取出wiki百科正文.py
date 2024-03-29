#coding:utf-8
import codecs
import re

import bz2file
import opencc
from gensim.corpora.wikicorpus import extract_pages, filter_wiki
from tqdm import tqdm

wiki = extract_pages(bz2file.open('../zhwiki-20220520-pages-articles-multistream.xml.bz2'))

def wiki_replace(d):
    s = d[1]
    s = re.sub(':*{\|[\s\S]*?\|}', '', s)
    s = re.sub('[\s\S]*?', '', s)
    s = re.sub('(.){{([^{}\n]*?\|[^{}\n]*?)}}', '\\1[[\\2]]', s)
    s = filter_wiki(s)
    s = re.sub('\* *\n|\'{2,}', '', s)
    s = re.sub('\n+', '\n', s)
    s = re.sub('\n[:;]|\n +', '\n', s)
    s = re.sub('\n==', '\n\n==', s)
    # cc = opencc.OpenCC('mix2s') #该版本没有mix2s
    # OpenCC有4种转换模式
    # t2s - 繁体转简体
    # s2t - 简体转繁体
    # mix2t - 混合体转繁体
    # mix2s - 混合体转简体
    cc = opencc.OpenCC()
    return cc.convert(s).strip()
    # return s

i = 0
f = codecs.open('../wiki.txt', 'w', encoding='utf-8')
w = tqdm(wiki, desc=u'已获取0篇文章')
for d in w:
    #re.findall返回正则表达式匹配的所有字符串，用于去掉帮助页面和重定向页面;
    if not re.findall('^[a-zA-Z]+:', d[0]) and not re.findall(u'^#', d[1]):
        s = wiki_replace(d)
        f.write(s+'\n\n\n')
        i += 1
        #print(u'已获取%s篇文章'%i)
        if i % 100 == 0:
            w.set_description(u'已获取%s篇文章'%i)

f.close()