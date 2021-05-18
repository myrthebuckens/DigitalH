import spacy
import pandas as pd

# read in raw text
with open('../data/Multatuli_English Corpus.txt', encoding='utf-8') as infile:
    content = infile.readlines()

# make separate list for each character
# the slices are based on overview in this link: https://www.dbnl.org/tekst/sote001stru01_01/sote001stru01_01_0003.php
droogstoppel = [content[4:1170], content[4515:4704], content[8104:8387], content[10074:10616], content[10626]]
stern = [content[1178:4507], content[4713:8102], content[8388:10072], content[10617]]
multatuli = [content[10619:10624], content[10628:10723]]

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

# load English spacy model
nlp = spacy.load("en_core_web_sm")

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


df.to_csv('../data/eng_labeled_sents.tsv', sep = '\t')


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