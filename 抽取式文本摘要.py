#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Jia ShiLin

# !/user/bin/python
# coding:utf-8

import codecs
import os

import jieba
import nltk
import numpy


class SummaryTxt:
    def __init__(self, stopwordspath):
        # 单词数量
        self.N = 100
        # 单词间的距离
        self.CLUSTER_THRESHOLD = 5
        # 返回的top n句子
        self.TOP_SENTENCES = 5
        self.stopwrods = {}
        # 加载停用词
        if os.path.exists(stopwordspath):
            stoplist = [line.strip() for line in codecs.open(stopwordspath, 'r', encoding='utf8').readlines()]
            self.stopwrods = {}.fromkeys(stoplist)

    def _split_sentences(self, texts):
        '''
        把texts拆分成单个句子，保存在列表里面，以（.!?。！？）这些标点作为拆分的意见，
        :param texts: 文本信息
        :return:
        '''
        splitstr = '.!?。！？'  # .decode('utf8')
        start = 0
        index = 0  # 每个字符的位置
        sentences = []
        for text in texts:
            if text in splitstr:  # 检查标点符号下一个字符是否还是标点
                sentences.append(texts[start:index + 1])  # 当前标点符号位置
                start = index + 1  # start标记到下一句的开头
            index += 1
        if start < len(texts):
            sentences.append(texts[start:])  # 这是为了处理文本末尾没有标

        return sentences

    def _score_sentences(self, sentences, topn_words):
        '''
        利用前N个关键字给句子打分
        :param sentences: 句子列表
        :param topn_words: 关键字列表
        :return:
        '''
        scores = []
        sentence_idx = -1
        for s in [list(jieba.cut(s)) for s in sentences]:
            sentence_idx += 1
            word_idx = []
            for w in topn_words:
                try:
                    word_idx.append(s.index(w))  # 关键词出现在该句子中的索引位置
                except ValueError:  # w不在句子中
                    pass
            word_idx.sort()
            if len(word_idx) == 0:
                continue
            # 对于两个连续的单词，利用单词位置索引，通过距离阀值计算族
            clusters = []
            cluster = [word_idx[0]]
            i = 1
            while i < len(word_idx):
                if word_idx[i] - word_idx[i - 1] < self.CLUSTER_THRESHOLD:
                    cluster.append(word_idx[i])
                else:
                    clusters.append(cluster[:])
                    cluster = [word_idx[i]]
                i += 1
            clusters.append(cluster)
            # 对每个族打分，每个族类的最大分数是对句子的打分
            max_cluster_score = 0
            for c in clusters:
                significant_words_in_cluster = len(c)
                total_words_in_cluster = c[-1] - c[0] + 1
                score = 1.0 * significant_words_in_cluster * significant_words_in_cluster / total_words_in_cluster
                if score > max_cluster_score:
                    max_cluster_score = score
            scores.append((sentence_idx, max_cluster_score))
        return scores

    def summaryScoredtxt(self, text):
        # 将文章分成句子
        sentences = self._split_sentences(text)

        # 生成分词
        words = [w for sentence in sentences for w in jieba.cut(sentence) if w not in self.stopwrods if
                 len(w) > 1 and w != '\t']
        # words = []
        # for sentence in sentences:
        #     for w in jieba.cut(sentence):
        #         if w not in stopwords and len(w) > 1 and w != '\t':
        #             words.append(w)

        # 统计词频
        wordfre = nltk.FreqDist(words)

        # 获取词频最高的前N个词
        topn_words = [w[0] for w in sorted(wordfre.items(), key=lambda d: d[1], reverse=True)][:self.N]

        # 根据最高的n个关键词，给句子打分
        scored_sentences = self._score_sentences(sentences, topn_words)

        # 利用均值和标准差过滤非重要句子
        avg = numpy.mean([s[1] for s in scored_sentences])  # 均值
        std = numpy.std([s[1] for s in scored_sentences])  # 标准差
        summarySentences = []
        for (sent_idx, score) in scored_sentences:
            if score > (avg + 0.5 * std):
                summarySentences.append(sentences[sent_idx])
                print(sentences[sent_idx])
        return summarySentences

    def summaryTopNtxt(self, text):
        # 将文章分成句子
        sentences = self._split_sentences(text)

        # 根据句子列表生成分词列表
        words = [w for sentence in sentences for w in jieba.cut(sentence) if w not in self.stopwrods if
                 len(w) > 1 and w != '\t']
        # words = []
        # for sentence in sentences:
        #     for w in jieba.cut(sentence):
        #         if w not in stopwords and len(w) > 1 and w != '\t':
        #             words.append(w)

        # 统计词频
        wordfre = nltk.FreqDist(words)

        # 获取词频最高的前N个词
        topn_words = [w[0] for w in sorted(wordfre.items(), key=lambda d: d[1], reverse=True)][:self.N]

        # 根据最高的n个关键词，给句子打分
        scored_sentences = self._score_sentences(sentences, topn_words)

        top_n_scored = sorted(scored_sentences, key=lambda s: s[1])[-self.TOP_SENTENCES:]
        top_n_scored = sorted(top_n_scored, key=lambda s: s[0])
        summarySentences = []
        for (idx, score) in top_n_scored:
            print(sentences[idx])
            summarySentences.append(sentences[idx])

        return sentences


