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
    pos_tags = []
    dep_relations = []
    trigramslist = []
    first_prons = []
    second_prons = []
    third_prons = []

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
        # letterlijke string match of string match surrounded by _
        first = [' ik ', ' my ', ' myn ', ' ikzelf ', ' myzelf ', ' mij ', ' me ', ' mijne ', ' myner ', ' myne ', ' mynen ']
        second = ['jy', 'jouw', 'jou', 'je', 'uw', 'u', 'uwe', 'uwer', 'uwen']
        third = ['hy', 'hij', 'zy', 'zij', 'zijner', 'zijne', 'zyne', 'zyner', 'zijn', 'haar', 'hare']

        for tokens in splitted:
            if any tokens in first:
                first_bool == 1
            else:
                first_bool == 0

            if any tokens in second:
                second_bool == 1
            else:
                second_bool == 0

            if any tokens in third:
                third_bool == 1
            else:
                third_bool == 0

        first_prons.append(first_bool)
        second_prons.append(second_bool)
        third_prons.append(third_bool)



        #in loop combineren met 'if pos = PRON', gaat niet lukken want niet altijd herkend als PRON
        #add to dictionary counts voor iedere pronoun, voor 'zijn' checken of het ook een pronoun is, 'haar'


    #adding to df
    df_sub['length'] = length
    df_sub['n_words'] = nwords
    df_sub['pos_tag'] = pos_tags
    df_sub['dependency'] = dep_relations
    df_sub['trigrams'] = trigramslist
    df_sub['1st pronoun'] = first_prons
    df_sub['2nd pronoun'] = second_prons
    df_sub['3rd pronoun'] = third_prons
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