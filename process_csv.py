import argparse
import sys


def compare_csv_files(file1, file2, output):
    """
    Compares csv files
    :param file1: file for comparison
    :param file2: file for comparison
    :param output: output file path
    """
    pass
    # compare them


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