if __name__ == '__main__':
    obj = SummaryTxt('stopword.txt')

    txt=u'十八大以来的五年，是党和国家发展进程中极不平凡的五年。面对世界经济复苏乏力、局部冲突和动荡频发、全球性问题加剧的外部环境，面对我国经济发展进入新常态等一系列深刻变化，我们坚持稳中求进工作总基调，迎难而上，开拓进取，取得了改革开放和社会主义现代化建设的历史性成就。' \
        u'为贯彻十八大精神，党中央召开七次全会，分别就政府机构改革和职能转变、全面深化改革、全面推进依法治国、制定“十三五”规划、全面从严治党等重大问题作出决定和部署。五年来，我们统筹推进“五位一体”总体布局、协调推进“四个全面”战略布局，“十二五”规划胜利完成，“十三五”规划顺利实施，党和国家事业全面开创新局面。' \
        u'经济建设取得重大成就。坚定不移贯彻新发展理念，坚决端正发展观念、转变发展方式，发展质量和效益不断提升。经济保持中高速增长，在世界主要国家中名列前茅，国内生产总值从五十四万亿元增长到八十万亿元，稳居世界第二，对世界经济增长贡献率超过百分之三十。供给侧结构性改革深入推进，经济结构不断优化，数字经济等新兴产业蓬勃发展，高铁、公路、桥梁、港口、机场等基础设施建设快速推进。农业现代化稳步推进，粮食生产能力达到一万二千亿斤。城镇化率年均提高一点二个百分点，八千多万农业转移人口成为城镇居民。区域发展协调性增强，“一带一路”建设、京津冀协同发展、长江经济带发展成效显著。创新驱动发展战略大力实施，创新型国家建设成果丰硕，天宫、蛟龙、天眼、悟空、墨子、大飞机等重大科技成果相继问世。南海岛礁建设积极推进。开放型经济新体制逐步健全，对外贸易、对外投资、外汇储备稳居世界前列。' \
        u'全面深化改革取得重大突破。蹄疾步稳推进全面深化改革，坚决破除各方面体制机制弊端。改革全面发力、多点突破、纵深推进，着力增强改革系统性、整体性、协同性，压茬拓展改革广度和深度，推出一千五百多项改革举措，重要领域和关键环节改革取得突破性进展，主要领域改革主体框架基本确立。中国特色社会主义制度更加完善，国家治理体系和治理能力现代化水平明显提高，全社会发展活力和创新活力明显增强。'

    # txt ='The information disclosed by the Film Funds Office of the State Administration of Press, Publication, Radio, Film and Television shows that, the total box office in China amounted to nearly 3 billion yuan during the first six days of the lunar year (February 8 - 13), an increase of 67% compared to the 1.797 billion yuan in the Chinese Spring Festival period in 2015, becoming the "Best Chinese Spring Festival Period in History".' \
    #      'During the Chinese Spring Festival period, "The Mermaid" contributed to a box office of 1.46 billion yuan. "The Man From Macau III" reached a box office of 680 million yuan. "The Journey to the West: The Monkey King 2" had a box office of 650 million yuan. "Kung Fu Panda 3" also had a box office of exceeding 130 million. These four blockbusters together contributed more than 95% of the total box office during the Chinese Spring Festival period.' \
    #      'There were many factors contributing to the popularity during the Chinese Spring Festival period. Apparently, the overall popular film market with good box office was driven by the emergence of a few blockbusters. In fact, apart from the appeal of the films, other factors like film ticket subsidy of online seat-selection companies, cinema channel sinking and the film-viewing heat in the middle and small cities driven by the home-returning wave were all main factors contributing to this blowout. A management of Shanghai Film Group told the 21st Century Business Herald.'
    # txt = 'Monetary policy summary The Bank of England’s Monetary Policy Committee (MPC) sets monetary policy in order to meet the 2% inflation target and in a way that helps to sustain growth and employment.  At its meeting ending on 5 August 2015, the MPC voted by a majority of 8-1 to maintain Bank Rate at 0.5%.  The Committee voted unanimously to maintain the stock of purchased assets financed by the issuance of central bank reserves at £375 billion, and so to reinvest the £16.9 billion of cash flows associated with the redemption of the September 2015 gilt held in the Asset Purchase Facility. CPI inflation fell back to zero in June.  As set out in the Governor’s open letter to the Chancellor, around three quarters of the deviation of inflation from the 2% target, or 1½ percentage points, reflects unusually low contributions from energy, food, and other imported goods prices.  The remaining quarter of the deviation of inflation from target, or ½ a percentage point, reflects the past weakness of domestic cost growth, and unit labour costs in particular.  The combined weakness in domestic costs and imported goods prices is evident in subdued core inflation, which on most measures is currently around 1%. With some underutilised resources remaining in the economy and with inflation below the target, the Committee intends to set monetary policy in order to ensure that growth is sufficient to absorb the remaining economic slack so as to return inflation to the target within two years.  Conditional upon Bank Rate following the gently rising path implied by market yields, the Committee judges that this is likely to be achieved. In its latest economic projections, the Committee projects UK-weighted world demand to expand at a moderate pace.  Growth in advanced economies is expected to be a touch faster, and growth in emerging economies a little slower, than in the past few years.  The support to UK exports from steady global demand growth is expected to be counterbalanced, however, by the effect of the past appreciation of sterling.  Risks to global growth are judged to be skewed moderately to the downside reflecting, for example, risks to activity in the euro area and China. Private domestic demand growth in the United Kingdom is expected to remain robust.  Household spending has been supported by the boost to real incomes from lower food and energy prices.  Wage growth has picked up as the labour market has tightened and productivity has strengthened.  Business and consumer confidence remain high, while credit conditions have continued to improve, with historically low mortgage rates providing support to activity in the housing market.  Business investment has made a substantial contribution to growth in recent years.  Firms have invested to expand capacity, supported by accommodative financial conditions.  Despite weakening slightly, surveys suggest continued robust investment growth ahead.  This will support the continuing increase of underlying productivity growth towards past average rates. Robust private domestic demand is expected to produce sufficient momentum to eliminate the margin of spare capacity over the next year or so, despite the continuing fiscal consolidation and modest global growth.  This is judged likely to generate the rise in domestic costs expected to be necessary to return inflation to the target in the medium term. The near-term outlook for inflation is muted.  The falls in energy prices of the past few months will continue to bear down on inflation at least until the middle of next year.  Nonetheless, a range of measures suggest that medium-term inflation expectations remain well anchored.  There is little evidence in wage settlements or spending patterns of any deflationary mindset among businesses and households. Sterling has appreciated by 3½% since May and 20% since its trough in March 2013.  The drag on import prices from this appreciation will continue to push down on inflation for some time to come, posing a downside risk to its path in the near term.  Set against that, the degree of slack in the economy has diminished substantially over the past two and a half years.  The unemployment rate has fallen by more than 2 percentage points since the middle of 2013, and the ratio of job vacancies to unemployment has returned from well below to around its pre-crisis average.  The margin of spare capacity is currently judged to be around ½% of GDP, with a range of views among MPC members around that central estimate.  A further modest tightening of the labour market is expected, supporting a continued firming in the growth of wages and unit labour costs over the next three years, counterbalancing the drag on inflation from sterling. Were Bank Rate to follow the gently rising path implied by market yields, the Committee judges that demand growth would be sufficient to return inflation to the target within two years.  In its projections, inflation then moves slightly above the target in the third year of the forecast period as sustained growth leads to a degree of excess demand. Underlying those projections are significant judgements in a number of areas, as described in the August Inflation Report.  In any one of these areas, developments might easily turn out differently than assumed with implications for the outlook for growth and inflation, and therefore for the appropriate stance of monetary policy.  Reflecting that, there is a spread of views among MPC members about the balance of risks to inflation relative to the best collective judgement presented in the August Report.  At the Committee’s meeting ending on 5 August, the majority of MPC members judged it appropriate to leave the stance of monetary policy unchanged at present.  Ian McCafferty preferred to increase Bank Rate by 25 basis points, given his view that demand growth and wage pressures were likely to be greater, and the margin of spare capacity smaller, than embodied in the Committee’s collective August projections. All members agree that, given the likely persistence of the headwinds weighing on the economy, when Bank Rate does begin to rise, it is expected to do so more gradually and to a lower level than in recent cycles.  This guidance is an expectation, not a promise.  The actual path Bank Rate will follow over the next few years will depend on the economic circumstances.  The Committee will continue to monitor closely the incoming data.'
    print(txt)
    print("--")
    obj.summaryScoredtxt(txt)

    print("----")
    obj.summaryTopNtxt(txt)