#splitting the data to test and training file
from math import floor
import pandas as pd

df = pd.read_csv('../data/labeled_sents.tsv', sep = '\t')

print(len(df['sentences']), len(df['label']))

grouped = df.groupby(df.label)

dr = grouped.get_group("droogstoppel")
st = grouped.get_group("stern")
mu = grouped.get_group("multatuli")

def get_training_and_testing_sets(file_list):
    split = 0.8
    split_index = floor(len(file_list) * split)
    training = file_list[:split_index]
    testing = file_list[split_index:]
    return training, testing


dr_train, dr_test = get_training_and_testing_sets(dr)
st_train, st_test = get_training_and_testing_sets(st)
mu_train, mu_test = get_training_and_testing_sets(mu)

all_training = [dr_train, st_train, mu_train]
training = pd.concat(all_training)
print(training.shape)

all_test = [dr_test, st_test, mu_test]
test = pd.concat(all_test)
print(test.shape)

training.to_csv('../data/training.tsv', sep = '\t')
test.to_csv('../data/test.tsv', sep = '\t')

