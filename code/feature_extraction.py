### creating test and training files
import pandas as pd
import spacy

#read file
df = pd.read_csv('../data/test.tsv', sep = '\t')

# load Dutch spacy model
nlp = spacy.load("nl_core_news_sm")

#creating lists for features
length = []
nwords = []
pos_tags = []
dep_relations = []

#extracting features
for sents in df['sentences']:

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
df['length'] = length
df['n_words'] = nwords
df['pos_tag'] = pos_tags
df['dependency'] = dep_relations

#writing to new file
df.to_csv('../data/test_feat.tsv', sep = '\t')

