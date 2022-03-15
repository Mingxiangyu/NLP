from hanlp_restful import HanLPClient
# Fill in your auth, set language='zh' to use Chinese models
HanLP = HanLPClient('https://hanlp.hankcs.com/api', auth=None, language='mul')
doc = HanLP('In 2021, HanLPv2.1 delivers state-of-the-art multilingual NLP techniques to production environments. ' \
            '2021年、HanLPv2.1は次世代の最先端多言語NLP技術を本番環境に導入します。' \
            '2021年 HanLPv2.1为生产环境带来次世代最先进的多语种NLP技术。')
print(doc)