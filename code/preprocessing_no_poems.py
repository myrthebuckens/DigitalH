import spacy
import pandas as pd

# read in raw text
with open('../data/MH1881_poems_excluded.txt') as infile:
    content = infile.readlines()

# make separate list for each character
# the slices are based on overview in this link: https://www.dbnl.org/tekst/sote001stru01_01/sote001stru01_01_0003.php
droogstoppel = [content[141:1638], content[4736:4908], content[8268:8613], content[9461:10069], content[10079]]
stern = [content[1638:4736], content[4908:8268], content[8613:9461], content[10069]]
multatuli = [content[10071:10077], content[10081:13227]]

droogstoppel = [item for sublist in droogstoppel for item in sublist]
stern = [item for sublist in stern for item in sublist]
multatuli = [item for sublist in multatuli for item in sublist]
characters = [droogstoppel, stern, multatuli]

# remove newlines, and remove multiple whitespaces
ds = []
st = []
mt = []

for line in droogstoppel:
    line = ' '.join(line.split())
    ds.append(line.strip('\n'))
for line in stern:
    line = ' '.join(line.split())
    st.append(line.strip('\n'))
for line in multatuli:
    line = ' '.join(line.split())
    mt.append(line.strip('\n'))

ds = ' '.join(ds)
st = ' '.join(st)
mt = ' '.join(mt)

# load Dutch spacy model
nlp = spacy.load("nl_core_news_sm")

ds = nlp(ds)
st = nlp(st)
mt = nlp(mt)

df = pd.DataFrame()

all_sents = []
all_labels = []
for sent in ds.sents:
    if len(sent) > 3:
        all_sents.append(sent.text)
        all_labels.append('droogstoppel')
for sent in st.sents:
    if len(sent) > 3:
        all_sents.append(sent.text)
        all_labels.append('stern')
for sent in mt.sents:
    if len(sent) > 3:
        all_sents.append(sent.text)
        all_labels.append('multatuli')


df['sentences'] = all_sents
df['label'] = all_labels


# count instances per character:
# count_ds = 0
# count_st = 0
# count_mt = 0
#
# for label in all_labels:
#     if label == 'droogstoppel':
#         count_ds += 1
#     if label == 'stern':
#         count_st += 1
#     if label == 'multatuli':
#         count_mt += 1
#
# print('droogstoppel',count_ds)
# print('stern',count_st)
# print('multatuli', count_mt)


df.to_csv('../data/labeled_sents_poems_excluded.tsv', sep = '\t')


# # write sentences + character label to file
# with open('../data/sentences_with_label.tsv', 'w', encoding = 'utf-8') as outfile:
#     header = 'sentences' + '\t' + 'label' + '\n'
#     outfile.write(header)
#     for sent in ds.sents:
#         if len(sent) > 3:
#             outfile.write(sent.text + '\t' +'droogstoppel' + '\n')
#     for sent in st.sents:
#         if len(sent) > 3:
#             outfile.write(sent.text + '\t' +'stern' + '\n')
#     for sent in mt.sents:
#         if len(sent) > 3:
#             outfile.write(sent.text + '\t' +'multatuli' + '\n')