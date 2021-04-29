import random
from sklearn.model_selection import train_test_split

with open('../data/sentences_with_label.tsv') as infile:
    content = infile.readlines()

# shuffle data
random.shuffle(content)

# get sentence + gold label
sentences = []
gold_labels = []

for row in content:
    row = row.strip('\n').split('\t')
    sentences.append(row[0])
    gold_labels.append(row[1])

# split test + training data
features_train, features_test, label_train, label_test = train_test_split(sentences, gold_labels, test_size=0.20)

# load model etc 