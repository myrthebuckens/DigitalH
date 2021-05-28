import pandas as pd
import spacy
import argparse


def feature_extraction(trainfile, output_file, language):

    #read file
    df = pd.read_csv(trainfile, sep = '\t')

    #subset to leave out sentence number
    df = df[['sentences', 'label']]

    # loading spacy model
    if language == 'en':
        nlp = spacy.load("en_core_web_sm")
    if language == "nl":
        nlp = spacy.load("nl_core_news_sm")

    #creating lists for features
    length = []
    nwords = []
    pos_tags = []
    dep_relations = []
    trigramslist = []
    prn_first_feat = []
    prn_second_feat = []
    prn_third_feat = []

    #extracting features
    for sents in df['sentences']:

        #sentence length
        sen_length = len(sents)
        length.append(sen_length)

        #words per sentence
        splitted = sents.split(' ')
        nwords.append(len(splitted))

        #trigrams
        N = 3 #length of trigram
        grams = [splitted[i:i + N] for i in range(len(splitted) - N + 1)]
        trigramslist.append(grams)

        #pos tag and dependency
        doc = nlp(sents)
        tokens = []
        dependencies = []
        for token in doc:
            tokens.append(token.pos_)
            dependencies.append(token.dep_)

        pos_tags.append(tokens)
        dep_relations.append(dependencies)
        #pronouns
        prn_first = []
        prn_second = []
        prn_third = []

        # literal string matches
        if language == 'en':
            first = ['I', 'my', 'My', 'myself', 'Myself']
            second = ['You', 'you', 'Your', 'your', 'yourself', 'Yourself']
            third = ['She', 'she', 'her', 'Her', 'He' 'he', 'His', 'his', 'herself', 'Herself', 'himself', 'Himself']

        if language == 'nl':
            first = ['ik', 'my', 'myn', 'ikzelf', 'myzelf', 'mij', 'me', 'mijne', 'myner', 'myne', 'mynen', 'Ik', 'My',
                     'Myn', 'Ikzelf', 'Myzelf', 'Mij', 'Me', 'Mijne', 'Myner', 'Myne', 'Mynen']
            second = ['jy', 'jouw', 'jou', 'je', 'uw', 'u', 'uwe', 'uwer', 'uwen', 'Jy', 'Jouw', 'Jou', 'Je', 'Uw', 'U',
                      'Uwe', 'Uwer', 'Uwen']
            third = ['hy', 'hij', 'zy', 'zij', 'zijner', 'zijne', 'zyne', 'zyner', 'zijn', 'haar', 'hare', 'Hy', 'Hij',
                     'Zy', 'Zij', 'Zijner', 'Zijne', 'Zyne', 'Zyner', 'Zijn', 'Haar', 'Hare']

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

    # adding to df
    df['length'] = length
    df['n_words'] = nwords
    df['pos_tag'] = pos_tags
    df['dependency'] = dep_relations
    df['trigrams'] = trigramslist
    df['prn_first'] = prn_first_feat
    df['prn_second'] = prn_second_feat
    df['prn_third'] = prn_third_feat

    df.to_csv(output_file, sep='\t')

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('input_file',
                        help='file path to data for feature extraction.')
    parser.add_argument('output_file',
                        help='file path to write output to.')
    parser.add_argument("language",
                        help = "language of data file")

    args = parser.parse_args()

    feature_extraction(args.input_file, args.output_file, args.language)

if __name__ == '__main__':
    main()


