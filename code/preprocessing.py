import spacy
import pandas as pd

# read in raw text
with open('../data/MH1881.txt') as infile:
    content = infile.readlines()

# make separate list for each character
# the slices are based on overview in this link: https://www.dbnl.org/tekst/sote001stru01_01/sote001stru01_01_0003.php
droogstoppel = [content[141:1797], content[4895:5078], content[8590:8840], content[10619:11227], content[11237]]
stern = [content[1797:4895], content[5078:8590], content[8840:10619], content[11227]]
multatuli = [content[11229], content[11239:14388]]

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

df.to_csv('../data/labeled_sents.tsv', sep = '\t')


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