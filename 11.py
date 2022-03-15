from kashgari.corpus import ChineseDailyNerCorpus

train_x, train_y = ChineseDailyNerCorpus.load_data('train')
valid_x, valid_y = ChineseDailyNerCorpus.load_data('validate')
test_x, test_y  = ChineseDailyNerCorpus.load_data('test')

print(f"train data count: {len(train_x)}")
print(f"validate data count: {len(valid_x)}")
print(f"test data count: {len(test_x)}")
train data count: 20864
validate data count: 2318
test data count: 4636
