import pandas as pd

df = pd.read_csv('../data/training1.tsv', sep = '\t')
sentences = df.sentences.values

length = []
for sents in sentences:
    if len(sents) == 19893:
        print(sents)
    length.append(len(sents))

print(max(length))
print(sum(length)/len(length))

