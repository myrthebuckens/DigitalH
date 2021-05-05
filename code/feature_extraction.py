### creating test and training files with features
### niet heel handig want geen functies gemaakt - later nog aanpassen

import pandas as pd
import spacy

#read file
df = pd.read_csv('../data/training.tsv', sep = '\t')

#subset to leave out sentence number
df_sub = df[['sentences', 'label']]

# load Dutch spacy model
nlp = spacy.load("nl_core_news_sm")

#creating lists for features
length = []
nwords = []
pos_tags = []
dep_relations = []

#extracting features
for sents in df_sub['sentences']:

    #sentence length
    sen_length = len(sents)
    length.append(sen_length)

    #words per sentence
    splitted = sents.split(' ')
    nwords.append(len(splitted))

    #ratio words
    #verhouding tussen sentence length en n woorden per sent?

    #pos tag and dependency
    doc = nlp(sents)
    tokens = []
    dependencies = []
    for token in doc:
        tokens.append(token.pos_)
        dependencies.append(token.dep_)

    pos_tags.append(tokens)
    dep_relations.append(dependencies)


#adding to df
df_sub['length'] = length
df_sub['n_words'] = nwords
df_sub['pos_tag'] = pos_tags
df_sub['dependency'] = dep_relations

#writing to new file
df_sub.to_csv('../data/training_feat.tsv', sep = '\t')

