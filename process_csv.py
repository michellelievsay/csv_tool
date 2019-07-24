import argparse
import csv
import sys
import numpy as np


def compare_csv_files(file1, file2, output):
    """
    Compares csv files
    :param file1: file for comparison
    :param file2: file for comparison
    :param output: output file path
    """
    pass
    f1 = open(file1, 'r')
    f2 = open(file2, 'r')
    list1 = np.array(list(csv.reader(f1)))
    list2 = np.array(list(csv.reader(f2)))

    ids1 = list1[1:, 0]
    print(f'infile 1 ids: {ids1}')
    ids2 = list2[1:, 0]
    print(f'infile 2 ids: {ids2}')

    result = list()

    for id_value in ids1:
        if id_value in ids2:
            result.append(id_value)

    print(f'matches: {result}')
    with open(output, mode='w', newline='') as output_file:
        id_writer = csv.writer(output_file,
                               delimiter=',',
                               quotechar='"',
                               quoting=csv.QUOTE_MINIMAL)
        for item in result:
            id_writer.writerow([item])


def main():
    parser = argparse.ArgumentParser(
        description='Produces a CSV file containing the matched ids from '
                    'infiles 1 and 2')
    parser.add_argument('--infile1',
                        help='Path to first file for comparison',
                        required=True)
    parser.add_argument('--infile2',
                        help='Path to second file for comparison',
                        required=True)
    parser.add_argument('--outfile',
                        help='Output file path (optional)',
                        default='output.csv')
    args = parser.parse_args()
    input_file1 = args.infile1
    input_file2 = args.infile2
    output_file = args.outfile

    compare_csv_files(input_file1, input_file2, output_file)


if __name__ == '__main__':
    sys.exit(main())
