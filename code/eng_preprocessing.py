import spacy
import pandas as pd
import argparse

def annotating_data(input_file, output_path_sentences, output_path_bundles):
    """
    :param input_file: file path to raw data file
    :param output_path_sentences: output path for writing annotated data in sentences to
    :param output_path_bundles: output path for writing annotated data in bundles to
    """

    # read in raw text
    with open(input_file, encoding='utf-8') as infile:
        content = infile.readlines()

    # make separate list for each character
    # the slices are based on overview in this link: https://www.dbnl.org/tekst/sote001stru01_01/sote001stru01_01_0003.php
    droogstoppel = [content[4:1170], content[4515:4704], content[8104:8387], content[10074:10616], content[10626]]
    stern = [content[1178:4507], content[4713:8102], content[8388:10072], content[10617]]
    multatuli = [content[10619:10624], content[10628:10723]]

    #flattening lists
    droogstoppel = [item for sublist in droogstoppel for item in sublist]
    stern = [item for sublist in stern for item in sublist]
    multatuli = [item for sublist in multatuli for item in sublist]

    #initializing lists for sentences
    ds = []
    st = []
    mt = []

    # remove newlines, and remove multiple whitespaces
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

    #empty df for sentences
    df = pd.DataFrame()

    droog_sents = []
    stern_sents = []
    multatuli_sents = []

    all_sents = []
    all_labels = []
    for sent in ds.sents:
        if len(sent) > 3:
            all_sents.append(sent.text)
            droog_sents.append(sent.text)
            all_labels.append('droogstoppel')
    for sent in st.sents:
        if len(sent) > 3:
            all_sents.append(sent.text)
            stern_sents.append(sent.text)
            all_labels.append('stern')
    for sent in mt.sents:
        if len(sent) > 3:
            all_sents.append(sent.text)
            multatuli_sents.append(sent.text)
            all_labels.append('multatuli')


    df['sentences'] = all_sents
    df['label'] = all_labels


    #creating new df with bundled sentences
    df_bundles = pd.DataFrame()

    bundles_sents_droog = [droog_sents[i] + droog_sents[i+1] + droog_sents[i+2]+ droog_sents[i+3]+ droog_sents[i+4]+ droog_sents[i+5]+
                           droog_sents[i+6]+ droog_sents[i+7]+ droog_sents[i+8]+ droog_sents[i+9]
                            for i in range(0, (len(droog_sents)-3), 10)]

    droog_labels = ['droogstoppel'] * len(bundles_sents_droog)

    bundles_sents_stern = [stern_sents[i] + stern_sents[i+1] + stern_sents[i+2]+ stern_sents[i+3]+ stern_sents[i+4]+ stern_sents[i+5]+
                           stern_sents[i+6]+ stern_sents[i+7]+ stern_sents[i+8]+ stern_sents[i+9]
                            for i in range(0, (len(stern_sents)-4), 10)]

    stern_labels = ['stern'] * len(bundles_sents_stern)

    bundles_sents_multa = [multatuli_sents[i] + multatuli_sents[i+1] + multatuli_sents[i+2]+multatuli_sents[i+3]+ multatuli_sents[i+4]+
                           multatuli_sents[i+5]+
                           multatuli_sents[i+6]+ multatuli_sents[i+7]+ multatuli_sents[i+8]+ multatuli_sents[i+9]
                            for i in range(0, (len(multatuli_sents)-6), 10)]

    multatuli_labels = ['multatuli'] * len(bundles_sents_multa)

    df_bundles['sentences'] = bundles_sents_droog + bundles_sents_stern + bundles_sents_multa
    df_bundles['label'] = droog_labels + stern_labels + multatuli_labels

    #writing data to files
    df.to_csv(output_path_sentences, sep = '\t')
    df_bundles.to_csv(output_path_bundles, sep= '\t')

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('input_file',
                        help='file path to plain text file. Recommended path: "../data/english/Multatuli_English Corpus.txt"')
    parser.add_argument('output_path_sentences',
                        help='file path to plain text file. Recommended path: "../data/english/eng_labeled_sents.txt"')
    parser.add_argument('output_path_bundles',
                        help='file path to location for annotated data. Recommended path: "../data/english/eng_bundels.tsv"')

    args = parser.parse_args()

    annotating_data(args.input_file, args.output_path_sentences, output_path_bundles)

if __name__ == '__main__':
    main()



