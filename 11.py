import kashgari
from kashgari.embeddings import BERTEmbedding

bert_embed = BERTEmbedding('chinese_wwm_ext_L-12_H-768_A-12',
                           task=kashgari.LABELING,
                           sequence_length=100)
