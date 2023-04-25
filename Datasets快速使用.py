# -*- codeing = utf-8 -*-
# @Time :2023/4/24 16:16
# @Author :xming
# @Version :1.0
# @Descriptioon :
# @Link : https://zhuanlan.zhihu.com/p/548355568
# @File :  Datasets快速使用.py

from datasets import load_dataset
# 加载公开数据集
datasets = load_dataset("madao33/new-title-chinese")
datasets

from datasets import list_datasets
# 数据集列表
print(list_datasets()[:10])

# 加载子数据集
print(load_dataset("super_glue", "boolq"))

# 按照数据划分加载
print(load_dataset("madao33/new-title-chinese", split="train"))

# 数据查看
print(datasets["train"][0])
print(datasets["train"][:2])

# 数据划分(原始的train数据集进行了划分，可以看到数据按照9:1的比例重新进行了划分）
dataset = datasets["train"]
split = dataset.train_test_split(test_size=0.1)
