import pandas as pd
import argparse
from math import floor

def get_training_and_testing_sets(file_list):
    """
     :param file_list: list with data to split
     :return: list with training set, list with test set
    """
    # splitting to 80/20 for training and test
    split = 0.8
    split_index = floor(len(file_list) * split)
    training = file_list[:split_index]
    testing = file_list[split_index:]
    return training, testing

def splitting(input_file, output_path_training, output_path_test):
    """
     :param input_file: path to input file with data
     :param output_path_training: path to output file for writing training set
     :param output_path_test:  path to output file for writing test set
    """
    # reading data
    df = pd.read_csv(input_file, sep ='\t')

    #grouping by label
    grouped = df.groupby(df.label)

    dr = grouped.get_group("droogstoppel")
    st = grouped.get_group("stern")
    mu = grouped.get_group("multatuli")

    # running splitting function on all three characters
    dr_train, dr_test = get_training_and_testing_sets(dr)
    st_train, st_test = get_training_and_testing_sets(st)
    mu_train, mu_test = get_training_and_testing_sets(mu)

    # concatenating all three characters
    all_training = [dr_train, st_train, mu_train]
    training = pd.concat(all_training)

    all_test = [dr_test, st_test, mu_test]
    test = pd.concat(all_test)

    # writing to files
    training.to_csv(output_path_training, sep = '\t')
    test.to_csv(output_path_test, sep = '\t')

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('input_file',
                        help='file path to data for feature extraction.')
    parser.add_argument('output_path_training',
                        help='file path to write output to for training data.')
    parser.add_argument('output_path_test',
                         help = 'file path to write output to for test data.')

    args = parser.parse_args()

    splitting(args.input_file, args.output_path_training, args.output_path_test)

if __name__ == '__main__':
    main()


