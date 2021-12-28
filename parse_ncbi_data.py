import pandas as pd
import matplotlib.pyplot as plt
from typing import Dict


class ParseFastq:
    """
    A class to read and parse fastq file and convert it to usable formats for further analysis

    """

    def __init__(self, input_file: str):
        """
        Constructs all necessary attributes for the object ParseFastq by first reading the lines of the fastq file and
        then making a list of sequences with 4 lines per sequence.

        :param input_file:The fastq format file is the input
        """
        self.input_file = input_file
        self.read_lines = []
        self.sequence_list = []

        # open and read all lines in the fastq file
        with open(self.input_file, 'r') as fastq_file:
            for lines in fastq_file:
                self.read_lines.append(lines.rstrip('\n'))

        # break into groups of 4
        for line in range(0, len(self.read_lines), 4):
            single_sequence = self.read_lines[line:line + 4]
            if single_sequence[0].startswith('@') and (len(single_sequence[1]) == len(single_sequence[3])):
                self.sequence_list.append(single_sequence)
            else:
                print(f'sequence mismatch with id starts with {single_sequence[0][0]}, '
                      f'read length {len(single_sequence[1])}, quality length {len(single_sequence[3])}')
        print(self.sequence_list)

    def fastq_to_csv(self) -> pd.DataFrame:
        """
        Converts the sequence list into a dataframe format for further analysis, where each row contains a sequence
        having attributes 'seq_id', 'seq_reads', 'id2', 'seq_quality'.

        :return: sequence dataframe
        """
        sequence_df = pd.DataFrame(self.sequence_list, columns=['seq_id', 'seq_reads', 'id2', 'seq_quality'])
        # print(sequence_df)
        return sequence_df

    def fastq_to_dict(self) -> Dict:
        """
        Converts the sequence list into a dictionary format for further analysis, where the first sequence id is key
        and the values are a list of sequence reads, id2 and sequence quality.

        :return:
        """
        sequence_dict = {k[0]: k[1:2]+k[3:] for k in self.sequence_list}
        # print(list(sequence_dict.items())[0])
        return sequence_dict

    @staticmethod
    def count_reads(seq_df: pd.DataFrame):
        """
        Counts the number of reads.

        :param seq_df: A sequence dataframe
        :return: prints the count of reads
        """
        count_reads = len(seq_df['seq_reads'])
        print(f"The count of reads is {count_reads}")

    @staticmethod
    def distribution_reads(seq_reads: pd.Series):
        """
        Function to determine the length of each read and making a histogram of read length.

        :param seq_reads:
        :return: Outputs a distribution of read length
        """
        dist = seq_reads.apply(len)
        print(f"read_distribution {dist.describe()}")
        print("Histogram of read lengths")
        plt.hist(x=dist, bins=50, color='#0504aa', alpha=0.7, rwidth=0.85)
        plt.grid(axis='y', alpha=0.75)
        plt.xlabel('Read Length')
        plt.ylabel('Frequency')
        plt.title('Distribution of Read Length')
        plt.show()


if __name__ == '__main__':
    # seq is an instance of class ParseFastq
    seq = ParseFastq('sra_data/SRR17066006.fastq')

    # when method fastq_to_csv is called, python internally converts the fastq file to a list of
    # individual sequences so that the list can be used to perform various analytics operations.
    df = seq.fastq_to_csv()
    seq.count_reads(df)
    seq.distribution_reads(df['seq_reads'])

    print("**************")
    seq_dict = seq.fastq_to_dict()
