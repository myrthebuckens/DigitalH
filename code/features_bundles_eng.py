import pandas as pd
import spacy
import argparse

def feature_extraction(trainfile, output_file):

    #read file
    df = pd.read_csv(trainfile, sep = '\t')

    #subset to leave out sentence number
    df_sub = df[['sentences', 'label']]

    # load Dutch spacy model
    nlp = spacy.load("nl_core_news_sm")

    #creating lists for features
    length = []
    nwords = []
    #pos_tags = []
    #dep_relations = []
    trigramslist = []
    prn_first_feat = []
    prn_second_feat = []
    prn_third_feat = []

    #extracting features
    for sents in df_sub['sentences']:

        #average sentence length
        sen_length = (len(sents)/10)
        length.append(sen_length)

        #words per sentence
        splitted = sents.split(' ')
        nwords.append(len(splitted))

        #trigrams
        N = 3 #length of trigram
        grams = [splitted[i:i + N] for i in range(len(splitted) - N + 1)]
        trigramslist.append(grams)

        # #pos tag and dependency
        # doc = nlp(sents)
        # tokens = []
        # dependencies = []
        # for token in doc:
        #     tokens.append(token.pos_)
        #     dependencies.append(token.dep_)
        #
        # pos_tags.append(tokens)
        # dep_relations.append(dependencies)

        #pronouns
        prn_first = []
        prn_second = []
        prn_third = []

        # letterlijke string match of string match surrounded by _
        first = ['I', 'my', 'My', 'myself', 'Myself']
        second = ['You', 'you', 'Your', 'your', 'yourself', 'Yourself' ]
        third = ['She', 'she', 'her', 'Her', 'He' 'he', 'His', 'his', 'herself', 'Herself', 'himself', 'Himself']

        for word in splitted:
            if word in first:
                prn_first.append(1)
            else:
                prn_first.append(0)

            if word in second:
                prn_second.append(1)
            else:
                prn_second.append(0)

            if word in third:
                prn_third.append(1)
            else:
                prn_third.append(0)

        prn_first_feat.append(max(prn_first))
        prn_second_feat.append(max(prn_second))
        prn_third_feat.append(max(prn_third))

        #in loop combineren met 'if pos = PRON', gaat niet lukken want niet altijd herkend als PRON
        #add to dictionary counts voor iedere pronoun, voor 'zijn' checken of het ook een pronoun is, 'haar'

    #adding to df
    df_sub['length'] = length
    df_sub['n_words'] = nwords
    #df_sub['pos_tag'] = pos_tags
    #df_sub['dependency'] = dep_relations
    df_sub['trigrams'] = trigramslist
    df_sub['prn_first'] = prn_first_feat
    df_sub['prn_second'] = prn_second_feat
    df_sub['prn_third'] = prn_third_feat
    df_sub.to_csv(output_file, sep = '\t')

    return df_sub

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('input_file',
                        help='file path to data for feature extraction.')
    parser.add_argument('output_file',
                        help='file path to write output to.')

    args = parser.parse_args()

    feature_extraction(args.input_file, args.output_file)

if __name__ == '__main__':
    main()